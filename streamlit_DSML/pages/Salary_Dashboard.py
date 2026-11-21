
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
from datetime import datetime, timezone

st.set_page_config(
    page_title="Salary Dashboard | Ahmed Abdi",
    page_icon="📈",
    layout="wide"
)

@st.cache_data
def load_data():
    path = (
        Path(__file__).resolve().parent.parent
        / "data" / "ds_salaries.csv"
    )
    df = pd.read_csv(path)
    df = df.drop(columns=["Unnamed: 0"], errors="ignore")
    return df

df = load_data()

experience_labels = {
    "EN": "Entry-level",
    "MI": "Mid-level",
    "SE": "Senior",
    "EX": "Executive"
}

company_labels = {
    "S": "Small",
    "M": "Medium",
    "L": "Large"
}

df["experience"] = df["experience_level"].map(
    experience_labels
)
df["company_group"] = df["company_size"].map(
    company_labels
)

st.title("📈 Data Science Salary Dashboard")
st.markdown(
    "Explore salary patterns across experience levels, "
    "company sizes, and years from **2020–2022**."
)

st.caption(
    "Dataset: Data Science Job Salaries | "
    f"{len(df):,} records | All salaries in USD"
)

st.divider()

# Interactive filters
st.sidebar.header("Salary Dashboard Filters")

years = sorted(df["work_year"].unique().tolist())

selected_years = st.sidebar.multiselect(
    "Select year(s)",
    options=years,
    default=years
)

experience_order = [
    "Entry-level", "Mid-level", "Senior", "Executive"
]

selected_experience = st.sidebar.multiselect(
    "Experience level",
    options=experience_order,
    default=experience_order
)

company_order = ["Small", "Medium", "Large"]

selected_company = st.sidebar.multiselect(
    "Company size",
    options=company_order,
    default=company_order
)

# Apply all filters to one shared dataframe
filtered = df[
    df["work_year"].isin(selected_years)
    & df["experience"].isin(selected_experience)
    & df["company_group"].isin(selected_company)
].copy()

if filtered.empty:
    st.warning(
        "No records match your filters. "
        "Please select more options."
    )
    st.stop()

# Dynamic KPIs
st.subheader("Key Performance Indicators")

k1, k2, k3, k4 = st.columns(4)

k1.metric(
    "Job Records",
    f"{len(filtered):,}"
)

k2.metric(
    "Average Salary",
    f"${filtered['salary_in_usd'].mean():,.0f}"
)

k3.metric(
    "Median Salary",
    f"${filtered['salary_in_usd'].median():,.0f}"
)

k4.metric(
    "Highest Salary",
    f"${filtered['salary_in_usd'].max():,.0f}"
)

st.divider()

# Linked visualization 1
st.subheader("Median Salary by Experience Level")

salary_exp = (
    filtered.groupby(
        "experience", as_index=False
    )["salary_in_usd"]
    .median()
)

fig1 = px.bar(
    salary_exp,
    x="experience",
    y="salary_in_usd",
    color="experience",
    category_orders={
        "experience": experience_order
    },
    labels={
        "experience": "Experience Level",
        "salary_in_usd": "Median Annual Salary (USD)"
    },
    title="Median Salary Across Experience Levels",
    color_discrete_sequence=px.colors.qualitative.Safe
)

fig1.update_yaxes(rangemode="tozero")
fig1.update_layout(showlegend=False)

st.plotly_chart(fig1, use_container_width=True)

st.caption(
    "Bars represent median salaries for the "
    "currently selected records."
)

# Linked visualization 2
st.subheader("Salary Distribution by Company Size")

fig2 = px.box(
    filtered,
    x="company_group",
    y="salary_in_usd",
    color="company_group",
    category_orders={
        "company_group": company_order
    },
    points="outliers",
    labels={
        "company_group": "Company Size",
        "salary_in_usd": "Annual Salary (USD)"
    },
    title="Salary Variation Across Company Sizes",
    color_discrete_sequence=px.colors.qualitative.Safe
)

fig2.update_layout(showlegend=False)

st.plotly_chart(fig2, use_container_width=True)

st.caption(
    "Boxes show median salaries, middle 50% ranges, "
    "and potential outliers for filtered records."
)

st.divider()

# Dynamic insights
st.subheader("Insights and Observations")

median_salary = filtered["salary_in_usd"].median()
average_salary = filtered["salary_in_usd"].mean()

highest_group = salary_exp.loc[
    salary_exp["salary_in_usd"].idxmax()
]

company_medians = (
    filtered.groupby("company_group")["salary_in_usd"]
    .median()
)

top_company = company_medians.idxmax()

st.markdown(
    f"""
- **Sample size:** {len(filtered):,} records match
  the current filters, out of {len(df):,} total.
- **Salary comparison:** The median annual salary
  is ${median_salary:,.0f}, compared with a mean
  of ${average_salary:,.0f}.
- **Experience:** {highest_group['experience']}
  has the highest median salary among the
  selected experience groups
  (${highest_group['salary_in_usd']:,.0f}).
- **Company size:** {top_company} companies have
  the highest median salary among the selected
  company-size groups
  (${company_medians.max():,.0f}).
- **Limitations:** These are historical,
  observational salary records. Differences
  may reflect job roles, locations, experience,
  or sampling effects rather than direct causes.
"""
)

st.divider()

# Ethics and reproducibility
st.subheader("Data Source and Ethics")

st.info(
    "This dataset contains historical job salary "
    "records and may not represent all data science "
    "workers or companies. Geographic and sampling "
    "biases can affect comparisons. Results should "
    "not be used to judge individual workers or "
    "predict current salaries."
)

st.markdown(
    "**Source:** [Data Science Job Salaries]"
    "(https://huggingface.co/datasets/"
    "hugginglearners/data-science-job-salaries)"
)

st.caption(
    "Data period: 2020–2022 | "
    "Source: Historical CSV | "
    "Last app refresh (UTC): "
    + datetime.now(timezone.utc).strftime(
        "%Y-%m-%d %H:%M"
    )
)
