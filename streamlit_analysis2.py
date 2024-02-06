# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 08:36:28 2024

@author: SLEEMTEECH
"""

import streamlit as st
import pandas as pd
import seaborn as sns

# title and subheader
st.title("Data Analysis")
st.subheader("Data Analysis Using Python and Streamlit")

# upload Dataset

upload = st.file_uploader("upload your Dataset (in csv format)")
if upload is not None:
    data=pd.read_csv(upload)
    
# show dataset
if upload is not None:   
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("tail"):
            st.write(data.tail())

# Check Datatype of each columns
if upload is not None:
    if st.checkbox("Datatypenof each column"):
        st.text("DataTypes")
        st.write(data.dtypes)
        
# find the shape of our Dataset(Number of rows and number of columns)
if upload is not None:
    data_shape=st.radio("what dimension do you want to check?",('Rows','Columns'))
    if data_shape=='Rows':
        st.text("Number of Rows")
        st.write(data.shape[0])
    if data_shape=='Columns':
        st.text("Number of Columns")
        st.write(data.shape[1])
        
# Find Null Values in the Dataset
if upload is not None:
    test=data.isnull().values.any()
    if test==True:
        if st.checkbox("Null Values in the dataset"):
            sns.heatmap(data.isnull())
            st.pyplot()
    else:
        st.success("Congratulations!!!, no Missing Values")
    
# find the duplicate Values in the Dataset
if upload is not None:
    test=data.duplicated().any()
    if test==True:
        st.warning("This Dataset Contain Some Duplicate Values")
        dup=st.selectbox("Do you want to remove Duplicate Values?",\
                         ("Select One", "Yes", "No"))
        if dup=="Yes":
            data=data.drop_duplicates()
            st.text("Duplicated Values are removed")
        if dup=="No":
            st.text("Ok No problem")
            
# Get overall Statistics of our dataset
if upload is not None:
    if st.checkbox("Summary of the dataset"):
        st.write(data.describe(include='all'))
        
# about section

if st.button("About App"):
    st.text("Built with Streamlit")
    st.text("Thanks to Streamlit")
    
# By
if st.checkbox("By"):
    st.success("Owolabi Ayomide")
        
        
        
        

