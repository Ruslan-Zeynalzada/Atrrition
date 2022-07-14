import pandas as pd
import numpy as np
import streamlit as st
import pickle
import sklearn

first_part = st.container()
data_set = st.container()
modeling = st.container()

with first_part : 
    st.title("Whether the employee has attrited or not")
    st.markdown("* **You can give inputs and click Predict button for to see predictions**")
    st.markdown("* **If you don't understand the variables press Description button**")
    
with data_set : 
    st.header("The Attrition DataSet")
    df = pickle.load(open("Attrition_data" , "rb"))
    st.write(df.head())
but_1 = st.sidebar.button("Description")
if but_1 : 
    st.header("Variables' Description")
    st.markdown("* **Age - The age of the employee**")
    st.markdown("* **Attrition - Whether the employee has attrited or not**")
    st.markdown("* **BusinessTravel - Whether the employee used to travel for business or not**")
    st.markdown("* **Department - Which department the employee was employed under**")
    st.markdown("* **DistanceFromHome - The distance the employee travels to reach for job on a day to day basis**")
    st.markdown("* **Gender - Gender of the employee**")
    st.markdown("* **JobInvolvement - The involvement rating of an employee over the job handled**")
    st.markdown("* **JobLevel - Level at which the employee is working**")
    st.markdown("* **JobRole - The roles and resposibilites of the employee**")
    st.markdown("* **JobSatisfaction - Satisfaction rating of the employee for the job**")
    st.markdown("* **MaritalStatus - Marital status of the employee**")
    st.markdown("* **MonthlyIncome - Monthly income of the employees**")
    st.markdown("* **NumCompaniesWorked - Number of companies the employees has worked for**")
    st.markdown("* **OverTime - Whether working Overtime or not**")
    st.markdown("* **PercentSalaryHike - Percentage salary hike since their appointment in the company**")
    st.markdown("* **PerformanceRating - Performance Rating of an employee**")
    st.markdown("* **StockOptionLevel - Level of opted for sharing the stock**")
    st.markdown("* **TotalWorkingYears - Total years worked by the employees**")
    st.markdown("* **TrainingTimesLastYear - How many trainings the employee has undergone**")
    st.markdown("* **YearsAtCompany - Years spent at the present organisation**")
    st.markdown("* **YearsSinceLastPromotion - Time gone in years since last promotion** ")
    st.markdown("* **YearsWithCurrManager - Years working under he current manager**")
    st.markdown("* **Higher_Education - Higher education level of the employee**")
    st.markdown("* **Date_of_Hire - Date of hire of the employee in the current organisation**")
    st.markdown("* **Status_of_leaving - Reason for leaving the organisation**")
    st.markdown("* **Mode_of_work - WFH or WFO**")
    st.markdown("* **Leaves - Total permitted leaves taken by the employee**")
    st.markdown("* **Absenteeism - Total days absent for the employee**")
    st.markdown("* **Work_accident - Work accident if any**")
    st.markdown("* **Source of Hire - Source of Hire**")
    st.markdown("* **Job_mode - Working Fulltime/ Part time/ Contractual**")

