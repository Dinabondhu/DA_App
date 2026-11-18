import streamlit as st
import pandas as pd
import seaborn as sns

st.title("Data Analisys")
st.subheader("Data Analisys using Python and Streamlit")

file = st.file_uploader("Upload Your Dataset (In CSV Format)")
if file is not None:
    data = pd.read_csv(file)
    
if file is not None:    
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())


    if st.checkbox("Datatype of Each Column"):
        st.text("Datatypes")
        st.write(data.dtypes)


    data_shape = st.radio("What dimension do you want to check?", ("Rows", "Columns"))
    
    if data_shape == "Rows":
        st.text("Number of Rows:")
        st.write(data.shape[0])
        
    if data_shape == "Columns":
        st.text("Number of Columns:")
        st.write(data.shape[1])
        

    test = data.isnull().values.any()
    if test:
        if st.checkbox("Null Values in the Dataset"):
            sns.heatmap(data.isnull())
            st.pyplot()
    else:
        st.success("No Missing Values!!!")

    test = data.duplicated().any()
    if test:
        st.warning("This dataset contains some duplicate values")
        dup = st.selectbox("Do you want to remove the duplicate values?", 
                           ("Select one", "Yes", "No"))
        if dup == "Yes":
            data = data.drop_duplicates()
            st.text("Duplicate values are removed successfully!")
        if dup == "No":
            st.text("OK! Continuing with duplicate values!")

    if st.checkbox("Summary of the Dataset"):
        st.write(data.describe(include="all"))

if st.button("About"):
    st.text("Created with streamlit")
    st.text("Thanks to streamlit")
    
if st.checkbox("By:"):
    st.success("Dinabondhu Ghosh")