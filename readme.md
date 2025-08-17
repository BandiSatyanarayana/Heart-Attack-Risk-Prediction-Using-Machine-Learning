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
	
	
## Tech Stack

**Language:** Python

**Libraries:** numpy, pandas, matplotlib, scikit-learn, boruta, imbalanced-learn

Happy Learning

Team VTUPulse.com