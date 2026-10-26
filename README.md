# AI Pest Finder 🌿🐛

AI Pest Finder is a web-based application that uses deep learning to analyze uploaded agricultural images and predict pest-related classes supported by its trained models. It combines a web frontend with a FastAPI backend to provide an accessible image prediction workflow.

## 🚀 Live Application

- **Frontend Website:** https://ai-pest-finder.vercel.app/
- **Backend API:** https://ai-pest-finder-api.onrender.com
- **Interactive API Documentation:** https://ai-pest-finder-api.onrender.com/docs

## ✨ Features

- **Image Upload:** Submit an image through the web interface for analysis.
- **AI-Based Classification:** Uses trained deep learning models to analyze images.
- **Pest Prediction:** Returns a predicted class supported by the model.
- **Image Processing:** Processes uploaded images through the backend API.
- **REST API:** Exposes prediction functionality using FastAPI.
- **Interactive API Documentation:** Explore and test API endpoints through Swagger UI.
- **Web Interface:** Built with HTML, CSS, and JavaScript.
- **Model Integration:** Uses trained Keras models and a JSON class mapping.

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
- MobileNetV2-based image classification
- Trained Keras models
- JSON-based class mapping

### Deployment and Version Control
- Vercel — frontend hosting
- Render — backend hosting
- Git and GitHub — version control

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
├── dataset/                  # Local agricultural image dataset
├── non_pest/                 # Local non-pest image dataset
├── data/                     # Supporting local data, if used
├── index.html
├── script.js
├── style.css
├── family.jpg
├── hero-pest.jpg
├── .gitignore
└── README.md
```

**Note:** The `dataset/`, `non_pest/`, and local `data/` directories may be excluded from GitHub because they contain large datasets or local development files. Their presence in this diagram describes the local project structure; it does not mean their contents are committed to the repository.

## ⚙️ Installation and Local Setup

### Prerequisites

- Python installed on your computer
- pip
- Git
- A web browser

### 1. Clone the Repository

```bash
git clone https://github.com/jeevanreddy29/AI-Pest-Finder.git
cd AI-Pest-Finder
```

### 2. Install Backend Dependencies

```bash
pip install -r backend/requirements.txt
```

### 3. Start the Backend

Run the following command from the project root:

```bash
uvicorn backend.main:app --reload
```

The local API will be available at:

```text
http://127.0.0.1:8000
```

Open the interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

### 4. Open the Frontend

Open `index.html` in your browser or serve the project files using a local development server.

By default, `script.js` is configured to communicate with the deployed Render backend. To use your local backend instead, update the API base URL in `script.js` to:

```javascript
http://127.0.0.1:8000
```

Change only the API URL in the existing code; do not replace unrelated JavaScript.

### 5. Dataset Setup

The large `dataset/` and `non_pest/` directories are not required to be committed to GitHub for normal deployment when the application uses the trained models already included in `models/`.

For local training or experimentation, prepare the datasets according to the instructions in the relevant Jupyter notebooks. Dataset availability and directory paths may need to be configured separately.

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Returns the API's home response |
| GET | `/health` | Checks API health |
| POST | `/predict` | Accepts an image and returns prediction results |

For details about request formats and responses, visit the [Interactive API Documentation](https://ai-pest-finder-api.onrender.com/docs).

## 🧠 Machine Learning Models

The `models/` directory contains the trained models and class mapping used by the application.

- **`final_pest_mobilenetv2_74_46.keras`** — primary MobileNetV2-based classification model.
- **`gate_model.keras`** — additional model used by the application.
- **`pest_class_mapping.json`** — maps model output classes to their corresponding labels.

Prediction results depend on the supported classes, training data, image quality, and model performance. The predictions should be treated as assistance rather than guaranteed agricultural diagnoses.

## 📓 Jupyter Notebooks

The `notebooks/` directory contains notebooks for dataset preparation, backend-related experimentation, and non-pest classification work.

- `01_dataset_setup_clean.ipynb`
- `02_fastapi_cleaned.ipynb`
- `03_non_pest_cleaned.ipynb`

These notebooks document development and experimentation workflows. Running training or dataset preparation may require the relevant image datasets to be available locally.

## 🔒 Dataset Management

Large image datasets are excluded from GitHub to avoid unnecessarily increasing repository size.

The `.gitignore` file should include:

```gitignore
dataset/
non_pest/
data/
```

Keep the trained models required by the deployed backend available in the `models/` directory. Do not remove or ignore those models unless you change the backend to obtain them from another reliable source.

## ⚠️ Limitations

- Predictions are limited to classes supported by the trained models.
- Image quality, lighting, background objects, and resolution can affect results.
- Model predictions are not a substitute for professional agricultural advice.
- Render's free web services may sleep after inactivity, which can delay the first request after a quiet period.
- Training or retraining requires the appropriate datasets and compatible dependencies.

## 🔮 Future Improvements

- Improve model accuracy using additional, representative training data.
- Display prediction confidence when supported by the model output.
- Improve mobile responsiveness and accessibility.
- Add prediction history and downloadable reports.
- Add multilingual support for farmers.
- Optimize inference speed and backend availability.
- Add clear guidance when an uploaded image is unsupported or uncertain.

## 👨‍💻 Author

**Jeevan Reddy**

GitHub: https://github.com/jeevanreddy29

## 📄 License

A license has not been specified. Add an appropriate `LICENSE` file if you intend to distribute the project and define permissions for reuse.

