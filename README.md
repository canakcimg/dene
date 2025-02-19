# Loan Prediction with Machine Learning 🏦

This project implements a machine learning model to predict loan approval probabilities using the CatBoost algorithm. The application includes a user-friendly web interface built with Streamlit for easy interaction with the prediction model.

## 📁 Project Structure

loan_prediction/
├── data/
│ ├── loan_data.csv # Loan dataset
├── models/
│ ├── catboost_model.pkl # Trained CatBoost model
├── streamlit/
│ ├── Home.py # Main Streamlit app
│ ├── pages/
│ │ ├── Model_Prediction.py # Model prediction page
│ │ ├── Data_Exploration.py # Data exploration page
│ │ └── README.md # This file
├── requirements.txt # Project dependencies
├── README.md # Project overview

## 📦 Installation

1. Clone the repository:   
    ```bash
    git clone https://github.com/yourusername/loan_prediction.git
    cd loan_prediction
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run Home.py
    ```     


## 🚀 Features

- **Data Analysis**: Comprehensive EDA and data visualization
- **Machine Learning Model**: CatBoost algorithm for loan prediction
- **Web Interface**: Interactive Streamlit application
- **Modular Code**: Well-structured Python modules in src directory

## 🛠️ Technologies Used

- Python 3.x
- Streamlit
- CatBoost
- Pandas
- NumPy
- Matplotlib
- Seaborn

## 📊 Model Features

The model considers various factors for prediction:

### Numerical Features:
- Age
- Annual Income
- Employment Length
- Loan Amount
- Interest Rate
- Loan Percent Income
- Credit History Length

### Categorical Features:
- Loan Intent
- Loan Grade
- Home Ownership Status

## 🚀 Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/loan_prediction.git
    cd loan_prediction
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run Home.py   
    ```


## 📱 Application Pages

1. **Home**: Project overview and introduction
2. **Loan Dataset**: Data exploration and statistics
3. **EDA Visualization**: Interactive data visualizations
4. **Model Prediction**: Loan approval prediction interface

## 🔍 Model Training

The model training process is documented in the Jupyter notebook:
- Data preprocessing
- Feature engineering
- Model selection
- Hyperparameter tuning
- Model evaluation

## 📈 Performance Metrics

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](link-to-issues).

## 📝 License

This project is [MIT](link-to-license) licensed.

## ✨ Acknowledgments

- Dataset source
- Contributors
- References




