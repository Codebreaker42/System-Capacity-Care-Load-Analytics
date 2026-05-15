# 🏥 System Capacity & Care Load Analytics for Unaccompanied Children

## 📌 Project Overview

This project focuses on analyzing healthcare system capacity and operational care load within the **U.S. Department of Health and Human Services (HHS) Unaccompanied Alien Children (UAC) Program**.

The system monitors children moving through:
- CBP custody
- HHS care facilities
- Medical and welfare support
- Sponsor reunification and discharge

The project transforms raw operational healthcare data into actionable business intelligence using:
- Time-series analytics
- Healthcare KPI engineering
- Stress detection
- Backlog analysis
- Interactive Streamlit dashboards

---

# 🎯 Problem Statement

The UAC care pipeline experiences fluctuating operational pressure due to varying intake volumes and discharge rates.

Without centralized analytics, the organization faces challenges in:
- Monitoring healthcare system load
- Detecting operational stress periods
- Tracking backlog accumulation
- Evaluating sustainability of care delivery
- Supporting data-driven policy decisions

This project addresses these challenges through a real-time healthcare analytics framework.

---

# 🚀 Objectives

## Primary Objectives
- Quantify system-wide healthcare load
- Monitor intake versus discharge imbalance
- Detect capacity stress periods
- Analyze backlog accumulation trends

## Secondary Objectives
- Support staffing and shelter planning
- Improve operational visibility
- Enable data-driven humanitarian response evaluation

---

# 📂 Dataset Description

Each row in the dataset represents one day of healthcare system reporting.

| Column | Description |
|---|---|
| Date | Reporting date |
| CBP Intake | Daily intake volume |
| CBP Custody | Active CBP care load |
| Transferred to HHS | Flow into HHS care |
| HHS Care | Active HHS care load |
| HHS Discharged | Successful sponsor reunification |

---

# ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Plotly
- Streamlit
- Matplotlib
- Seaborn

---

# 📊 Key Features

## ✅ Healthcare KPI Engineering
- Total System Load
- Net Daily Intake
- Care Load Growth Rate
- Backlog Indicator
- Load Volatility

## ✅ Time-Series Analytics
- Daily trend analysis
- Weekly rolling averages
- Monthly load monitoring
- Volatility detection

## ✅ Capacity Stress Detection
- High-load window identification
- Operational pressure monitoring
- Sustained backlog detection

## ✅ Interactive Streamlit Dashboard
- KPI cards
- Dynamic filters
- Interactive Plotly charts
- Stress threshold controls
- Policy intelligence insights

---

# 🧠 Feature Engineering

## Total System Load

Measures total children currently under care.

```python
Total_System_Load = CBP_Custody + HHS_Care
```

## Net Daily Intake

Measures operational pressure.

```python
Net_Daily_Intake = Transfers_to_HHS - HHS_Discharged
```

## Care Load Growth Rate

Measures day-over-day healthcare load change.

## Backlog Indicator

Measures sustained unresolved care burden.

---

# 📈 Streamlit Dashboard Modules

## 📊 Module 1 — System Load Overview
- KPI cards
- System load trends
- CBP vs HHS comparison
- Intake vs discharge analysis

## ⚠️ Module 2 — Capacity Stress Dashboard
- 7-day rolling averages
- 14-day rolling averages
- High-stress period detection
- Operational pressure analysis

## 📌 Module 3 — Backlog & Sustainability Dashboard
- Net intake pressure
- Backlog accumulation trends
- Discharge efficiency analysis
- Sustainability indicators

## 📈 Module 4 — Volatility & Temporal Analytics
- Load volatility monitoring
- Monthly trend analysis
- Correlation matrix
- Temporal healthcare analytics

---

# 🎛️ Dashboard Filters

The dashboard includes:
- 📅 Date range selector
- 📊 Metric toggle
- 📆 Time granularity filter
- 🚨 Stress threshold controls

---

# 🔍 Key Insights

- System load fluctuates significantly over time.
- Certain periods show prolonged intake pressure.
- Sustained positive intake creates backlog accumulation.
- Rolling averages reveal operational stress windows.
- High volatility indicates unstable healthcare demand.

---

# 💡 Recommendations

- Increase staffing during surge periods
- Improve discharge efficiency
- Expand shelter and healthcare support capacity
- Monitor rolling averages for early stress detection
- Implement predictive forecasting systems

---

# 🚀 Future Scope

Future improvements may include:
- Machine learning-based forecasting
- Real-time healthcare monitoring
- AI-driven operational alerts
- Predictive backlog analysis
- Cloud deployment

---

# 🖥️ How to Run the Project

## 1️⃣ Clone Repository

```bash
git clone <repository_link>
```

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 3️⃣ Run Streamlit Application

```bash
streamlit run app.py
```

---

# 📁 Project Structure

```text
project/
│
├── app.py
├── processed_uac_healthcare_analysis.csv
├── requirements.txt
├── notebook.ipynb
└── README.md
```

---

# 📌 Internship Project Summary

Developed an industry-level healthcare analytics dashboard for monitoring operational load, intake pressure, backlog accumulation, and care system sustainability within the U.S. HHS Unaccompanied Children care pipeline using Python, Plotly, and Streamlit.

The project demonstrates:
- Healthcare analytics
- Time-series intelligence
- Business intelligence dashboards
- Operational monitoring
- Capacity planning
- Policy-oriented analytics

---

# 👨‍💻 Author

Nitin Budhlakoti

Internship Project — Unified Mentor