# System Capacity & Care Load Analytics for Unaccompanied Children


# IMPORT LIBRARIES
# =========================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# =========================
# PAGE CONFIGURATION
# =========================

st.set_page_config(
    page_title="UAC Healthcare Analytics Dashboard",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown(
    """
    <style>
    .main {
        background-color: #0e1117;
        color: white;
    }

    .stMetric {
        background-color: #1f2937;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #374151;
    }

    h1, h2, h3 {
        color: #f9fafb;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# LOAD DATA
# =========================

@st.cache_data

def load_data():

    df = pd.read_csv(
        "processed_uac_healthcare_analysis.csv"
    )

    df['Date'] = pd.to_datetime(df['Date'])

    return df


df = load_data()

# =========================
# SIDEBAR FILTERS
# =========================

st.sidebar.title("📌 Dashboard Filters")

# Date Range Filter

start_date = st.sidebar.date_input(
    "Start Date",
    df['Date'].min()
)

end_date = st.sidebar.date_input(
    "End Date",
    df['Date'].max()
)

# Metric Toggle

metric_option = st.sidebar.selectbox(
    "Select Metric",
    [
        'Total_System_Load',
        'CBP_Custody',
        'HHS_Care',
        'Net_Daily_Intake',
        'Load_Volatility'
    ]
)

# Time Granularity

time_granularity = st.sidebar.selectbox(
    "Time Granularity",
    ['Daily', 'Weekly', 'Monthly']
)

# Stress Threshold Slider

stress_threshold = st.sidebar.slider(
    "Stress Threshold Percentile",
    min_value=50,
    max_value=99,
    value=90
)

# =========================
# FILTER DATA
# =========================

filtered_df = df[
    (df['Date'] >= pd.to_datetime(start_date)) &
    (df['Date'] <= pd.to_datetime(end_date))
]

# =========================
# HEADER
# =========================

st.title("🏥 UAC Healthcare Capacity Analytics Dashboard")

st.markdown(
    """
    Monitoring system-wide healthcare load, operational stress,
    backlog accumulation, and care sustainability for the
    Unaccompanied Alien Children (UAC) Program.
    """
)

# ==========================================================
# KPI SECTION
# ==========================================================

st.markdown("---")

st.header("📊 System KPI Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Total Children Under Care",
        f"{filtered_df['Total_System_Load'].mean():,.0f}"
    )

with col2:

    st.metric(
        "Average Daily Intake",
        f"{filtered_df['Children apprehended and placed in CBP custody*'].mean():,.0f}"
    )

with col3:

    st.metric(
        "Average Daily Discharge",
        f"{filtered_df['HHS_Discharged'].mean():,.0f}"
    )

with col4:

    st.metric(
        "Net Intake Pressure",
        f"{filtered_df['Net_Daily_Intake'].mean():,.2f}"
    )

# ==========================================================
# MODULE 1 — SYSTEM LOAD OVERVIEW
# ==========================================================

st.markdown("---")

st.header("📈 Module 1 — System Load Overview")

# Total System Load Trend

fig = px.line(
    filtered_df,
    x='Date',
    y='Total_System_Load',
    title='Total System Load Over Time'
)

st.plotly_chart(fig, use_container_width=True)

# CBP vs HHS Comparison

comparison_df = filtered_df[
    ['Date', 'CBP_Custody', 'HHS_Care']
]

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=comparison_df['Date'],
        y=comparison_df['CBP_Custody'],
        mode='lines',
        name='CBP Custody'
    )
)

fig.add_trace(
    go.Scatter(
        x=comparison_df['Date'],
        y=comparison_df['HHS_Care'],
        mode='lines',
        name='HHS Care'
    )
)

fig.update_layout(
    title='CBP vs HHS Care Load Comparison'
)

st.plotly_chart(fig, use_container_width=True)

# Intake vs Discharge

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=filtered_df['Date'],
        y=filtered_df['Transferred_to_HHS'],
        mode='lines',
        name='Transferred to HHS'
    )
)

fig.add_trace(
    go.Scatter(
        x=filtered_df['Date'],
        y=filtered_df['HHS_Discharged'],
        mode='lines',
        name='Discharged from HHS'
    )
)

fig.update_layout(
    title='Daily Intake vs Discharge Trend'
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# MODULE 2 — CAPACITY STRESS ANALYSIS
# ==========================================================

st.markdown("---")

st.header("⚠️ Module 2 — Capacity Stress & Pressure Analysis")

# Rolling Average Analysis

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=filtered_df['Date'],
        y=filtered_df['Total_System_Load'],
        mode='lines',
        name='Daily Load'
    )
)

fig.add_trace(
    go.Scatter(
        x=filtered_df['Date'],
        y=filtered_df['7Day_Load_Avg'],
        mode='lines',
        name='7-Day Average'
    )
)

fig.add_trace(
    go.Scatter(
        x=filtered_df['Date'],
        y=filtered_df['14Day_Load_Avg'],
        mode='lines',
        name='14-Day Average'
    )
)

fig.update_layout(
    title='Rolling Average Healthcare Load Analysis'
)

st.plotly_chart(fig, use_container_width=True)

# Stress Threshold

threshold_value = (
    filtered_df['Total_System_Load']
    .quantile(stress_threshold / 100)
)

# Stress Detection

stress_df = filtered_df[
    filtered_df['Total_System_Load'] > threshold_value
]

st.subheader("🚨 High Stress Periods")

st.dataframe(
    stress_df[
        [
            'Date',
            'Total_System_Load',
            'Net_Daily_Intake',
            'Stress_Level'
        ]
    ]
)

# ==========================================================
# MODULE 3 — BACKLOG & SUSTAINABILITY
# ==========================================================

st.markdown("---")

st.header("📊 Module 3 — Backlog & Sustainability Analysis")

# Net Intake Trend

fig = px.line(
    filtered_df,
    x='Date',
    y='Net_Daily_Intake',
    title='Net Daily Intake Pressure'
)

st.plotly_chart(fig, use_container_width=True)

# Backlog Indicator

fig = px.line(
    filtered_df,
    x='Date',
    y='Backlog_Indicator',
    title='Backlog Accumulation Trend'
)

st.plotly_chart(fig, use_container_width=True)

# Discharge Offset Ratio

filtered_df['Discharge_Offset_Ratio'] = (
    filtered_df['HHS_Discharged']
    /
    filtered_df['Transferred_to_HHS']
)

fig = px.line(
    filtered_df,
    x='Date',
    y='Discharge_Offset_Ratio',
    title='Discharge Offset Ratio'
)

st.plotly_chart(fig, use_container_width=True)

# Sustainability Status

avg_net_intake = filtered_df['Net_Daily_Intake'].mean()

if avg_net_intake > 0:

    st.error(
        "⚠️ System experiencing sustained intake pressure and backlog accumulation."
    )

else:

    st.success(
        "✅ System currently operating within sustainable discharge capacity."
    )

# ==========================================================
# MODULE 4 — VOLATILITY & TEMPORAL ANALYTICS
# ==========================================================

st.markdown("---")

st.header("📈 Module 4 — Volatility & Temporal Analytics")

# Volatility Trend

fig = px.line(
    filtered_df,
    x='Date',
    y='Load_Volatility',
    title='Care Load Volatility Analysis'
)

st.plotly_chart(fig, use_container_width=True)

# Monthly Trend

monthly_load = (
    filtered_df.groupby('Month')['Total_System_Load']
    .mean()
    .reset_index()
)

monthly_load['Month'] = monthly_load['Month'].astype(str)

fig = px.bar(
    monthly_load,
    x='Month',
    y='Total_System_Load',
    title='Monthly Average System Load'
)

st.plotly_chart(fig, use_container_width=True)

# Correlation Heatmap

correlation_columns = [
    'Children apprehended and placed in CBP custody*',
    'CBP_Custody',
    'Transferred_to_HHS',
    'HHS_Care',
    'HHS_Discharged',
    'Total_System_Load'
]

corr = filtered_df[correlation_columns].corr()

fig = px.imshow(
    corr,
    text_auto=True,
    title='Healthcare Capacity Correlation Matrix'
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# POLICY INSIGHTS SECTION
# ==========================================================

st.markdown("---")

st.header("📌 Policy Intelligence Summary")

st.info(
    """
    The healthcare system experienced periods of sustained
    intake pressure, indicating potential operational strain
    on shelter capacity and healthcare staffing resources.

    Rolling average analysis revealed prolonged high-load
    windows requiring proactive capacity planning.
    """
)

# ==========================================================
# RECOMMENDATIONS SECTION
# ==========================================================

st.markdown("---")

st.header("📌 Strategic Recommendations")

st.success(
    """
    ✔ Increase staffing during prolonged high-load periods.

    ✔ Expand shelter and healthcare support capacity.

    ✔ Improve discharge efficiency to reduce backlog.

    ✔ Monitor rolling averages for early stress detection.

    ✔ Implement predictive forecasting models for surge planning.
    """
)

# ==========================================================
# FUTURE SCOPE
# ==========================================================

st.markdown("---")

st.header("🚀 Future Scope")

st.write(
    """
    Future enhancements may include:

    - Machine learning-based capacity forecasting
    - Real-time healthcare monitoring systems
    - Predictive backlog analysis
    - AI-driven operational alerts
    - Cloud deployment for live policy intelligence
    """
)

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.markdown(
    """
    ### Internship Project

    System Capacity & Care Load Analytics for Unaccompanied Children

    Developed using:
    - Python
    - Pandas
    - Plotly
    - Streamlit
    - Healthcare Time-Series Analytics
    """
)

