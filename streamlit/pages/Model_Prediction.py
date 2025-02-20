import streamlit as st
import pandas as pd
import pickle
import numpy as np
import sys
import os




def load_model():
    with open('.pkl\CatBoost_best_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model


def preprocess_input(input_data):
    """Preprocess the input data for prediction"""
    # Convert input to DataFrame
    df = pd.DataFrame([input_data])
    
    # Convert numeric columns to float
    numeric_columns = [
        'person_age',
        'person_income',
        'person_emp_length',
        'loan_amnt',
        'loan_int_rate',
        'loan_percent_income',
        'cb_person_cred_hist_length'
    ]
    
    for col in numeric_columns:
        df[col] = df[col].astype(float)
    

    
    df['person_home_ownership_MORTGAGE'] = (df['person_home_ownership'] == 'MORTGAGE').astype(int)
    df['person_home_ownership_OTHER'] = (df['person_home_ownership'] == 'OTHER').astype(int)
    df['person_home_ownership_OWN'] = (df['person_home_ownership'] == 'OWN').astype(int)
    df['person_home_ownership_RENT'] = (df['person_home_ownership'] == 'RENT').astype(int)
     # Create dummy variables for categorical columns with drop_first=True

# loan_intent için dummy değişkenler
    df['loan_intent_DEBTCONSOLIDATION'] = (df['loan_intent'] == 'DEBTCONSOLIDATION').astype(int)
    df['loan_intent_EDUCATION'] = (df['loan_intent'] == 'EDUCATION').astype(int)
    df['loan_intent_HOMEIMPROVEMENT'] = (df['loan_intent'] == 'HOMEIMPROVEMENT').astype(int)
    df['loan_intent_MEDICAL'] = (df['loan_intent'] == 'MEDICAL').astype(int)
    df['loan_intent_PERSONAL'] = (df['loan_intent'] == 'PERSONAL').astype(int)
    df['loan_intent_VENTURE'] = (df['loan_intent'] == 'VENTURE').astype(int)
    
    # loan_grade için dummy değişkenler
    df['loan_grade_A'] = (df['loan_grade'] == 'A').astype(int)
    df['loan_grade_B'] = (df['loan_grade'] == 'B').astype(int)
    df['loan_grade_C'] = (df['loan_grade'] == 'C').astype(int)
    df['loan_grade_D'] = (df['loan_grade'] == 'D').astype(int)
    df['loan_grade_E'] = (df['loan_grade'] == 'E').astype(int)
    df['loan_grade_F'] = (df['loan_grade'] == 'F').astype(int)
    df['loan_grade_G'] = (df['loan_grade'] == 'G').astype(int)



        # Ensure correct column order
    final_columns = [
        'person_age',
        'person_income',
        'person_emp_length',
        'loan_amnt',
        'loan_int_rate',
        'loan_percent_income',
        'cb_person_cred_hist_length',
        'person_home_ownership_MORTGAGE',
        'person_home_ownership_OTHER',
        'person_home_ownership_OWN',
        'person_home_ownership_RENT',
        'loan_intent_DEBTCONSOLIDATION',
        'loan_intent_EDUCATION',
        'loan_intent_HOMEIMPROVEMENT',
        'loan_intent_MEDICAL',
        'loan_intent_PERSONAL',
        'loan_intent_VENTURE', 
        'loan_grade_A',
        'loan_grade_B',
        'loan_grade_C',
        'loan_grade_D',
        'loan_grade_E',
        'loan_grade_F',
        'loan_grade_G',
    ]

        # Add missing columns with 0s and select only needed columns
    for col in final_columns:
        if col not in df.columns:
            df[col] = 0
            
    st.write("Final processed data:", df[final_columns])


    return df[final_columns]

def main():

    st.set_page_config(
        page_title="Loan Prediction App",
        page_icon="💰",
        layout="wide"
    )
    
    # Resim için mutlak yol oluştur
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(os.path.dirname(current_dir))
    image_path = os.path.join(parent_dir, 'streamlit', 'picture', 'bild1.webp')
    
    try:
        # Resmi göster
        st.image(image_path, use_container_width=True)
    except Exception as e:
        st.error(f"Error loading image: {str(e)}")
        # Alternatif olarak base64 encoded resim kullanabiliriz
        st.markdown("""
        <div style="text-align: center; padding: 20px; background-color: #f0f2f6; border-radius: 10px; margin-bottom: 20px;">
            <h2 style="color: #1f77b4;">🏦 Loan Prediction Model</h2>
            <p style="font-size: 18px;">Predict loan approval using machine learning</p>
        </div>
        """, unsafe_allow_html=True)

    st.title("Loan Prediction Model 🎯")

    st.markdown("""
    ### Welcome to the Loan Prediction App!
    
    This application uses machine learning to predict loan approval probability based on various factors:
    
    #### Key Features Used in Prediction:
    - **Personal Information**: Age, Income, Employment Length
    - **Loan Details**: Amount, Interest Rate, Percent of Income
    - **Loan Purpose**: Personal, Education, Medical, etc.
    - **Credit Grade**: A through G
    - **Home Ownership Status**: Own, Rent, Mortgage
    
    #### How to Use:
    1. Navigate to the 'Model Prediction' page
    2. Enter your information
    3. Click 'Predict' to see your loan approval probability
    
    #### Model Information:
    - Uses CatBoost algorithm
    - Trained on historical loan data
    - Considers multiple factors for accurate prediction
    """)

    
    try:
        model = load_model()
        
        st.header("Enter Loan Application Details")
        
        col1, col2 = st.columns(2)
        
        with col1:
            person_age = st.number_input("Age", min_value=18, max_value=100, value=30)
            person_income = st.number_input("Annual Income", min_value=0, value=50000)
            person_emp_length = st.number_input("Employment Length (years)", min_value=0, value=5)
            loan_intent = st.selectbox("Loan Intent", 
                                     ["PERSONAL", "EDUCATION", "MEDICAL", 
                                      "VENTURE", "HOMEIMPROVEMENT", "DEBTCONSOLIDATION"])
            person_home_ownership = st.selectbox("Home Ownership", 
                                               ["RENT", "MORTGAGE", "OWN", "OTHER"])
            
            
        with col2:
            loan_amnt = st.number_input("Loan Amount", min_value=0, value=10000)
            loan_int_rate = st.number_input("Interest Rate", min_value=0.0, max_value=30.0, value=10.0)
            loan_percent_income = st.number_input("Loan Percent Income", min_value=0.0, max_value=1.0, value=0.1)
            loan_grade = st.selectbox("Loan Grade", ["A", "B", "C", "D", "E", "F", "G"])
            cb_person_cred_hist_length = st.number_input("Credit History Length (years)", min_value=0, value=3)
            
        if st.button("Predict"):
            input_data = {
                'person_age': int(person_age),
                'person_income': float(person_income),
                'person_emp_length': float(person_emp_length),
                'loan_amnt': float(loan_amnt),
                'loan_int_rate': float(loan_int_rate),
                'loan_percent_income': float(loan_percent_income),
                'person_home_ownership': person_home_ownership,
                'loan_intent': loan_intent,
                'loan_grade': loan_grade,
                'cb_person_cred_hist_length': float(cb_person_cred_hist_length),
            }
            
            # Preprocess input
            processed_data = preprocess_input(input_data)
            
             # Debug için model girdisini görelim
            st.write("Model input shape:", processed_data.shape)
            #st.write("Model input columns:", processed_data.columns.tolist())
                
            # Make prediction
            prediction = model.predict(processed_data)
            probability = model.predict_proba(processed_data)
            
            # Display result
            st.header("Prediction Result")
            if prediction[0] == 1:
                st.success("Loan Approved! ✅")
            else:
                st.error("Loan Not Approved ❌")
                
            st.write(f"Approval Probability: {probability[0][1]:.2%}")
            
    except Exception as e:
        st.error(f"Error in prediction: {str(e)}")
        st.write("Debug - Error details:", str(e))

if __name__ == "__main__":
    main()