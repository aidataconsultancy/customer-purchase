import streamlit as st
import pandas as pd
#import altair as alt
import matplotlib.pyplot as plt
#import pandas_profiling
from streamlit_pandas_profiling import st_profile_report


st.set_option('deprecation.showPyplotGlobalUse', False)


def app():
    #Header
    st.write("Training data used")


    #Reading the data
    training_sample_subset=pd.read_csv("testing_sample.csv")

#display the data as a table
    st.write(training_sample_subset.head(30))


    #header
    st.write("Distribution of Orders (Dependent variable)")


    #bar plot
    temp=training_sample_subset["ordered"].value_counts()
    fig, ax = plt.subplots()
    ax.bar(["Not ordered","Ordered"],temp,color ='maroon',width = 0.4)
    plt.xlabel("Order status")
    plt.ylabel("No. of customers")
    st.pyplot()
    





# Profiling Report
    # st.write("Profiling Report")
    # pr = training_sample_subset.profile_report()
    # st_profile_report(pr)

################## ------- STYLING OF THE PAGE -------
#hiding Streamlit default styling
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)