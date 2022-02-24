import math
import streamlit as st
import numpy as np
import time 
import pandas as pd 
import csv as csv 


st.title("SYSEN 5160 HW 2")

st.subheader("Analytical Hierarchy Process")

st.text("Enter the Matrix with the Attributes Ranked")

att_file = st.file_uploader("Attributes Pairwise Comparison CSV File") 

att_array = csv.reader(att_file)

st.table(att_array)


st.text("Pairwise Comparisons of Options Added Here")

opt = st.file_uploader("Options Pairwise Comparison") 