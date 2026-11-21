
import streamlit as st

st.set_page_config(
    page_title="EDA Gallery | Ahmed Abdi",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Exploratory Data Analysis Gallery")
st.write("Exploring Data Science Job Salaries (2020–2022)")

st.markdown("""
This gallery explores how salaries differ across
experience levels, job titles, company sizes,
and remote-work arrangements.

Four visualizations will help us understand
patterns in the dataset.
""")

st.info("Next: Load the dataset and create four interactive charts.")
