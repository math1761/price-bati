import tensorflow as tf

def create_model(input_shape):
    """
    Create a simple neural network model for regression.
    """
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(input_shape,)),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(1)  # Output layer for regression
    ])
    
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    return model

def train_model(model, train_dataset, test_dataset, epochs=50):
    """
    Train the TensorFlow model.
    """
    history = model.fit(train_dataset, validation_data=test_dataset, epochs=epochs)
    return history
