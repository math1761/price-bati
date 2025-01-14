import os
import tensorflow as tf

def save_model(model, filename="saved_model.keras"):
    """
    Save the TensorFlow model.
    """
    try:
        base_path = os.path.dirname(__file__)
        model_path = os.path.join(base_path, "saved_model.keras")
        model.save(model_path)
        print(f"Model saved to {filename}")
    except Exception as e:
        print(f"Error saving model: {str(e)}")

def load_model(filename="saved_model.keras"):
    """
    Load a saved TensorFlow model.
    """
    try:
        base_path = os.path.dirname(__file__)
        model_path = os.path.join(base_path, filename)
        
        print(f"Loading model from {model_path}")
        return tf.keras.models.load_model(model_path)
    except Exception as e:
        print(f"Error loading model: {str(e)}")
        return None
