
from pathlib import Path
import io
import json

import numpy as np
import tensorflow as tf
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image, UnidentifiedImageError

# Project folders
PROJECT_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = PROJECT_DIR / "models"

MODEL_PATH = MODEL_DIR / "final_pest_mobilenetv2_74_46.keras"
GATE_MODEL_PATH = MODEL_DIR / "gate_model.keras"
MAPPING_PATH = MODEL_DIR / "pest_class_mapping.json"

# Check that all required files exist
for path in (MODEL_PATH, GATE_MODEL_PATH, MAPPING_PATH):
    if not path.is_file():
        raise FileNotFoundError(f"Required project file not found: {path}")

print("Loading pest classification model...")
model = tf.keras.models.load_model(str(MODEL_PATH))
print("Pest classification model loaded.")

print("Loading relevance gate model...")
gate_model = tf.keras.models.load_model(str(GATE_MODEL_PATH))
print("Relevance gate model loaded.")

with open(MAPPING_PATH, "r", encoding="utf-8") as f:
    mapping = json.load(f)

label_to_class = {int(key): value for key, value in mapping.items()}

app = FastAPI(title="AI Pest Finder API")

# Restrict this to your frontend's deployed origin before production.
# For local testing, the wildcard allows requests from any origin.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

pest_info = {
    "rice leaf roller": "Remove heavily affected leaves, maintain field sanitation, and monitor the crop regularly.",
    "asiatic rice borer": "Remove affected plant parts, monitor for infestation, and follow recommended rice pest management practices.",
    "brown plant hopper": "Monitor hopper populations, avoid excessive nitrogen fertilizer, and use recommended integrated pest management practices.",
    "rice leafhopper": "Monitor the crop regularly, remove heavily affected plants when appropriate, and follow recommended pest management practices.",
    "black cutworm": "Remove weeds around the crop, monitor young plants, and follow recommended cutworm management practices.",
    "corn borer": "Remove severely damaged plant material, monitor regularly, and use recommended integrated pest management methods.",
    "army worm": "Inspect leaves regularly, remove heavily infested plant material, and follow recommended armyworm management practices.",
    "aphids": "Remove heavily affected leaves, encourage natural predators, and use appropriate pest-control methods when necessary.",
    "Thrips": "Remove heavily affected plant material, control weeds, monitor regularly, and follow recommended thrips management practices.",
    "Trialeurodes vaporariorum": "Monitor the underside of leaves, remove heavily infested leaves, and use recommended whitefly management practices.",
}


@app.get("/")
def home():
    return {
        "status": "success",
        "message": "AI Pest Finder API is running",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=400,
            detail="Please upload a valid image file.",
        )

    try:
        image_bytes = await file.read()

        if not image_bytes:
            raise HTTPException(status_code=400, detail="The uploaded file is empty.")

        with Image.open(io.BytesIO(image_bytes)) as uploaded_image:
            image = uploaded_image.convert("RGB")

        image = image.resize((128, 128))
        image_array = np.asarray(image, dtype=np.float32) / 255.0
        image_batch = np.expand_dims(image_array, axis=0)

        gate_probability = float(
            gate_model.predict(image_batch, verbose=0).reshape(-1)[0]
        )

        print("Gate probability:", round(gate_probability * 100, 2), "%")

        if gate_probability < 0.50:
            return {
                "success": False,
                "type": "not_supported",
                "message": (
                    "The uploaded image does not appear to contain a supported "
                    "crop pest. Please upload a clear crop image showing one "
                    "of the supported pests."
                ),
            }

        predictions = model.predict(image_batch, verbose=0)[0]
        predicted_label = int(np.argmax(predictions))

        if predicted_label not in label_to_class:
            raise RuntimeError("The predicted class is missing from the class mapping.")

        confidence = float(predictions[predicted_label] * 100)
        pest_name = label_to_class[predicted_label]

        if confidence >= 70:
            confidence_level = "High"
        elif confidence >= 50:
            confidence_level = "Moderate"
        else:
            confidence_level = "Low"

        return {
            "success": True,
            "pest": pest_name,
            "confidence": round(confidence, 2),
            "confidence_level": confidence_level,
            "management": pest_info.get(
                pest_name,
                "Follow recommended agricultural pest management practices.",
            ),
        }

    except HTTPException:
        raise
    except UnidentifiedImageError:
        raise HTTPException(
            status_code=400,
            detail="The uploaded file is not a readable image.",
        )
    except Exception:
        # Keep internal error details out of public responses.
        print("Prediction failed:", "An internal prediction error occurred.")
        raise HTTPException(
            status_code=500,
            detail="Prediction failed. Please try again later.",
        )
    finally:
        await file.close()
