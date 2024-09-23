# src/utils/interpretability.py

import shap
import numpy as np

def explain_model(model, X_sample):
    # Use DeepExplainer for deep learning models
    explainer = shap.DeepExplainer(model, X_sample)
    shap_values = explainer.shap_values(X_sample)
    return shap_values

def plot_shap_summary(shap_values, X_sample):
    shap.summary_plot(shap_values, X_sample)
