import streamlit as st

import joblib
model=joblib.load("online_shoppers_intention'.pkl")
l1=joblib.load("le1.pkl")
l2=joblib.load("le2.pkl")
l3=joblib.load("le3.pkl")
l4=joblib.load("le4.pkl")
s=joblib.load("sd.pkl")


st.title("online_shoppers_intention")
st.write("Enter Data Description")


BounceRates=st.number_input(" Enter BounceRates")
Administrative=st.number_input(' Enter Administrative')
Administrative_Duration=st.number_input(' Enter Administrative_Duration')
Informational=st.number_input('Enter Informational')
Informational_Duration=st.number_input('Ener Informational_Duration')
Month=st.selectbox("Enter Month",['Feb', 'Mar', 'May', 'Oct', 'June', 'Jul', 'Aug', 'Nov', 'Sep','Dec'])
ProductRelated=st.number_input(" Enter ProductRelated")
ExitRates=st.number_input("Enter ExitRates")
ProductRelated_Duration=st.number_input(" Enter ProductRelated_Duration")
PageValues=st.number_input("Enter PageValues")
SpecialDay=st.number_input("Enter SpecialDay")
OperatingSystems=st.number_input("Enter OperatingSystems")
Browser=st.number_input("Enter Browser")
Region=st.number_input("Enter Region")
TrafficType=st.number_input("Enter TrafficType")
VisitorType=st.selectbox("Enter VisitorType",['Returning_Visitor', 'New_Visitor', 'Other'])
Weekend=st.selectbox("Enter Weekend",["True","False"])



Month=le1.fit_transform([Month])[0]
VisitorType=le2.fit_transform([VisitorType])[0]
Weekend=le3.fit_transform([Weekend])[0]
Revenue=le4.fit_transform([Revenue])[0]
if st.button("predict"):
    result=model.predict(s.transform([[BounceRates,Administrative,Administrative_Duration,Informational,Informational_Duration,
                                               Month,ProductRelated,ExitRates,ProductRelated_Duration,PageValues,
                                       SpecialDay,OperatingSystems,Browser,Region,TrafficType,VisitorType,Weekend]]))[0]
    st.success('the output is {}'.format(result))



