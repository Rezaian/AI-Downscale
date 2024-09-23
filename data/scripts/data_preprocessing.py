# data/scripts/data_preprocessing.py

import os
import xarray as xr
import numpy as np
import argparse
import yaml
from xesmf import Regridder

def preprocess_cmip6_data(config):
    print("Preprocessing CMIP6 data...")
    # Load raw CMIP6 data
    cmip6_files = os.listdir(config['data_paths']['raw_cmip6'])
    cmip6_ds = xr.open_mfdataset([os.path.join(config['data_paths']['raw_cmip6'], f) for f in cmip6_files],
                                 combine='by_coords')
    # Perform any necessary preprocessing steps
    return cmip6_ds

def preprocess_era5_data(config):
    print("Preprocessing ERA5 data...")
    # Load raw ERA5 data
    era5_files = os.listdir(config['data_paths']['raw_era5'])
    era5_ds = xr.open_mfdataset([os.path.join(config['data_paths']['raw_era5'], f) for f in era5_files],
                                combine='by_coords')
    # Perform any necessary preprocessing steps
    return era5_ds

def regrid_cmip6_to_era5(cmip6_ds, era5_ds, config):
    print("Regridding CMIP6 data to ERA5 resolution...")
    regridder = Regridder(cmip6_ds, era5_ds, 'bilinear')
    cmip6_regridded = regridder(cmip6_ds)
    return cmip6_regridded

def save_processed_data(ds, path):
    ds.to_netcdf(path)
    print(f"Processed data saved to {path}")

def main(config_path):
    # Load configuration
    with open(config_path) as f:
        config = yaml.safe_load(f)
    
    # Preprocess datasets
    cmip6_ds = preprocess_cmip6_data(config)
    era5_ds = preprocess_era5_data(config)
    
    # Regrid CMIP6 data
    cmip6_regridded = regrid_cmip6_to_era5(cmip6_ds, era5_ds, config)
    
    # Save processed data
    os.makedirs(config['data_paths']['processed'], exist_ok=True)
    save_processed_data(cmip6_regridded, os.path.join(config['data_paths']['processed'], 'cmip6_regridded.nc'))
    save_processed_data(era5_ds, os.path.join(config['data_paths']['processed'], 'era5_processed.nc'))
    
    print("Data preprocessing complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Data Preprocessing Script')
    parser.add_argument('--config', type=str, help='Path to the config file', default='configs/data_config.yaml')
    args = parser.parse_args()
    main(args.config)
