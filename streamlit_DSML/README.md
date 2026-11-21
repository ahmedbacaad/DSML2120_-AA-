# Data Science & Machine Learning Portfolio

**Ahmed Abdi | Metropolitan State University of Denver**

An interactive Streamlit portfolio showcasing my work in data science, machine learning, exploratory data analysis, and dashboard development.

This project was developed for **DSML 2120 — Data Visualization**. It combines a professional portfolio with an interactive analysis of data science job salaries from 2020–2022.

## Project Overview

This application demonstrates my ability to clean and analyze datasets, create interactive visualizations, and communicate data-driven insights.

The main analytics project explores how data science salaries vary by experience level, company size, and remote-work arrangements using 607 historical salary records.

**Technologies:** Python, Pandas, Plotly, Streamlit, Git, and GitHub.

## Application Pages

### 1. Professional Bio
Introduces my educational background, technical skills, professional interests, and visualization philosophy.

### 2. Visualization
Demonstrates data visualization techniques and concepts from coursework.

### 3. Pie Chart
Presents a visualization of personal interests using a pie chart.

### 4. Cryptocurrency
Displays cryptocurrency information using an external API.

### 5. Weather
Provides a weather dashboard for Denver.

### 6. EDA Gallery
Explores the Data Science Job Salaries dataset using four visualization types:

- **Bar chart:** Median salary by experience level.
- **Histogram:** Distribution of annual salaries.
- **Box plot:** Salary variation across company sizes.
- **Scatter plot:** Remote-work percentage compared with salary.

Each chart includes an explanation of how to interpret it, observations, and source information.

### 7. Salary Dashboard
An interactive dashboard featuring:

- Filters for year, experience level, and company size.
- Four dynamic KPIs: record count, average salary, median salary, and maximum salary.
- Two linked visualizations that respond to filters.
- Automatically generated observations and data limitations.

### 8. Future Work
Discusses possible improvements, including more recent data, salary prediction models, geographic analysis, accessibility improvements, and advanced filters.

## Dataset Information

**Dataset:** Data Science Job Salaries

**Source:** https://huggingface.co/datasets/hugginglearners/data-science-job-salaries

**Number of records:** 607

**Number of original columns:** 12

**Years covered:** 2020–2022

The dataset includes job titles, salaries, experience levels, employment types, company locations, company sizes, and remote-work percentages.

### Data Preprocessing

The application uses Pandas to:

1. Load the CSV file.
2. Remove the unnecessary `Unnamed: 0` index column.
3. Convert experience-level codes into readable labels.
4. Convert company-size codes into readable categories.
5. Convert remote-work percentages into descriptive categories.
6. Use `salary_in_usd` for consistent salary comparisons.
7. Calculate summary statistics for charts and dashboard KPIs.

The original dataset is preserved in the `data` directory.

### Ethics and Limitations

The dataset contains historical job salary records and may not represent the entire data science workforce. Salary differences can reflect geographic location, job title, experience, and sampling bias. Visualizations are descriptive and should not be interpreted as proof of causation or as predictions of current compensation.

## Project Structure

```text
streamlit_DSML/
├── app.py
├── assets/
│   └── Ahmed.JPG
├── data/
│   ├── ds_salaries.csv
│   └── pie_demo.csv
├── pages/
│   ├── 1_Bio.py
│   ├── 2_Visualization.py
│   ├── 3_Pie.py
│   ├── 4_Crypto.py
│   ├── 5_Weather.py
│   ├── EDA_Gallery.py
│   ├── Salary_Dashboard.py
│   └── 7_Future_Work.py
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/ahmedbacaad/DSML2120_-AA-.git
cd DSML2120_-AA-/streamlit_DSML
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Run the application

```bash
streamlit run app.py
```

The application will open locally in your browser, usually at `http://localhost:8501`.

## Requirements

Python packages are listed in `requirements.txt`, including Streamlit, Pandas, Plotly, and dependencies used by the existing application pages.

## Deployment

The application is hosted using Streamlit Community Cloud and connected to the GitHub repository.

**GitHub Repository:** https://github.com/ahmedbacaad/DSML2120_-AA-

**Live Streamlit Application:** Add your deployed Streamlit app URL here.

## Future Improvements

- Incorporate more recent salary datasets.
- Develop machine learning models for salary prediction.
- Add interactive geographic salary comparisons.
- Improve accessibility and mobile responsiveness.
- Introduce additional filters for job titles and locations.

## AI Assistance Acknowledgment

ChatGPT was used to assist with project planning, Python code development, documentation, and refinement of data visualization explanations. The application was deployed and tested using Streamlit Community Cloud.

## Author

**Ahmed Abdi**

Data Science & Machine Learning Student

Metropolitan State University of Denver

**GitHub:** https://github.com/ahmedbacaad
