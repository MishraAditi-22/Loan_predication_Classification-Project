import pandas as pd
import streamlit  as st
import  pickle
st.set_page_config(page_title='Loan_predictor')
st.header("Welcome to loan predictor application")
st.subheader("Please enter your details to continue...")
df=pd.read_csv("cleaned.csv")
with open('rfmodel.pkl','rb') as file:
    model=pickle.load(file)
objects={}
for i in df.columns:
    if df[i].dtype==object:
        objects[i]=list(df[i].unique())
        objects[i].sort()
print(objects)
with st.container(border=True):
    age=st.number_input('person_age:',min_value=18,max_value=99)
    income=st.number_input('person_income:')
    experience=st.number_input('person_emp_exp:')
    ownership=st.selectbox('person_house_ownership:',options=objects['person_home_ownership'])
    loan_amount=st.number_input("Loan_amount:")
    loan_intent =st.selectbox('loan_intent:',options=objects['loan_intent'])
    loan_int_rate=st.number_input('loan_int_rate')
    cb_person_cred_hist_lenght=st.number_input("credit_history:")
    credit_score=st.number_input('credit_score:')
    previous_loan_defaults_on_files=st.selectbox('is there any previous loan default on file:',options=objects['previous_loan_defaults_on_file'])
    input_vals=[[age,income,experience,objects['person_home_ownership'].index(ownership),loan_amount,objects['loan_intent'].index(loan_intent),loan_int_rate,cb_person_cred_hist_lenght,credit_score,objects['previous_loan_defaults_on_file'].index(previous_loan_defaults_on_files)]]
c1,c2,c3=st.columns([1.9,1.5,1])
if c2.button('Submit'):
    out=model.predict(input_vals)
    if out[0]==1:
        st.subheader("LOAN CAN BE SANCTIONE")
    else:
        st.subheader("LOAN CANNOT BE SANCTIONE")
