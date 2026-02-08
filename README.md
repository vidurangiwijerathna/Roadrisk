README

Road Accident Risk Prediction Application
This Streamlit application allows users to predict the risk level of road accidents based on road, weather, and traffic conditions.
The prediction model is trained on a road accident dataset and deployed using FastAPI and Streamlit to provide an interactive and user-friendly experience.

Files Included

01. main.py
Contains the FastAPI backend. It loads the trained machine learning model, defines API endpoints, processes user inputs, and returns the predicted accident risk.

02. app.py
Contains the Streamlit frontend. It provides an interface for users to enter road and traffic conditions and view the predicted accident risk.

03. Road_Accident_Risk_model.pkl
The trained machine learning model serialized using Joblib. It is loaded by FastAPI and used for all predictions.

04. requirements.txt
Lists all the required Python libraries needed to run both FastAPI and Streamlit.

05. train.csv / test.csv
These files contain the dataset used to train and test the road accident risk prediction model.

 train.csv – Used to train the machine learning model

 test.csv – Used to evaluate and validate the model

Instructions for Usage

01. Setting Up the Environment

IMPORTANT – Ensure that Python is installed on your system.
Make sure that all commands are executed inside the IDE or terminal you are using and that all project files (including the trained model file) are loaded into the same project folder.

Install all required dependencies by running:

pip install -r requirements.txt

02. Running the FastAPI Application

Run the following command in your terminal:

uvicorn main:app --reload


This will start the FastAPI development server.

You can access:

API Documentation:
http://127.0.0.1:8000/docs

API Root URL:
http://127.0.0.1:8000/

You can also use the FastAPI interface to test predictions directly. However, for the full application experience, a Streamlit-based frontend has been developed.
03. Running the Streamlit Application

Open a new terminal and run:

streamlit run app.py


This will start the Streamlit server. You will usually be redirected automatically to:

http://localhost:8501


You can now use the application to enter data and view predictions.

04. Using the Application

Once the application loads, you will see three main pages:

Home

This page introduces the application and explains its purpose and functionality.

About

This page provides information about the dataset and the problem domain used for training the model.

Prediction

This page allows you to enter the required input data (such as road and traffic conditions).
After submitting the form, the system processes the data using the trained machine learning model and displays the predicted result.
