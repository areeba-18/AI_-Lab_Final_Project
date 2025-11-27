# Import the DiabetesApp class from the src.diabetes_app module
from src.diabetes_app import DiabetesApp

# This block ensures the script runs only if executed directly (not imported as a module)
if __name__ == "__main__":
    # Create an instance of the DiabetesApp class
    app = DiabetesApp()
    # Run the app, which starts the Streamlit interface
    app.run()
