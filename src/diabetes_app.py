import streamlit as st
import pandas as pd
from pathlib import Path
from src.diabetes_model import DiabetesModel
from src.patient_profile import PatientProfile


# DiabetesApp is a Streamlit-based web application
# It loads a pre-trained diabetes prediction model and
# provides a user interface for inputting patient data and displaying predictions
class DiabetesApp:
    def __init__(self):
        # Dynamically construct the path to the saved SVM model file
        # Path is relative to the current script location for portability
        base_path = Path(__file__).parent.resolve()  # Directory of this script
        model_path = (
            base_path.parent / "models" / "svm_diabetes_model.pkl"
        )  # ../models/svm_diabetes_model.pkl
        print(
            f"Loading model from: {model_path}"
        )  # Debug output to verify path correctness

        # Load the diabetes prediction model from the specified file path
        self.model = DiabetesModel(str(model_path))

        # Load predefined patient profiles to provide default input values
        self.profile = PatientProfile()

    # Main method to run the Streamlit app interface
    def run(self):
        # Display the app title and description
        st.title("Diabetes Prediction using SVM")
        st.markdown(
            "Predict the probability of a patient having diabetes based on input features."
        )

        # Dropdown menu to select patient type for auto-filling inputs
        # Options: Manual Input (empty/default), Healthy, Average, Diabetic
        patient_type = st.selectbox(
            "Select Patient Type:", ["Manual Input", "Healthy", "Average", "Diabetic"]
        )

        # Retrieve default input values based on the selected patient type profile
        default = self.profile.get_profile(patient_type)

        # Create three columns for a more compact side-by-side layout
        col1, col2, col3 = st.columns(3)

        # Create input fields for all features required by the model
        # Values default to those from the profile or fallback to sensible defaults
        with col1:
            user_input = {
                "Pregnancies": st.number_input(
                    "Pregnancies", 0, 20, value=default.get("Pregnancies", 1)
                ),
                "Glucose": st.number_input(
                    "Glucose", 0, 200, value=default.get("Glucose", 120)
                ),
                "BloodPressure": st.number_input(
                    "Blood Pressure", 0, 140, value=default.get("BloodPressure", 70)
                ),
            }
        with col2:
            user_input.update(
                {
                    "SkinThickness": st.number_input(
                        "Skin Thickness", 0, 100, value=default.get("SkinThickness", 20)
                    ),
                    "Insulin": st.number_input(
                        "Insulin", 0, 900, value=default.get("Insulin", 80)
                    ),
                    "BMI": st.number_input(
                        "BMI", 0.0, 70.0, value=default.get("BMI", 30.0), format="%.1f"
                    ),
                }
            )
        with col3:
            user_input.update(
                {
                    "DiabetesPedigreeFunction": st.number_input(
                        "Diabetes Pedigree Function",
                        0.0,
                        3.0,
                        value=default.get("DiabetesPedigreeFunction", 0.5),
                        format="%.3f",
                    ),
                    "Age": st.number_input(
                        "Age", 10, 100, value=default.get("Age", 30)
                    ),
                }
            )

        # When the Predict button is clicked:
        if st.button("Predict"):
            # Convert user inputs into a DataFrame for model compatibility
            input_df = pd.DataFrame([user_input])

            # Preprocess the input data to match model expectations (e.g., scaling)
            processed = self.model.preprocess(input_df)

            # Predict the probability that the patient has diabetes
            prob = self.model.predict(processed)

            # Convert the predicted probability into a human-readable label and emoji for UI
            label, emoji = self.model.classify(prob)

            # Display prediction result and probability to the user
            st.subheader(f"{emoji} Prediction: {label}")
            st.write(f"**Probability of Diabetes:** `{prob:.2f}`")
