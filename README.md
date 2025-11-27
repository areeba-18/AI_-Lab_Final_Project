# Diabetes Prediction Application

**Diabetes Prediction Application** is a web-based tool built using Streamlit that leverages a Support Vector Machine (SVM) model to predict the likelihood of diabetes in patients based on clinical input features. This application is designed for ease of use, allowing healthcare practitioners and users to assess diabetes risk quickly and reliably.

---

## Table of Contents

- [Diabetes Prediction Application](#diabetes-prediction-application)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Features](#features)
  - [Usage](#usage)
  - [Technical Details](#technical-details)
  - [Contributing](#contributing)

---

## Overview

The application utilizes a pre-trained Support Vector Machine (SVM) classifier trained on the PIMA Indians Diabetes dataset. Input patient parameters are preprocessed—handling missing values and scaling—before prediction. The model returns a probability score and categorizes the patient into one of three risk levels: Healthy, Average Risk, or Diabetic.

---

## Features

- **Intuitive Web Interface**: Interactive user input with manual and preset patient profiles.  
- **Robust Preprocessing**: Imputation of missing values and feature scaling ensure data integrity.  
- **Accurate Predictions**: Probability-based diabetes risk classification using a well-validated SVM model.  
- **Modular Design**: Clean separation of concerns with dedicated modules for data preprocessing, model inference, and patient profiles.  
- **Model Persistence**: Efficient model and scaler serialization for seamless deployment.  


---

Usage
-----

1.  Ensure the trained model file svm\_diabetes\_model.pkl is present in the models/ directory.
    
2.  Launch the application:
```
streamlit run main.py

```
3.  Access the app in your browser at the URL provided by Streamlit (usually http://localhost:8501).
    
4.  Select a patient profile or input patient features manually.
    
5.  Click **Predict** to obtain the diabetes risk classification and probability score.

Technical Details
-----------------

*   **Model**: Support Vector Machine (SVM) trained on PIMA Diabetes dataset.
    
*   **Preprocessing**: Replaces zero values in clinical features with mean imputation; applies standard scaling.
    
*   **Prediction**: Outputs probability of diabetes and risk category labels based on predefined thresholds.
    
*   **Patient Profiles**: Quick preset values representing typical Healthy, Average, and Diabetic patient data to facilitate ease of testing.

Contributing
------------

Contributions and suggestions are welcome. Please fork the repository and create a pull request with your enhancements or bug fixes. For major changes, please open an issue first to discuss your ideas.