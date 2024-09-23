# src/utils/data_preprocessing.py

import xarray as xr
import numpy as np

def normalize_data(ds, variables):
    for var in variables:
        mean = ds[var].mean()
        std = ds[var].std()
        ds[var] = (ds[var] - mean) / std
    return ds

def handle_missing_values(ds, method='interpolate'):
    if method == 'interpolate':
        ds = ds.interpolate_na(dim='time', method='linear')
    elif method == 'fill':
        ds = ds.fillna(0)
    return ds

def create_time_features(ds):
    ds['month'] = ds['time.month']
    ds['dayofyear'] = ds['time.dayofyear']
    return ds
