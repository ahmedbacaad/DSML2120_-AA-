
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="EDA Gallery | Ahmed Abdi",
    page_icon="📊",
    layout="wide"
)

# Load and cache the dataset
@st.cache_data
def load_data():
    data_path = (
        Path(__file__).resolve().parent.parent
        / "data" / "ds_salaries.csv"
    )
    df = pd.read_csv(data_path)
    df = df.drop(columns=["Unnamed: 0"], errors="ignore")
    return df

df = load_data()

# Labels for easier interpretation
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

remote_labels = {
    0: "On-site",
    50: "Hybrid",
    100: "Fully remote"
}

df["experience"] = df["experience_level"].map(
    experience_labels
)
df["company_group"] = df["company_size"].map(
    company_labels
)
df["work_arrangement"] = df["remote_ratio"].map(
    remote_labels
)

st.title("📊 Data Science Salary EDA Gallery")
st.write(
    "Exploring 607 data science salary records "
    "from 2020 to 2022."
)

st.markdown("""
This gallery investigates salary distributions,
experience levels, company sizes, and remote work.

All salary values are expressed in USD.
The charts are descriptive and do not establish causation.
""")

st.divider()

# Chart 1: Bar chart
st.header("1. Median Salary by Experience Level")

st.write(
    "**Question:** How does median salary differ "
    "across experience levels?"
)

experience_order = [
    "Entry-level", "Mid-level", "Senior", "Executive"
]

salary_by_experience = (
    df.groupby("experience", as_index=False)["salary_in_usd"]
    .median()
)

fig1 = px.bar(
    salary_by_experience,
    x="experience",
    y="salary_in_usd",
    color="experience",
    category_orders={"experience": experience_order},
    title="Median Annual Salary by Experience Level",
    labels={
        "experience": "Experience Level",
        "salary_in_usd": "Median Annual Salary (USD)"
    },
    color_discrete_sequence=px.colors.qualitative.Safe
)

fig1.update_yaxes(rangemode="tozero")
fig1.update_layout(showlegend=False)

st.plotly_chart(fig1, use_container_width=True)

st.subheader("How to read this chart")
st.markdown("""
- The horizontal axis shows experience levels.
- The vertical axis shows median annual salary in USD.
- Taller bars indicate higher median salaries.
""")

st.subheader("Observations")
highest_exp = salary_by_experience.loc[
    salary_by_experience["salary_in_usd"].idxmax()
]
lowest_exp = salary_by_experience.loc[
    salary_by_experience["salary_in_usd"].idxmin()
]

st.markdown(
    f"- **{highest_exp['experience']}** has the highest "
    f"median salary (${highest_exp['salary_in_usd']:,.0f}).\n"
    f"- **{lowest_exp['experience']}** has the lowest "
    f"median salary (${lowest_exp['salary_in_usd']:,.0f}).\n"
    "- These differences describe the dataset and "
    "do not prove that experience alone causes higher pay."
)

st.caption("Source: Data Science Job Salaries (2020–2022)")

st.divider()

# Chart 2: Histogram
st.header("2. Distribution of Data Science Salaries")

st.write(
    "**Question:** How are salaries distributed, "
    "and are there unusually high values?"
)

fig2 = px.histogram(
    df,
    x="salary_in_usd",
    nbins=40,
    title="Distribution of Annual Salaries",
    labels={
        "salary_in_usd": "Annual Salary (USD)",
        "count": "Number of Records"
    },
    color_discrete_sequence=["#4477AA"]
)

fig2.update_layout(
    xaxis_title="Annual Salary (USD)",
    yaxis_title="Number of Records",
    bargap=0.05
)

st.plotly_chart(fig2, use_container_width=True)

st.subheader("How to read this chart")
st.markdown("""
- The horizontal axis groups annual salaries into ranges.
- The vertical axis shows the number of records per range.
- Taller bars represent more common salary ranges.
""")

st.subheader("Observations")

median_salary = df["salary_in_usd"].median()
mean_salary = df["salary_in_usd"].mean()
max_salary = df["salary_in_usd"].max()

