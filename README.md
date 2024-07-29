# Smart Agriculture Advisory System

## Overview
The Smart Agriculture Advisory System is an application designed to provide farmers with personalized advice on crop management, pest control, and irrigation scheduling. By leveraging machine learning models, the system analyzes various environmental and soil parameters to recommend the most suitable crops for cultivation.

## Dataset
The dataset used for this project is sourced from Kaggle: [Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset).

### Features
- **N (Nitrogen)**: Nitrogen content in the soil
- **P (Phosphorus)**: Phosphorus content in the soil
- **K (Potassium)**: Potassium content in the soil
- **temperature**: Temperature in degree Celsius
- **humidity**: Relative humidity in %
- **ph**: pH value of the soil
- **rainfall**: Rainfall in mm

### Target
- **label**: Type of crop to be grown

## Installation

### Prerequisites
- [Anaconda](https://www.anaconda.com/products/individual#download-section): A distribution of Python and R for scientific computing and data science.

### Steps

1. **Install Anaconda**

    Download and install Anaconda from the [official website](https://www.anaconda.com/products/individual#download-section) based on your operating system.

2. **Clone the Repository**

    ```bash
    git clone https://github.com/your-username/smart-agriculture-advisory-system.git
    cd smart-agriculture-advisory-system
    ```

3. **Create a Conda Environment**

    ```bash
    conda create --name smart-agriculture python=3.8
    conda activate smart-agriculture
    ```

4. **Install Required Libraries**

    ```bash
    pip install -r requirements.txt
    ```

5. **Install Jupyter Notebook**

    ```bash
    conda install -c conda-forge notebook
    ```

## Usage

1. **Run Jupyter Notebook**

    ```bash
    jupyter notebook
    ```

2. **Open the Notebook**

    In the Jupyter Notebook interface, open `notebooks/Smart_Agriculture_Advisory_System.ipynb` to explore the analysis, model training, and predictions.

## Project Structure

- `data/`: Contains the dataset used for training and testing.
- `notebooks/`: Jupyter notebooks for data analysis and model building.
- `models/`: Saved machine learning models.
- `scripts/`: Python scripts for data processing and model training.
- `requirements.txt`: List of required Python libraries.

## Model Details

### Model Selection
Several machine learning models were evaluated for this multi-class classification problem. The final model chosen for deployment is a Random Forest classifier due to its high accuracy and robustness.

### Model Training
The model was trained using the following steps:

1. **Data Preprocessing**: Handling missing values, scaling features, and encoding categorical variables.
2. **Feature Selection**: Identifying the most important features contributing to the prediction.
3. **Model Training**: Training the Random Forest classifier with hyperparameter tuning using GridSearchCV.

### Model Evaluation
The model's performance was evaluated using accuracy, precision, recall, and F1-score. Cross-validation was also performed to ensure the model's robustness.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.
