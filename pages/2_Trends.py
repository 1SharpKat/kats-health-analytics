import streamlit as st
import plotly.express as px
import warnings
from datetime import timedelta

from utils.constants import COLORS
from utils.chart_helpers import clean_layout

from modules.processor import process_data

from styles.theme import load_theme

st.set_page_config(layout="wide", page_title="Trends & Insights")

load_theme()
@st.cache_data
def load_cached_data():
    return process_data()


warnings.filterwarnings("ignore", category=FutureWarning)



# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(layout="wide", page_title="Trends & Insights")


# -----------------------------
# Premium styling
# -----------------------------



# -----------------------------
# Hero
# -----------------------------
st.markdown(
    """
    <div class="trend-hero">
        <h1>📈 Trends & Insights</h1>
        <p>Premium trend analysis across recovery, sleep, movement, and energy.</p>
    </div>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Load data
# -----------------------------
with st.spinner("Analyzing trends..."):
    df = load_cached_data()

if df.empty:
    st.warning("No data available.")
    st.stop()


# -----------------------------
# Sidebar filter
# -----------------------------
st.sidebar.header("Filters")

time_range = st.sidebar.selectbox(
    "Select Time Range",
    ["Last 7 Days", "Last 30 Days", "All Time"]
)

max_date = df["Date"].max()

if time_range == "Last 7 Days":
    cutoff_date = max_date - timedelta(days=7)
    filtered_df = df[df["Date"] >= cutoff_date].copy()
elif time_range == "Last 30 Days":
    cutoff_date = max_date - timedelta(days=30)
    filtered_df = df[df["Date"] >= cutoff_date].copy()
else:
    filtered_df = df.copy()

if filtered_df.empty:
    st.warning("No data matches this filter.")
    st.stop()


# -----------------------------
# Required column check
# -----------------------------
required_columns = [
    "Date",
    "Recovery_Score",
    "Sleep_Hours",
    "Steps",
    "Calories_Burned"
]

missing_columns = [col for col in required_columns if col not in filtered_df.columns]

if missing_columns:
    st.error(f"Missing required columns: {missing_columns}")
    st.stop()


# -----------------------------
# Quick metric highlights
# -----------------------------
metric1, metric2, metric3, metric4 = st.columns(4)

with metric1:
    st.metric("Avg Recovery", f"{filtered_df['Recovery_Score'].mean():.1f}")

with metric2:
    st.metric("Avg Sleep", f"{filtered_df['Sleep_Hours'].mean():.1f} hrs")

with metric3:
    st.metric("Avg Steps", f"{filtered_df['Steps'].mean():,.0f}")

with metric4:
    st.metric("Avg Calories", f"{filtered_df['Calories_Burned'].mean():,.0f}")

st.markdown("<br>", unsafe_allow_html=True)


# -----------------------------
# Summary stats
# -----------------------------
st.markdown('<div class="card-glow">', unsafe_allow_html=True)

st.subheader(" Summary Statistics")

summary = filtered_df[
    ["Recovery_Score", "Sleep_Hours", "Steps", "Calories_Burned"]
].agg(["mean", "min", "max"]).round(2)

st.markdown(
    summary.to_html(classes="summary-table", border=0),
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)


# -----------------------------
# Monthly Recovery Trend
# -----------------------------
st.markdown('<div class="card-glow">', unsafe_allow_html=True)

st.subheader(" Average Recovery Score by Month")

monthly = filtered_df.copy()
monthly["Month"] = monthly["Date"].dt.to_period("M").astype(str)

monthly = monthly.groupby("Month", as_index=False)["Recovery_Score"].mean()

fig_month = px.line(
    monthly,
    x="Month",
    y="Recovery_Score",
    markers=True,
    labels={
        "Month": "Month",
        "Recovery_Score": "Average Recovery Score"
    }
)

fig_month.update_traces(
    line=dict(color=COLORS["indigo"], width=4),
    marker=dict(
        size=9,
        color=COLORS["pink"],
        line=dict(width=2, color="white")
    ),
    hovertemplate="<b>Month:</b> %{x}<br><b>Avg Recovery:</b> %{y:.1f}<extra></extra>"
)

st.plotly_chart(
    clean_layout(fig_month),
    use_container_width=True
)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)


# -----------------------------
# Histograms
# -----------------------------
st.markdown('<div class="card-glow">', unsafe_allow_html=True)

st.subheader(" Metric Distributions")

col1, col2 = st.columns(2)

with col1:
    fig_steps = px.histogram(
        filtered_df,
        x="Steps",
        nbins=25,
       
        color_discrete_sequence=[COLORS["green"]]
    )

    fig_steps.update_traces(
        marker_line_color="rgba(255,255,255,0.85)",
        marker_line_width=1.4,
        opacity=0.9,
        hovertemplate="<b>Steps:</b> %{x}<br><b>Count:</b> %{y}<extra></extra>"
    )

    st.plotly_chart(
        clean_layout(fig_steps),
        use_container_width=True
    )

with col2:
    fig_calories = px.histogram(
        filtered_df,
        x="Calories_Burned",
        nbins=25,
        
        color_discrete_sequence=[COLORS["amber"]]
    )

    fig_calories.update_traces(
        marker_line_color="rgba(255,255,255,0.85)",
        marker_line_width=1.4,
        opacity=0.9,
        hovertemplate="<b>Calories:</b> %{x}<br><b>Count:</b> %{y}<extra></extra>"
    )

    st.plotly_chart(
        clean_layout(fig_calories),
        use_container_width=True
    )

col3, col4 = st.columns(2)

with col3:
    fig_recovery = px.histogram(
        filtered_df,
        x="Recovery_Score",
        nbins=25,
       
        color_discrete_sequence=[COLORS["indigo"]]
    )

    fig_recovery.update_traces(
        marker_line_color="rgba(255,255,255,0.85)",
        marker_line_width=1.4,
        opacity=0.9,
        hovertemplate="<b>Recovery Score:</b> %{x}<br><b>Count:</b> %{y}<extra></extra>"
    )

    st.plotly_chart(
        clean_layout(fig_recovery),
        use_container_width=True
    )

with col4:
    fig_sleep = px.histogram(
        filtered_df,
        x="Sleep_Hours",
        nbins=25,
        
        color_discrete_sequence=[COLORS["pink"]]
    )

    fig_sleep.update_traces(
        marker_line_color="rgba(255,255,255,0.85)",
        marker_line_width=1.4,
        opacity=0.9,
        hovertemplate="<b>Sleep Hours:</b> %{x}<br><b>Count:</b> %{y}<extra></extra>"
    )

    st.plotly_chart(
        clean_layout(fig_sleep),
        use_container_width=True
    )

st.markdown("</div>", unsafe_allow_html=True)