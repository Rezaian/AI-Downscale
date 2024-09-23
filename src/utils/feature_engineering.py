# src/utils/feature_engineering.py

import xarray as xr
import numpy as np

def add_topography(ds, topo_data_path):
    topo_ds = xr.open_dataset(topo_data_path)
    topo_ds = topo_ds.interp_like(ds)
    ds['elevation'] = topo_ds['elevation']
    return ds

def add_land_sea_mask(ds, mask_data_path):
    mask_ds = xr.open_dataset(mask_data_path)
    mask_ds = mask_ds.interp_like(ds)
    ds['land_sea_mask'] = mask_ds['mask']
    return ds
