import streamlit as st

def main():
    st.set_page_config(
        page_title="Loan Prediction App",
        page_icon="💰",
        layout="wide"
    )
    
    st.title("Loan Prediction Application 💰")
    st.markdown("""
    ### Welcome to the Loan Prediction App!
    
    This application helps predict loan approval status using machine learning.
    
    #### Features:
    - **Loan Dataset**: Explore the raw dataset
    - **EDA & Visualization**: Detailed analysis of the loan data
    - **Model Prediction**: Get loan approval predictions using our trained model
    
    #### How to use:
    1. Navigate through the pages using the sidebar
    2. Explore the dataset and visualizations
    3. Try the prediction model with your own data
    
    #### About the Model:
    - Uses CatBoost algorithm
    - Trained on historical loan data
    - Predicts loan approval status
    """)

if __name__ == "__main__":
    main()