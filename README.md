# AI Pest Finder 🌿🐛

AI Pest Finder is an AI-powered web application designed to help users identify agricultural pests and related plant conditions from uploaded images. It uses deep learning models and a FastAPI backend to process images and return prediction results through a simple web interface.

## 🚀 Live Application

- **Frontend:** https://ai-pest-finder.vercel.app/
- **Backend API:** https://ai-pest-finder-api.onrender.com
- **Interactive API Documentation:** https://ai-pest-finder-api.onrender.com/docs

## ✨ Features

- **Image Upload:** Upload an image for analysis through the web interface.
- **AI-Based Prediction:** Uses trained deep learning models to analyze submitted images.
- **Pest Identification:** Predicts a class from the model's supported labels.
- **Image Validation:** Processes uploaded images through the backend API.
- **REST API:** Provides prediction functionality through FastAPI.
- **Web Interface:** Simple frontend built with HTML, CSS, and JavaScript.
- **Model-Based Classification:** Uses trained Keras models for image classification.

## 🛠️ Technology Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- FastAPI
- Uvicorn
- Pillow
- NumPy
- TensorFlow / Keras

### Machine Learning
- MobileNetV2-based classification model
- Trained Keras model files
- JSON-based class mapping

### Deployment
- Vercel for the frontend
- Render for the backend API
- GitHub for source code management

## 📁 Project Structure

```text
AI-Pest-Finder/
├── backend/
│   ├── main.py
│   └── requirements.txt
├── models/
│   ├── final_pest_mobilenetv2_74_46.keras
│   ├── gate_model.keras
│   └── pest_class_mapping.json
├── notebooks/
│   ├── 01_dataset_setup_clean.ipynb
│   ├── 02_fastapi_cleaned.ipynb
│   └── 03_non_pest_cleaned.ipynb
├── index.html
├── script.js
├── style.css
├── family.jpg
├── hero-pest.jpg
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### Prerequisites

Install the following before running the project locally:

- Python
- pip
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/jeevanreddy29/AI-Pest-Finder.git
cd AI-Pest-Finder
```

### 2. Install Backend Dependencies

```bash
pip install -r backend/requirements.txt
```

### 3. Start the Backend Server

From the project root directory, run:

```bash
uvicorn backend.main:app --reload
```

The local API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

### 4. Run the Frontend

Open `index.html` in a web browser, or use a local development server to serve the project files.

The frontend is configured to communicate with the deployed Render API. To use a local backend instead, update the API base URL in `script.js` to:

```javascript
http://127.0.0.1:8000
```

## 🔌 API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Returns the API home response |
| GET | `/health` | Checks API health |
| POST | `/predict` | Processes an uploaded image and returns prediction results |

For request formats and response details, visit the [interactive API documentation](https://ai-pest-finder-api.onrender.com/docs).

## 🧠 Machine Learning Models

The project includes trained Keras model files and a JSON class-mapping file.

- `final_pest_mobilenetv2_74_46.keras` — primary image classification model.
- `gate_model.keras` — additional model used by the application.
- `pest_class_mapping.json` — maps model output classes to their corresponding labels.

Predictions depend on the training data, image quality, supported classes, and model performance.

## 🔒 Dataset and Model Files

The `.gitignore` configuration excludes local dataset directories and temporary development files. Trained model files required by the deployed backend are stored in the `models/` directory.

Only use datasets and images that you have permission to use.

## ⚠️ Limitations

- Predictions are limited to the classes supported by the trained models.
- Results may be affected by image quality, lighting, background objects, and image resolution.
- Model predictions should be treated as assistance rather than guaranteed agricultural diagnoses.
- The free Render service may sleep after inactivity, causing the first request after a quiet period to take longer.
- Reliable predictions depend on the quality and coverage of the training dataset.

## 🔮 Future Enhancements

- Improve model accuracy with additional high-quality training data.
- Add confidence scores and clearer prediction explanations.
- Improve mobile responsiveness and accessibility.
- Add prediction history and downloadable reports.
- Add multilingual support for farmers.
- Optimize inference speed and deployment reliability.

## 👨‍💻 Author

**Jeevan Reddy**

GitHub: [jeevanreddy29](https://github.com/jeevanreddy29)

## 📄 License

Add a license file if you intend to distribute the project publicly. Until a license is specified, reuse permissions should not be assumed.
