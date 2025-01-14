import os

from fastapi import HTTPException
import joblib
import numpy as np
from app.save_model import load_model

def load_preprocessors(encoder_filename="encoder.pkl", scaler_filename="scaler.pkl"):
    """
    Load the saved encoder and scaler from disk.
    """
    try:
        encoder_path = os.path.join('/app', encoder_filename)
        scaler_path = os.path.join('/app', scaler_filename)

        encoder = joblib.load(encoder_path)
        scaler = joblib.load(scaler_path)

        return encoder, scaler
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"Preprocessor file not found: {str(e)}")
    except Exception as e:
        print(f"Exception encountered: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error loading preprocessors: {str(e)}")


def predict(surface_m2, type_projet, model_filename="saved_model.keras"):
    """
    Predict the cost given the surface area and type of project.
    """
    try:
        model = load_model(model_filename)

        print(f"Predicting cost for surface_m2: {surface_m2}, type_projet: {type_projet}")
        encoder, scaler = load_preprocessors()

        # Preprocess the input
        X_encoded = encoder.transform([[type_projet]]).toarray()
        X_scaled = scaler.transform([[surface_m2]])
        X_input = np.hstack([X_scaled, X_encoded])


        # Predict using the trained model
        predicted_cost = model.predict(X_input)
        print(f"Predicted cost: {predicted_cost}, type: {type(predicted_cost)}, shape: {predicted_cost.shape}")

        # Return the scalar value
        return float(predicted_cost.item())
    except Exception as e:
        print(f"Error predicting cost: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")


