# Heart Attack Risk Prediction Using Machine Learning

The fact that human life is dependent on the proper functioning
of the heart is the driving force behind this research. The heart
is a crucial part of our bodies, and heart disease has become the
leading cause of death globally. With the increase in number of 
deaths among people due to heart diseases, it becomes an issue to
be addressed.

This application takes age, BMI, Systolic BP, Diastolic BP, heart
rate and blood glucose levels as input to give the risk in percentage
associated with having a heart attack in a patient in 10 years time.

## 🌐 Live Demo

**🚀 [Try the Live Application](https://heart-attack-risk-prediction-k9mj.onrender.com)**

Your heart attack risk prediction is now live and accessible worldwide!

## 📊 Features

- **Real-time Predictions**: Get instant heart attack risk assessments
- **Two ML Models**: Choose between K-Nearest Neighbors and Logistic Regression
- **Professional Interface**: Clean, user-friendly web application
- **Accurate Results**: Based on Framingham Heart Study dataset
- **Confidence Scores**: See prediction confidence levels

## Installation of required software and Libraries (One Time)

1. Install the Anaconda Python Package
2. Open Anaconda Prompt and Move to the downloaded project directory (Heart Attack Risk Prediction) using the cd command

	Example:
	>> cd Path_of_Project_Directory
	
3. Create the virtual environment using the below command
	>>conda create -n harp python==3.11.7
4. Activate the virtual environment using the command
	>>conda activate harp
5. Now install the required Libraries using the below command
	>>pip install -r requirements.txt


## Steps to train the model after Installation of required software and Libraries
1. Open Anaconda Prompt and Move to the downloaded project directory (Heart Attack Risk Prediction) using the cd command

	Example:
	>> cd Path_of_Project_Directory
	
2. Activate the virtual environment using the command
	>>conda activate harp
	
	Note: harp is the environment created at the time of installing the software and Libraries
	
3. Next to train the model open the Jupyter Notebook using the below command
	>>jupyter notebook
4. Open the Heart-Attack-Risk-Prediction.ipynb and run all cells
5. Once the training is completed the trained model knn_model.pkl and logreg_model.pkl will be stored in the models directory


## Steps to run the Flask App after training the model 
1. Open Anaconda Prompt and Move to the downloaded project directory (Heart Attack Risk Prediction) using the cd command

	Example:
	>> cd Path_of_Project_Directory
	
2. Activate the virtual environment using the command
	>>conda activate harp
	
	Note: harp is the environment created at the time of installing the software and Libraries
	
3. Run the Flask App using the below command
	>>python app.py
	
	
## 🚀 Deployment Status

[![Deploy to Render](https://img.shields.io/badge/Deploy%20to-Render-46f3f7?style=for-the-badge&logo=render)](https://render.com)
[![Python](https://img.shields.io/badge/Python-3.12.4-blue?style=for-the-badge&logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.1.1-green?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Online-brightgreen?style=for-the-badge)](https://heart-attack-risk-prediction-k9mj.onrender.com)

## 🏗️ Tech Stack

**Language:** Python 3.12.4

**Framework:** Flask 3.1.1

**Libraries:** numpy, pandas, matplotlib, scikit-learn, boruta, imbalanced-learn, gunicorn

**Deployment:** Render (Production)

## 📱 Quick Start

1. **Try the Live App**: [https://heart-attack-risk-prediction-k9mj.onrender.com](https://heart-attack-risk-prediction-k9mj.onrender.com)
2. **Local Setup**: Follow the installation steps below
3. **Model Training**: Use the Jupyter notebook for custom training

## 🎯 Project Status

✅ **Local Development**: Complete  
✅ **Production Deployment**: Live on Render  
✅ **Auto-deploy**: Every push triggers new deployment  
✅ **HTTPS**: Automatic SSL certificate  

---

Happy Learning! 🫀✨

Team VTUPulse.com