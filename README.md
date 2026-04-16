# ANN Prediction API

A complete Artificial Neural Network project: from training to API to cloud deployment.

## 📁 Project Structure

```
ann-project/
├── model.py                              # Train ANN model
├── app.py                                # FastAPI application
├── model.h5                              # Trained model (generated)
├── scaler.pkl                            # StandardScaler (generated)
├── requirements.txt                      # Dependencies
├── Artificial_Neural_Network_Case_Study_data.csv  # Input data
└── README.md
```

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.8+
- pip

### 2. Setup Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare Your Data

Place your CSV file in the project directory:
```
Artificial_Neural_Network_Case_Study_data.csv
```

The CSV should have:
- Features in all columns except the last
- Target variable in the last column
- Binary classification (0 or 1)

### 5. Train the Model

```bash
python model.py
```

This will:
- Load and preprocess data
- Scale features with StandardScaler
- Train ANN with 2 hidden layers (10 → 5 neurons)
- Save `model.h5` and `scaler.pkl`

### 6. Run the API Locally

```bash
uvicorn app:app --reload
```

Visit: **http://127.0.0.1:8000/docs**

You'll see the interactive Swagger UI with:
- `/` - Home endpoint
- `/predict` - Make predictions (POST)
- `/health` - Health check (GET)

### 7. Test the API

**Using Swagger UI (http://127.0.0.1:8000/docs):**
- Click "Try it out" on `/predict`
- Enter: `{"data": [45, 60000, 1, 0, 3]}`
- Click Execute

**Using curl:**
```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"data": [45, 60000, 1, 0, 3]}'
```

**Using Python:**
```python
import requests

response = requests.post(
    "http://127.0.0.1:8000/predict",
    json={"data": [45, 60000, 1, 0, 3]}
)
print(response.json())
```

## ☁️ Deploy to Render (FREE)

### 1. Push to GitHub

```bash
git init
git add .
git commit -m "Initial ANN API"
git push origin main
```

### 2. Deploy on Render

1. Go to https://render.com
2. Sign up (free)
3. Click "New Web Service"
4. Connect your GitHub repository
5. Fill in the details:

| Field | Value |
|-------|-------|
| **Name** | ann-api (or your choice) |
| **Environment** | Python 3 |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `uvicorn app:app --host 0.0.0.0 --port 10000` |
| **Plan** | Free |

6. Click "Create Web Service"
7. Wait for deployment (2-3 minutes)

### 3. Get Your Public API Link

Once deployed, you'll get:
```
https://your-app-name.onrender.com
```

Your API endpoints:
- Homepage: `https://your-app-name.onrender.com/`
- Swagger Docs: `https://your-app-name.onrender.com/docs`
- Predictions: `https://your-app-name.onrender.com/predict`

### 4. Test Deployed API

```bash
curl -X POST "https://your-app-name.onrender.com/predict" \
  -H "Content-Type: application/json" \
  -d '{"data": [45, 60000, 1, 0, 3]}'
```

## 📊 Model Architecture

```
Input Layer (n features)
    ↓
Dense(10, activation='relu')
    ↓
Dense(5, activation='relu')
    ↓
Dense(1, activation='sigmoid')
    ↓
Output (Probability: 0-1)
```

**Hyperparameters:**
- Optimizer: Adam
- Loss: Binary Crossentropy
- Metrics: Accuracy
- Epochs: 10
- Batch Size: 10

## 🔧 Workflow Summary

1. **Data Preprocessing** ✓
   - Loaded CSV
   - Split features and target
   - Applied StandardScaler

2. **Model Building** ✓
   - 2 hidden layers (ReLU activation)
   - Output layer with Sigmoid (binary classification)

3. **Model Training** ✓
   - Optimizer: Adam
   - Loss: Binary Crossentropy
   - Evaluated on test set

4. **API Creation** ✓
   - FastAPI for easy integration
   - Automatic Swagger documentation
   - Health check endpoint

5. **Deployment** ✓
   - Free tier on Render
   - Public API link generated
   - Ready for production

## 📝 API Response Examples

**Predict Request:**
```json
{
  "data": [45, 60000, 1, 0, 3]
}
```

**Predict Response:**
```json
{
  "prediction": 0.87,
  "confidence": 0.87
}
```

## 🛠️ Troubleshooting

### ModuleNotFoundError
```bash
pip install -r requirements.txt
```

### Port Already in Use
```bash
uvicorn app:app --reload --port 8001
```

### Model Not Found
Ensure you ran `python model.py` first

### CSV Not Found
Place `Artificial_Neural_Network_Case_Study_data.csv` in the project directory

## 📚 Additional Resources

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [TensorFlow Keras](https://www.tensorflow.org/guide/keras)
- [Render Docs](https://render.com/docs)
- [Scikit-learn Preprocessing](https://scikit-learn.org/stable/modules/preprocessing.html)

## 📄 License

Free to use and modify

---

**Created:** 2026
**Status:** Ready for production
