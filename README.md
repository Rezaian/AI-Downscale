# AI-Downscale: Machine Learning for High-Resolution Regional Climate Projections

![Project Banner](docs/images/banner.png) 

---

## Abstract

**AI-Downscale** is a research project aimed at developing a machine learning model to downscale coarse-resolution Global Climate Model (GCM) outputs to high-resolution regional climate projections over Europe. By integrating physical constraints and enhancing model interpretability, the project addresses the limitations of traditional downscaling methods. The developed Convolutional Neural Network (CNN) model incorporates domain knowledge and ensures generalizability across different regions and climate scenarios. This repository contains all the code, documentation, and resources needed to replicate the study and apply the model to your own climate data analysis projects.

---

## Table of Contents

- [Abstract](#abstract)
- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Clone the Repository](#clone-the-repository)
  - [Create a Virtual Environment](#create-a-virtual-environment)
  - [Install Dependencies](#install-dependencies)
- [Data Acquisition and Preparation](#data-acquisition-and-preparation)
  - [Data Sources](#data-sources)
  - [Data Download](#data-download)
  - [Data Preprocessing](#data-preprocessing)
- [Running the Code](#running-the-code)
  - [Training the Model](#training-the-model)
  - [Evaluating the Model](#evaluating-the-model)
  - [Interpreting the Model](#interpreting-the-model)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

---

## Features

- **High-Resolution Downscaling**: Converts coarse GCM outputs to high-resolution climate projections.
- **Physical Constraints**: Incorporates physical laws into the machine learning model to ensure physical consistency.
- **Model Interpretability**: Utilizes SHAP and LIME for model explanation and transparency.
- **Generalizability**: Designed to work across different regions and future climate scenarios.
- **Open Source**: All code and resources are available for use and adaptation under the MIT License.

---

## Installation

### Prerequisites

- **Operating System**: Linux, macOS, or Windows
- **Python**: Version 3.7 or higher
- **Git**: Version control system
- **Anaconda or Miniconda** *(Recommended)*: For environment management
- **Disk Space**: At least 50 GB free space for data storage and processing
- **Memory**: 16 GB RAM or higher recommended for processing large datasets

### Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/Rezaian/AI-Downscale.git
cd AI-Downscale
```

### Create a Virtual Environment

Using Anaconda/Miniconda:

```bash
conda create -n ai-downscale python=3.8
conda activate ai-downscale
```

Alternatively, using `venv`:

```bash
python -m venv ai-downscale
source ai-downscale/bin/activate  # On Windows use `ai-downscale\Scripts\activate`
```

### Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

## Data Acquisition and Preparation

### Data Sources

Due to the large size of climate datasets, data is **not included** in the repository. You will need to download the data from the following sources:

1. **CMIP6 GCM Data**: Obtain low-resolution GCM outputs.
   - Access via ESGF nodes: [ESGF Data Portal](https://esgf-node.llnl.gov/projects/cmip6/)
   - Variables: Near-surface air temperature (`tas`), precipitation (`pr`), etc.

2. **ERA5 Reanalysis Data**: Obtain high-resolution observational data.
   - Access via Copernicus Climate Data Store: [ERA5 Data](https://cds.climate.copernicus.eu/)
   - Variables: 2m temperature, total precipitation, etc.

3. **Additional Data**:
   - **Topography**: Elevation data from [ETOPO1](https://www.ngdc.noaa.gov/mgg/global/global.html)
   - **Land-Sea Mask**: From ERA5 or other reliable sources

### Data Download

#### 1. CMIP6 Data

Use the `data/scripts/data_acquisition.py` script to guide you through the process. Modify the script according to your specific needs and data access protocols.

**Note**: You may need to register and agree to data usage terms.

#### 2. ERA5 Data

Use the Copernicus Climate Data Store API to download ERA5 data. Instructions are available on their website.

#### 3. Download Additional Data

Download topography and land-sea mask data as required.

### Data Preprocessing

Once you have downloaded the data, preprocess it using the provided scripts.

```bash
python data/scripts/data_preprocessing.py --config configs/data_config.yaml
```

This script will:

- Regrid CMIP6 data to match the resolution of ERA5 data.
- Normalize and standardize datasets.
- Handle missing values.
- Generate additional features like topography and time variables.

---

## Running the Code

### Training the Model

1. **Configure Training Parameters**

   Edit the `configs/train_config.yaml` file to set your training parameters, such as batch size, number of epochs, learning rate, and data paths.

2. **Start Training**

   Run the training script:

   ```bash
   python scripts/train_model.py --config configs/train_config.yaml
   ```

   **Options**:

   - Use `--config` to specify a different configuration file if needed.

3. **Monitor Training**

   Training progress, including loss and metric values, will be displayed in the console. Model checkpoints will be saved to the path specified in the configuration file.

### Evaluating the Model

1. **Configure Evaluation Parameters**

   Edit the `configs/evaluate_config.yaml` file to set the evaluation parameters and data paths.

2. **Run Evaluation**

   ```bash
   python scripts/evaluate_model.py --config configs/evaluate_config.yaml
   ```

   The script will output evaluation metrics such as MSE, MAE, and R².

3. **Visualize Results**

   Use the Jupyter notebook `notebooks/model_evaluation.ipynb` to generate detailed visualizations and analyses.

   ```bash
   jupyter notebook notebooks/model_evaluation.ipynb
   ```

### Interpreting the Model

1. **Run the Interpretation Notebook**

   Open the `notebooks/model_evaluation.ipynb` notebook and execute the cells related to model interpretability.

2. **Analyze SHAP Values**

   The notebook will guide you through computing SHAP values to understand feature importance and model decision-making processes.

---

## Project Structure

```
AI-Downscale/
├── README.md
├── LICENSE
├── requirements.txt
├── configs/
│   ├── data_config.yaml
│   ├── train_config.yaml
│   └── evaluate_config.yaml
├── data/
│   ├── raw/
│   │   ├── cmip6/
│   │   └── era5/
│   ├── processed/
│   └── scripts/
│       ├── data_acquisition.py
│       └── data_preprocessing.py
├── notebooks/
│   ├── data_exploration.ipynb
│   └── model_evaluation.ipynb
├── src/
│   ├── models/
│   │   ├── downscaling_model.py
│   │   └── custom_loss.py
│   ├── utils/
│   │   ├── data_preprocessing.py
│   │   ├── feature_engineering.py
│   │   └── interpretability.py
│   └── main.py
├── scripts/
│   ├── train_model.py
│   └── evaluate_model.py
└── docs/
    ├── references.md
    └── images/
```

- **configs/**: Configuration files for data processing, training, and evaluation.
- **data/**: Data storage and processing scripts.
- **notebooks/**: Jupyter notebooks for data exploration and model evaluation.
- **src/**: Source code for models and utilities.
- **scripts/**: Command-line scripts for training and evaluation.
- **docs/**: Documentation and references.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**

2. **Create a Feature Branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Commit Your Changes**

   ```bash
   git commit -am 'Add new feature'
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/your-feature-name
   ```

5. **Open a Pull Request**

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **Data Providers**:
  - CMIP6 Project: For providing GCM outputs.
  - Copernicus Climate Change Service: For providing ERA5 reanalysis data.
- **Research Inspiration**: Based on the project proposal "AI-Downscale: Machine Learning Approaches for High-Resolution Regional Climate Projections".

---

## Contact

For questions or assistance, please contact:

- **Email**: [Rezaian@ut.ac.ir](mailto:rezaian@ut.ac.ir)
- **GitHub**: [Rezaian](https://github.com/Rezaian)

---

*Note: Ensure compliance with data usage agreements and licenses when downloading and using climate datasets. The user is responsible for obtaining necessary permissions and complying with all applicable laws and regulations.*
