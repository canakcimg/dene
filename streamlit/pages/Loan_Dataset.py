import streamlit as st
import pandas as pd
import sys
import os

# Add parent directory to path to import from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.data_import import load_data
from src.data_analysis import check_df, grab_col_names, missing_values_table


def main():
    st.title("Loan Dataset Analysis 📊")
    
    try:
        # Load data
        train_df, test_df = load_data("data/train.csv", "data/test.csv")
        
        st.header("Dataset Overview")
        tab1, tab2 = st.tabs(["Training Data", "Test Data"])
        
        with tab1:
            st.subheader("Training Dataset")
            st.dataframe(train_df)
            
            st.subheader("Dataset Information")
            col1, col2 = st.columns(2)
            with col1:
                st.write("Shape:", train_df.shape)
            with col2:
                st.write("Missing Values:", train_df.isnull().sum().sum())
            
            st.subheader("Data Types")
            st.write(train_df.dtypes)
            
        with tab2:
            st.subheader("Test Dataset")
            st.dataframe(test_df)
            
            st.subheader("Dataset Information")
            col1, col2 = st.columns(2)
            with col1:
                st.write("Shape:", test_df.shape)
            with col2:
                st.write("Missing Values:", test_df.isnull().sum().sum())
            
            st.subheader("Data Types")
            st.write(test_df.dtypes)
            
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")

if __name__ == "__main__":
    main()