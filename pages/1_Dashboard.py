import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import warnings
from utils.constants import COLORS
from utils.chart_helpers import clean_layout


warnings.filterwarnings(
    "ignore",
    category=FutureWarning
)

from datetime import timedelta

from modules.processor import process_data

from styles.theme import load_theme

load_theme()




# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(layout="wide", page_title="FitSync Dashboard")

st.title("FitSync Dashboard")
st.write(
    "Personal health analytics based on steps, sleep, heart rate, calories, "
    "and recovery score."
)


# -----------------------------
# Load data
# -----------------------------
@st.cache_data
def load_cached_data():
    return process_data()


with st.spinner("Loading and processing data..."):
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
    "Steps",
    "Sleep_Hours",
    "Recovery_Score",
    "Heart_Rate_bpm",
    "Calories_Burned"
]

missing_columns = [col for col in required_columns if col not in filtered_df.columns]

if missing_columns:
    st.error(f"Missing required columns: {missing_columns}")
    st.stop()





# -----------------------------
# Key metrics
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Average Steps", f"{filtered_df['Steps'].mean():,.0f}")

with col2:
    st.metric("Average Sleep Hours", f"{filtered_df['Sleep_Hours'].mean():.1f}")

with col3:
    st.metric("Average Recovery Score", f"{filtered_df['Recovery_Score'].mean():.1f}")

st.markdown("---")


# -----------------------------
# First row of charts
# -----------------------------
left_col, right_col = st.columns(2)

with left_col:
    st.markdown('<div class="card-glow">', unsafe_allow_html=True)

    st.subheader("Recovery Score & Sleep Trend")

    fig_recovery_sleep = go.Figure()

    fig_recovery_sleep.add_trace(
        go.Scatter(
            x=filtered_df["Date"],
            y=filtered_df["Recovery_Score"],
            mode="lines+markers",
            name="Recovery Score",
            line=dict(color=COLORS["indigo"], width=3),
            marker=dict(size=6)
        )
    )

    fig_recovery_sleep.add_trace(
        go.Scatter(
            x=filtered_df["Date"],
            y=filtered_df["Sleep_Hours"],
            mode="lines+markers",
            name="Sleep Hours",
            line=dict(color=COLORS["blue"], width=3),
            marker=dict(size=6)
        )
    )

    fig_recovery_sleep.update_layout(
        xaxis_title="Date",
        yaxis_title="Value"
    )

    st.plotly_chart(
        clean_layout(fig_recovery_sleep),
        use_container_width=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

with right_col:
    st.markdown('<div class="card-glow">', unsafe_allow_html=True)

    st.subheader("Recovery Score vs Daily Steps")

    fig_steps = px.scatter(
        filtered_df,
        x="Steps",
        y="Recovery_Score",
        color="Sleep_Hours",
        color_continuous_scale=[
            COLORS["blue"],
            COLORS["indigo"]
        ],
        hover_data=["Date"],
        labels={
            "Steps": "Daily Steps",
            "Recovery_Score": "Recovery Score",
            "Sleep_Hours": "Sleep Hours"
        }
    )

    fig_steps.update_traces(
        marker=dict(size=9)
    )

    st.plotly_chart(
        clean_layout(fig_steps),
        use_container_width=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


st.markdown("<br>", unsafe_allow_html=True)


# -----------------------------
# Second row of charts
# -----------------------------
left_col, right_col = st.columns(2)

with left_col:
    st.markdown('<div class="card-glow">', unsafe_allow_html=True)

    st.subheader("Recovery Score vs Resting Heart Rate")

    fig_heart = px.scatter(
        filtered_df,
        x="Heart_Rate_bpm",
        y="Recovery_Score",
        hover_data=["Date"],
        color_discrete_sequence=[COLORS["green"]],
        labels={
            "Heart_Rate_bpm": "Resting Heart Rate",
            "Recovery_Score": "Recovery Score"
        }
    )

    fig_heart.update_traces(
        marker=dict(
            size=8,
            color=COLORS["green"]
        )
    )

    st.plotly_chart(
        clean_layout(fig_heart),
        use_container_width=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

with right_col:
    st.markdown('<div class="card-glow">', unsafe_allow_html=True)

    st.subheader("Daily Calories Burned Trend")

    fig_calories = px.line(
        filtered_df,
        x="Date",
        y="Calories_Burned",
        markers=True,
        labels={
            "Date": "Date",
            "Calories_Burned": "Calories Burned"
        }
    )

    fig_calories.update_traces(
        line=dict(
            color=COLORS["amber"],
            width=3
        ),
        marker=dict(size=6)
    )

    st.plotly_chart(
        clean_layout(fig_calories),
        use_container_width=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

