
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.title("Interactive Pie Chart")

# Find the CSV file inside streamlit_DSML/data
csv_path = Path(__file__).resolve().parents[1] / "data" / "pie_demo.csv"

# Load the CSV data
df = pd.read_csv(csv_path)

st.write("This chart uses data loaded from a CSV file.")

# Show the data
st.subheader("Demo Data")
st.dataframe(df)

# Build the interactive pie chart
fig = px.pie(
    df,
    names="Category",
    values="Count",
    title="Distribution by Category",
    hole=0.3
)

st.plotly_chart(fig, use_container_width=True)
