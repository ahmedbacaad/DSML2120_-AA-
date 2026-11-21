
import streamlit as st

st.set_page_config(
    page_title="Future Work | Ahmed Abdi",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Future Work & Reflection")

st.write("""
This portfolio demonstrates exploratory data analysis
and interactive dashboard development using Python,
Pandas, Plotly, and Streamlit.

The following improvements would expand its usefulness
and strengthen the quality of the analysis.
""")

st.divider()

st.header("1. Future Improvements")

st.subheader("1. Add More Recent Salary Data")
st.write("""
Expand the dataset beyond 2022 to investigate
more recent salary trends and compare how
compensation changes over time.
""")

st.subheader("2. Develop Salary Prediction Models")
st.write("""
Experiment with regression models to estimate
salaries using experience level, job title,
company size, and location. Evaluate predictions
using MAE and RMSE on held-out data.
""")

st.subheader("3. Add Geographic Visualizations")
st.write("""
Create an interactive map showing salary
differences by country. Include sample sizes
to help viewers interpret regional comparisons.
""")

st.subheader("4. Improve Dashboard Accessibility")
st.write("""
Evaluate color contrast, chart readability,
keyboard navigation, and mobile layouts.
Provide clearer descriptions for users
with different accessibility needs.
""")

st.subheader("5. Add Advanced Filters")
st.write("""
Introduce job-title, country, and remote-work
filters to allow more detailed comparisons
between salary groups.
""")

st.divider()

st.header("2. Prototype to Final Application")

st.markdown("""
The final application extends the initial
visualization design through:

- **Improved navigation:** Multiple pages separate
  the professional portfolio from the analysis.
- **Interactive exploration:** Plotly charts allow
  users to inspect salary records through hover details.
- **Linked dashboard filters:** Year, experience,
  and company-size selections update the KPIs and charts.
- **Data storytelling:** Chart explanations and
  observations help users interpret results.
""")

st.caption(
    "Review this reflection against your actual "
    "Lab 4.3 paper prototype before submitting."
)

st.divider()

st.header("3. Final Reflection")

st.write("""
This project helped me connect exploratory data
analysis with interactive dashboard development.
I learned how to select appropriate visualizations,
communicate findings clearly, and build reusable
Python components.

In future projects, I want to incorporate
machine learning, stronger accessibility practices,
and more detailed data validation.
""")
