# src/models/downscaling_model.py

import tensorflow as tf
from tensorflow.keras.layers import Input, Conv2D, UpSampling2D, Concatenate, BatchNormalization
from tensorflow.keras.models import Model

def build_downscaling_model(input_shape):
    inputs = Input(shape=input_shape)
    
    # Encoder
    x = Conv2D(64, (3,3), activation='relu', padding='same')(inputs)
    x = BatchNormalization()(x)
    x = Conv2D(64, (3,3), activation='relu', padding='same')(x)
    x = BatchNormalization()(x)
    skip_conn = x  # Skip connection
    
    # Bottleneck
    x = Conv2D(128, (3,3), activation='relu', padding='same')(x)
    x = BatchNormalization()(x)
    
    # Decoder
    x = UpSampling2D((2,2))(x)
    x = Conv2D(64, (3,3), activation='relu', padding='same')(x)
    x = BatchNormalization()(x)
    x = Concatenate()([x, skip_conn])
    x = Conv2D(64, (3,3), activation='relu', padding='same')(x)
    x = BatchNormalization()(x)
    
    # Output Layer
    outputs = Conv2D(1, (3,3), activation='linear', padding='same')(x)
    
    model = Model(inputs, outputs)
    return model