st.sidebar.header("Inputs Giving") 
Age = st.sidebar.slider("Please select input for the Age vairable" , min_value = 18 , max_value = 60 , value = 18 , step = 1)
BusinessTravel = st.sidebar.selectbox("Please select input for the BusinessTravel variable" , options = ["Travel_Rarely" , "Travel_Frequently" , "Non-Travel"] , index = 0)
Department = st.sidebar.selectbox("Please select input for the Department variable" ,  options = ["Research & Development" , "Sales" , "Human Resources"] , index = 0)
DistanceFromHome = st.sidebar.slider("Please selet input for the DistanceFromHome variable" , min_value = 1 , max_value = 2 , value = 0 , step = 1)
Gender = st.sidebar.selectbox("Please select input for the Gender variable" , options = ["Male" , "Female"] , index = 0)
JobInvolvement = st.sidebar.selectbox("Please select input for the JobInvolvement variable" , options = [1,2,3,4] , index = 0)
JobLevel = st.sidebar.selectbox("Please select input for the JobLevel variable" , options = [1,2,3,4,5] , index = 0)
JobRole = st.sidebar.selectbox("Please select input for the JobRole variable" , options = ["Sales Executive" , "Research Scientist" , "Laboratory Technician"] , index = 0)
JobSatisfaction = st.sidebar.selectbox("Please select input for the JobSatisfaction variable" , options = [1,2,3,4])
MaritalStatus = st.sidebar.selectbox("Please select input for the MaritalStatus	variable" , options = ["Married", 'Single', 'Divorced'] , index = 0)
MonthlyIncome = st.sidebar.slider("Please select input for the MonthlyIncome variable" , min_value = 1009 , max_value = 20000 , value = 1009 , step = 1)
NumCompaniesWorked = st.sidebar.selectbox("Please select input for the NumCompaniesWorked	 variable" , options = [0,1,2,3,4,5,6,7,8,9] , index = 0)
OverTime = st.sidebar.selectbox("Please select input for the OverTime variable" , options = ["No" , "Yes"] , index = 0)
PercentSalaryHike = st.sidebar.slider("Please select input for the PercentSalaryHike variable" , min_value = 11 , max_value = 25 , value = 11 , step = 1) 
PerformanceRating = st.sidebar.selectbox("Please select input for the PerformanceRating variable" , options = [3,4] , index = 0) 
StockOptionLevel = st.sidebar.selectbox("Please select input for the StockOptionLevel variable" , options = [0,1,2,3] , index = 0) 
TotalWorkingYears = st.sidebar.slider("Please select input for the TotalWorkingYears variable" , min_value = 0 , max_value = 40 , value = 0 , step = 1) 
TrainingTimesLastYear = st.sidebar.slider("Please select input for the TrainingTimesLastYear variable" , min_value = 0 , max_value = 6 , value = 0 , step = 1) 
YearsAtCompany = st.sidebar.slider("Please select input for the YearsAtCompany variable" , min_value = 0 , max_value = 40 , value = 0 , step = 1) 
YearsSinceLastPromotion = st.sidebar.slider("Please select input for the YearsSinceLastPromotion variable" , min_value = 0 , max_value = 15 , value = 0 , step = 1) 
YearsWithCurrManager = st.sidebar.slider("Please select input for the YearsWithCurrManager variable" , min_value = 0 , max_value = 17 , value = 0 , step = 1)
st.sidebar.markdown("0 - 12th, 1-Graduation, 2-Post Graduation, 3-PHD")
Higher_Education = st.sidebar.selectbox("Please select input for the Higher_Education variable" , options = [0,1,2,3] , index = 0)
Status_of_leaving = st.sidebar.selectbox("Please select input for the Status_of_leaving variable" , options = ["Dept.Head" , "Salary" , "Work Environment" , "Work Accident" , "Better Opportunity"] , index = 0)
Mode_of_work = st.sidebar.selectbox("Please select input for the Mode_of_work variable" , options = ["WFH" , "OFFICE"] , index = 0)
Leaves = st.sidebar.slider("Please select input for the Leaves variable" , min_value = 0 , max_value = 5 , value = 0 , step = 1)
Absenteeism	 = st.sidebar.slider("Please select input for Absenteeism variable" , min_value = 0 , max_value = 3 , value = 0 , step = 1)
Work_accident = st.sidebar.selectbox("Please select input for the Work_accident variable" , options = ["No" , "Yes"] , index = 0)
Source_of_Hire = st.sidebar.selectbox("Please select input for the Source_of_Hire variable" , options = ["Recruiter" , "Job Event" , "Walk-in" , "Job Portal"] , index = 0)
Job_mode = st.sidebar.selectbox("Please select input for the Job_mode variable" , options = ["FullTime" , "Contract" , "Part Time"] , index = 0)
Day = st.sidebar.slider("Please select input for the Day variable" , min_value = 1 , max_value = 31 , value = 1 , step = 1)
Month = st.sidebar.slider("Please select input for the Month variable" , min_value = 1 , max_value = 12 , value = 1 , step = 1)
Year = st.sidebar.slider("Please select input for the Year variable" , min_value = 2016 , max_value = 2022 , value = 2016 , step=1)

inputs = pd.DataFrame({"Age" : [Age], "BusinessTravel" : [BusinessTravel], "Department" : [Department] , "DistanceFromHome" : DistanceFromHome,
                      "Gender" : [Gender] , "JobInvolvement" : [JobInvolvement] , "JobLevel" : [JobLevel], "JobRole" : [JobRole],
                      "JobSatisfaction" : [JobSatisfaction] , "MaritalStatus" : [MaritalStatus] , "MonthlyIncome" : [MonthlyIncome],
                      "NumCompaniesWorked" : [NumCompaniesWorked] , "OverTime" : [OverTime] , "PercentSalaryHike" : [PercentSalaryHike],
                      "PerformanceRating" : [PerformanceRating] , "StockOptionLevel" : [StockOptionLevel],"TotalWorkingYears":                                     [TotalWorkingYears],"TrainingTimesLastYear" : [TrainingTimesLastYear] , "YearsAtCompany" : [YearsAtCompany] ,                               "YearsSinceLastPromotion" :[YearsSinceLastPromotion] , "YearsWithCurrManager" : [YearsWithCurrManager] ,                                     "Higher_Education" : [Higher_Education],"Status_of_leaving" : [Status_of_leaving] , "Mode_of_work" : [Mode_of_work] ,                        "Leaves" : [Leaves] , "Absenteeism" :[Absenteeism], "Work_accident" : [Work_accident] , "Source_of_Hire" :                                  [Source_of_Hire] , "Job_mode" : [Job_mode],
                      "Day" :[ Day] , "Month" :[Month] , "Year" : [Year]})
st.header("You have entered these inputs")
st.write(inputs)

btn = st.sidebar.button("Predict")

if btn : 
    model = pickle.load(open("Model" , "rb"))
    y_pred = model.predict(inputs)
    y_pred_prob = model.predict_proba(inputs)
    
    if y_pred == [1] : 
        st.markdown("This employee will **attrition** and probablity is {}".format(np.round(y_pred_prob[:,1][0])*100),2)
    else : 
        st.markdown("This employee won't **attrition** and probablity is {}".format(np.round(y_pred_prob[: , 0][0])*100),2)
    