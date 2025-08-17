# Heart Attack Risk Prediction - Local Setup Guide

## 🚀 Project Overview
This is a Machine Learning-based web application that predicts heart attack risk using patient health parameters. The application uses pre-trained K-Nearest Neighbors (KNN) and Logistic Regression models to provide risk assessments.

## 🌐 Live Demo Available!
**🚀 [Try the Live Application](https://heart-attack-risk-prediction-k9mj.onrender.com)**

Your heart attack risk prediction app is now live and accessible worldwide!

## 📋 Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Web browser

## 🛠️ Installation Steps

### 1. Navigate to Project Directory
```bash
cd "Heart-Attack-Risk-Prediction-lnm71a"
```

### 2. Create Virtual Environment
```bash
python -m venv harp
```

### 3. Activate Virtual Environment
**On Windows (PowerShell):**
```bash
.\harp\Scripts\Activate.ps1
```
**On Windows (Command Prompt):**
```bash
harp\Scripts\activate.bat
```
**On macOS/Linux:**
```bash
source harp/bin/activate
```

### 4. Install Required Packages
```bash
pip install -r requirements.txt
```

## 🚀 Running the Application

### Method 1: Using Virtual Environment Python
```bash
.\harp\Scripts\python.exe app.py
```

### Method 2: After Activating Virtual Environment
```bash
# First activate the environment
.\harp\Scripts\Activate.ps1
# Then run the app
python app.py
```

### Method 3: Direct Python Execution
```bash
python app.py
```

## 🌐 Accessing the Application
Once the Flask app is running, open your web browser and navigate to:
```
http://127.0.0.1:5000
```
or
```
http://localhost:5000
```

## 📊 Input Parameters
The application requires the following health parameters:

| Parameter | Range | Description |
|-----------|-------|-------------|
| Age | 32 - 70 years | Patient's age |
| Total Cholesterol | 107 - 696 mg/dL | Total cholesterol level |
| Systolic BP | 83 - 295 mmHg | Systolic blood pressure |
| Diastolic BP | 48 - 142 mmHg | Diastolic blood pressure |
| BMI | 15.54 - 56.8 | Body Mass Index |
| Heart Rate | 44 - 143 bpm | Resting heart rate |
| Glucose | 40 - 394 mg/dL | Blood glucose level |

## 🤖 Available Models
- **K-Nearest Neighbors (KNN)**: Non-parametric classification algorithm
- **Logistic Regression**: Linear classification algorithm

## 📁 Project Structure
```
Heart-Attack-Risk-Prediction-lnm71a/
├── app.py                 # Main Flask application
├── models/                # Pre-trained ML models
│   ├── knn_model.pkl     # KNN model
│   ├── logreg_model.pkl  # Logistic Regression model
│   ├── scaler.pkl        # Data scaler
│   └── features.json     # Feature names
├── dataset/               # Training dataset
│   └── framingham.csv    # Heart disease dataset
├── templates/             # HTML templates
│   └── index.html        # Main web interface
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

## 🔧 Troubleshooting

### Common Issues:

1. **Port Already in Use**
   - The default port is 5000. If it's busy, you can modify `app.py` to use a different port:
   ```python
   app.run(debug=True, port=5001)
   ```

2. **Virtual Environment Activation Issues**
   - On Windows, you might need to change PowerShell execution policy:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

3. **Package Installation Errors**
   - Try upgrading pip first:
   ```bash
   python -m pip install --upgrade pip
   ```

4. **Model Loading Errors**
   - Ensure all model files are present in the `models/` directory
   - Check file permissions

### Error Messages:
- **"Module not found"**: Ensure virtual environment is activated and packages are installed
- **"Port already in use"**: Change port number or stop other services using port 5000
- **"Model loading error"**: Verify model files exist and are not corrupted

## 📚 Additional Resources

### Training New Models
If you want to retrain the models:
1. Open `Heart-Attack-Risk-Prediction.ipynb` in Jupyter Notebook
2. Run all cells to train new models
3. Models will be saved to the `models/` directory

### Dataset Information
The `framingham.csv` dataset contains:
- 4,242 patient records
- 15 features including demographics, medical history, and lab results
- Target variable: 10-year risk of coronary heart disease

## 🎯 Usage Example
1. Open the web application in your browser
2. Enter your name
3. Fill in your health parameters (use realistic values within the specified ranges)
4. Select a prediction model (KNN or Logistic Regression)
5. Click "Predict" to get your heart attack risk assessment
6. View the prediction result and confidence level

## 🔒 Security Notes
- This is a development server - not suitable for production use
- The application runs locally and doesn't store personal health data
- All predictions are made locally using pre-trained models

## 📞 Support
For issues or questions, refer to the main README.md file or check the project documentation.

---
**Happy Predicting! 🫀✨**
