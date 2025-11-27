# PatientProfile class stores predefined example profiles representing typical patient data.
# These profiles can be used to autofill input fields for different patient types 
# (e.g., Healthy, Average, Diabetic) to simplify testing or demonstration.

class PatientProfile:
    # Initialize the profiles dictionary with preset feature values for each patient type.
    # Each profile includes typical values for the diabetes dataset features.
    def __init__(self):
        self.profiles = {
            "Healthy": {
                'Pregnancies': 1,
                'Glucose': 99,
                'BloodPressure': 70,
                'SkinThickness': 20,
                'Insulin': 85,
                'BMI': 24.5,
                'DiabetesPedigreeFunction': 0.3,
                'Age': 25
            },
            "Average": {
                'Pregnancies': 3,
                'Glucose': 130,
                'BloodPressure': 78,
                'SkinThickness': 25,
                'Insulin': 120,
                'BMI': 30.0,
                'DiabetesPedigreeFunction': 0.6,
                'Age': 35
            },
            "Diabetic": {
                'Pregnancies': 6,
                'Glucose': 170,
                'BloodPressure': 90,
                'SkinThickness': 32,
                'Insulin': 250,
                'BMI': 38.0,
                'DiabetesPedigreeFunction': 1.0,
                'Age': 50
            }
        }

    # Retrieve the feature profile dictionary for a given patient type
    # type: string key representing the patient category ("Healthy", "Average", "Diabetic")
    # Returns: dictionary of feature names and their corresponding values for the profile,
    #          or an empty dictionary if the type is not found.
    def get_profile(self, type):
        return self.profiles.get(type, {})
