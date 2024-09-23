# scripts/evaluate_model.py

import os
import argparse
import yaml
import numpy as np
import xarray as xr
from tensorflow.keras.models import load_model
from src.models.custom_loss import custom_loss
from src.utils.data_preprocessing import normalize_data
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def load_data(data_path, variables):
    ds = xr.open_dataset(data_path)
    ds = normalize_data(ds, variables)
    X = ds[variables].to_array().transpose('time', 'lat', 'lon', 'variable').values
    y = ds['target_variable'].values
    return X, y

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    # Denormalize if necessary
    mse = mean_squared_error(y_test.flatten(), y_pred.flatten())
    mae = mean_absolute_error(y_test.flatten(), y_pred.flatten())
    r2 = r2_score(y_test.flatten(), y_pred.flatten())
    return mse, mae, r2

def main(config_path):
    # Load configuration
    with open(config_path) as f:
        config = yaml.safe_load(f)
    
    # Load test data
    variables = ['variable1', 'variable2', 'variable3', 'elevation', 'month']
    X_test, y_test = load_data(config['data']['test_data_path'], variables)
    
    # Load model
    model = load_model(config['model']['load_path'], custom_objects={'custom_loss': custom_loss})
    
    # Evaluate model
    mse, mae, r2 = evaluate_model(model, X_test, y_test)
    
    print(f'MSE: {mse}')
    print(f'MAE: {mae}')
    print(f'R^2: {r2}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Model Evaluation Script')
    parser.add_argument('--config', type=str, help='Path to the config file', default='configs/evaluate_config.yaml')
    args = parser.parse_args()
    main(args.config)
