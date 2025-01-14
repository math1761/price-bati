import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import joblib

def preprocess_data(df: pd.DataFrame):
    """
    Preprocess Firestore data for TensorFlow:
    - Encode categorical variables using OneHotEncoder.
    - Standardize numerical features using StandardScaler.
    - Return TensorFlow datasets (train and test).
    """
    # Separate features and target
    X = df[['surface_m2', 'type_projet']]
    y = df['cout_total']

    # One-hot encode 'type_projet'
    encoder = OneHotEncoder()
    X_encoded = encoder.fit_transform(X[['type_projet']]).toarray()

    # Standardize 'surface_m2'
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X[['surface_m2']])

    # Combine encoded and scaled features
    import numpy as np
    X_preprocessed = np.hstack([X_scaled, X_encoded])

    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X_preprocessed, y, test_size=0.2, random_state=42)

    # Convert to TensorFlow datasets
    train_dataset = tf.data.Dataset.from_tensor_slices((X_train, y_train)).batch(32)
    test_dataset = tf.data.Dataset.from_tensor_slices((X_test, y_test)).batch(32)

    return train_dataset, test_dataset, encoder, scaler

def save_preprocessors(encoder, scaler, encoder_filename="encoder.pkl", scaler_filename="scaler.pkl"):
    """
    Save the encoder and scaler to disk using joblib.
    """
    joblib.dump(encoder, encoder_filename)
    joblib.dump(scaler, scaler_filename)
    print(f"Encoder and scaler saved to {encoder_filename} and {scaler_filename}")