# scripts/train_model.py

import os
import argparse
import yaml
import numpy as np
import xarray as xr
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from src.models.downscaling_model import build_downscaling_model
from src.models.custom_loss import custom_loss
from src.utils.data_preprocessing import normalize_data

def load_data(data_path, variables):
    ds = xr.open_dataset(data_path)
    ds = normalize_data(ds, variables)
    X = ds[variables].to_array().transpose('time', 'lat', 'lon', 'variable').values
    y = ds['target_variable'].values
    return X, y

def main(config_path):
    # Load configuration
    with open(config_path) as f:
        config = yaml.safe_load(f)
    
    # Load data
    variables = ['variable1', 'variable2', 'variable3', 'elevation', 'month']
    X_train, y_train = load_data(config['data']['training_data_path'], variables)
    
    # Build model
    input_shape = (config['model']['input_shape']['height'],
                   config['model']['input_shape']['width'],
                   config['model']['input_shape']['channels'])
    model = build_downscaling_model(input_shape)
    
    # Compile model
    optimizer = Adam(learning_rate=config['training']['learning_rate'])
    model.compile(optimizer=optimizer, loss=custom_loss, metrics=['mae'])
    
    # Callbacks
    callbacks = [
        EarlyStopping(patience=5, restore_best_weights=True),
        ModelCheckpoint(config['model']['save_path'], save_best_only=True)
    ]
    
    # Train model
    model.fit(
        X_train, y_train,
        batch_size=config['training']['batch_size'],
        epochs=config['training']['epochs'],
        validation_split=config['training']['validation_split'],
        shuffle=config['training']['shuffle'],
        callbacks=callbacks
    )
    
    print("Model training complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Model Training Script')
    parser.add_argument('--config', type=str, help='Path to the config file', default='configs/train_config.yaml')
    args = parser.parse_args()
    main(args.config)
