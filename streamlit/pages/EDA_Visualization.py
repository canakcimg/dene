import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os

# Add parent directory to path to import from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.data_import import load_data, combine_data
from src.data_analysis import grab_col_names
from src.data_visualization import plot_numerical_dist, plot_correlation_matrix, plot_categorical_dist


def main():
    st.title("Exploratory Data Analysis & Visualization 📈")
    
    try:
        # Load and combine data
        train_df, test_df = load_data("data/train.csv", "data/test.csv")
        df = combine_data(train_df, test_df)
        
        # Get column types
        cat_cols, num_cols, cat_but_car = grab_col_names(df)
        
        # Create tabs for different visualizations
        tab1, tab2, tab3 = st.tabs(["Numerical Analysis", "Categorical Analysis", "Correlation Analysis"])
        
        with tab1:
            st.header("Numerical Variables Distribution")
            for col in num_cols:
                fig, ax = plt.subplots(figsize=(10, 6))
                sns.histplot(data=df, x=col, kde=True)
                plt.title(f"Distribution of {col}")
                st.pyplot(fig)
                plt.close()
        
        with tab2:
            st.header("Categorical Variables Distribution")
            for col in cat_cols:
                if col != 'loan_status':
                    fig, ax = plt.subplots(figsize=(10, 6))
                    df[col].value_counts().plot(kind='bar')
                    plt.title(f"Distribution of {col}")
                    plt.xticks(rotation=45)
                    st.pyplot(fig)
                    plt.close()
        
        with tab3:
            st.header("Correlation Matrix")
            fig, ax = plt.subplots(figsize=(12, 8))
            sns.heatmap(df[num_cols].corr(), annot=True, cmap='coolwarm')
            st.pyplot(fig)
            plt.close()
            
    except Exception as e:
        st.error(f"Error in visualization: {str(e)}")

if __name__ == "__main__":
    main()