st.markdown(
    f"- The median salary is **${median_salary:,.0f}**.\n"
    f"- The mean salary is **${mean_salary:,.0f}**.\n"
    f"- The highest recorded salary is "
    f"**${max_salary:,.0f}**.\n"
    "- Compare the mean and median to understand "
    "whether high salaries influence the average."
)

st.caption("Source: Data Science Job Salaries (2020–2022)")

st.divider()

# Chart 3: Box plot
st.header("3. Salary Variation by Company Size")

st.write(
    "**Question:** How do salaries vary between "
    "small, medium, and large companies?"
)

fig3 = px.box(
    df,
    x="company_group",
    y="salary_in_usd",
    color="company_group",
    category_orders={
        "company_group": ["Small", "Medium", "Large"]
    },
    points="outliers",
    title="Annual Salary Distribution by Company Size",
    labels={
        "company_group": "Company Size",
        "salary_in_usd": "Annual Salary (USD)"
    },
    color_discrete_sequence=px.colors.qualitative.Safe
)

fig3.update_layout(showlegend=False)
st.plotly_chart(fig3, use_container_width=True)

st.subheader("How to read this chart")
st.markdown("""
- Each box represents a company-size category.
- The line inside each box represents the median salary.
- The box shows the middle 50% of salaries.
- Points beyond the whiskers represent potential outliers.
""")

st.subheader("Observations")

company_stats = (
    df.groupby("company_group")["salary_in_usd"]
    .median()
)

highest_company = company_stats.idxmax()
lowest_company = company_stats.idxmin()

st.markdown(
    f"- **{highest_company} companies** have the highest "
    f"median salary (${company_stats.max():,.0f}).\n"
    f"- **{lowest_company} companies** have the lowest "
    f"median salary (${company_stats.min():,.0f}).\n"
    "- The boxes and outlier points help reveal "
    "differences in salary variability.\n"
    "- Company size alone does not explain these differences."
)

st.caption("Source: Data Science Job Salaries (2020–2022)")

st.divider()

# Chart 4: Scatter plot
st.header("4. Remote Work and Salary")

st.write(
    "**Question:** How do salaries relate to remote "
    "work arrangements and experience levels?"
)

fig4 = px.scatter(
    df,
    x="remote_ratio",
    y="salary_in_usd",
    color="experience",
    hover_data=[
        "job_title",
        "work_year",
        "company_location"
    ],
    category_orders={"experience": experience_order},
    title="Remote Work Percentage vs Annual Salary",
    labels={
        "remote_ratio": "Remote Work Percentage (%)",
        "salary_in_usd": "Annual Salary (USD)",
        "experience": "Experience Level"
    },
    color_discrete_sequence=px.colors.qualitative.Safe,
    opacity=0.55
)

fig4.update_xaxes(
    tickvals=[0, 50, 100],
    ticktext=["On-site (0%)", "Hybrid (50%)", "Remote (100%)"]
)

st.plotly_chart(fig4, use_container_width=True)

st.subheader("How to read this chart")
st.markdown("""
- Each point represents one salary record.
- The horizontal axis shows remote-work percentage.
- The vertical axis shows annual salary in USD.
- Colors distinguish experience levels; hover for details.
""")

st.subheader("Observations")

remote_stats = (
    df.groupby("work_arrangement")["salary_in_usd"]
    .median()
)

for arrangement, value in remote_stats.items():
    st.markdown(
        f"- **{arrangement}:** median salary "
        f"${value:,.0f}."
    )

st.markdown(
    "- Many records overlap at the same remote-work "
    "percentage, so hover to inspect individual records.\n"
    "- Experience, location, and job title may also "
    "influence observed salary differences."
)

st.caption("Source: Data Science Job Salaries (2020–2022)")

st.divider()

# Ethics and limitations
st.header("Data Ethics and Limitations")

st.info("""
This dataset contains historical job salary records
from 2020–2022 and may not represent the entire
data science workforce. Salary comparisons can be
affected by geographic location, job title, and
sampling bias. These visualizations describe
patterns rather than prove causal relationships.
""")

st.markdown(
    "**Dataset source:** "
    "[Hugging Face — Data Science Job Salaries]"
    "(https://huggingface.co/datasets/"
    "hugginglearners/data-science-job-salaries)"
)
