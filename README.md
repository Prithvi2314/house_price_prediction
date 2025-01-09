# House Price Prediction Project

This project is a machine learning application that predicts house prices based on various input features. The goal is to provide accurate price predictions by analyzing housing data using advanced algorithms.

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Dataset](#dataset)
6. [Model Training](#model-training)
7. [File Structure](#file-structure)
8. [Acknowledgements](#acknowledgements)

---

## Overview
The House Price Prediction project allows users to input features like area, number of bedrooms, bathrooms, parking spaces, and others. Based on these inputs, the application predicts the price of a house using a pre-trained Linear Regression model.

---

## Features
- **Input Form:** Users can input house features via a web interface.
- **Prediction Results:** The predicted house price is displayed dynamically.
- **Machine Learning Model:** Linear Regression model trained on a housing dataset for price prediction.
- **Scalable and modular code for future improvements.
- **Visualization of data and model performance.


---


### Prerequisites
To run this project, you need:
- Python 3.8 or higher
- Virtual Environment 




## Installation
Follow these steps to set up the project on your local machine:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/house-price-prediction.git
   ```

2. Navigate to the project directory:
   ```bash
   cd house-price-prediction
   ```

3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Ensure the required dataset is placed in the `data` directory as `housing.csv`.

---

## Usage

1. Train the model (if not already trained):
   ```bash
   python train_model.py
   ```
   This script preprocesses the dataset, trains a Linear Regression model, and saves it to `model/house_price_model.pkl`.

2. Run the Flask application:
   ```bash
   python app.py
   ```
   The application will start at `http://127.0.0.1:5000/`.

3. Use the web interface to input house details and view the predicted price.

---

## Dataset
The dataset is expected to be in CSV format (`housing.csv`) and should include the following columns:
- `area`: Area of the house in square feet.
- `bedrooms`: Number of bedrooms.
- `bathrooms`: Number of bathrooms.
- `stories`: Number of stories.
- `mainroad`: Whether the house is near a main road (yes/no).
- `guestroom`: Whether the house has a guest room (yes/no).
- `basement`: Whether the house has a basement (yes/no).
- `hotwaterheating`: Whether the house has hot water heating (yes/no).
- `airconditioning`: Whether the house has air conditioning (yes/no).
- `parking`: Number of parking spaces.

---

## Model Training
The `train_model.py` script performs the following tasks:
1. Loads and preprocesses the dataset.
2. Splits the data into training and testing sets.
3. Trains a Linear Regression model using the training data.
4. Saves the trained model to `model/house_price_model.pkl`.
5. Evaluates the model and prints the R² score.

---

## File Structure
```
House Price Prediction/
├── app.py                 # Main Flask application
├── train_model.py         # Script to train the model
├── preprocess.py          # Data preprocessing script
├── model/
│   └── house_price_model.pkl  # Trained model
├── data/
│   └── housing.csv        # Dataset file
├── templates/
│   ├── index.html         # Input form template
│   └── results.html       # Results display template
```

---

## Acknowledgements
This project is created to demonstrate the use of Flask for web development and machine learning model deployment. Special thanks to open datasets and community resources for providing the base housing dataset.
