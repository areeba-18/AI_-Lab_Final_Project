import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# DiabetesModel loads a pre-trained SVM model and scaler for diabetes prediction.
# It provides methods to preprocess input data, predict diabetes probability,
# and classify the risk level based on the probability.
class DiabetesModel:
    # Initialize the model by loading from a saved file
    # model_path: string path to the saved joblib file containing model and scaler
    def __init__(self, model_path):
        data = joblib.load(model_path)  # Load model and scaler dict from disk
        self.model = data['model']      # Trained SVM model
        self.scaler = data['scaler']    # Pre-fitted scaler for feature scaling

        # List of features expected by the model in specific order
        self.features = [
            'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
            'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'
        ]

    # Preprocess input data to prepare for prediction
    # input_df: pandas DataFrame containing raw input features (single or multiple samples)
    # Returns: DataFrame with scaled features ready for model prediction
    def preprocess(self, input_df):
        # Columns where zero is invalid and should be treated as missing
        cols_with_zeros = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

        # Replace zeros with NaN to impute missing values correctly
        input_df[cols_with_zeros] = input_df[cols_with_zeros].replace(0, np.nan)

        # Predefined mean values for imputing missing data for each feature
        mean_values = {
            'Glucose': 120.9,
            'BloodPressure': 69.1,
            'SkinThickness': 20.5,
            'Insulin': 79.8,
            'BMI': 32.0
        }

        # Impute missing values with mean for each column
        for col in cols_with_zeros:
            input_df[col] = input_df[col].fillna(mean_values[col])

        # Scale features using the pre-loaded scaler to match training conditions
        scaled = self.scaler.transform(input_df[self.features])

        # Return the scaled data as a DataFrame with the same feature columns
        return pd.DataFrame(scaled, columns=self.features)

    # Predict the probability of diabetes using the processed input features
    # processed_input: DataFrame of scaled features from preprocess method
    # Returns: float probability of diabetes (value between 0 and 1)
    def predict(self, processed_input):
        try:
            # Use predict_proba to get probability of positive class (diabetes=1)
            prob = self.model.predict_proba(processed_input)[0][1]
        except:
            # If model doesn't support predict_proba, fallback to predict with fixed prob
            label = self.model.predict(processed_input)[0]
            prob = 0.8 if label == 1 else 0.2
        return prob

    # Classify risk level based on predicted diabetes probability
    # prob: float probability output from predict method
    # Returns: tuple (label string, icon string)
    # Label can be "Healthy", "Average Risk", or "Diabetic"
    def classify(self, prob):
        if prob < 0.3:
            return "Healthy", "✅"
        elif prob < 0.7:
            return "Average Risk", "⚠️"
        else:
            return "Diabetic", "❗"
