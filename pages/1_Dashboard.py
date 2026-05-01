import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import warnings
from datetime import timedelta

from modules.processor import process_data
from styles.theme import load_theme
from utils.constants import COLORS
from utils.chart_helpers import clean_layout


warnings.filterwarnings("ignore", category=FutureWarning)

st.set_page_config(
    layout="wide",
    page_title="The Dashboard",
    initial_sidebar_state="expanded"
)

load_theme()


def hover_title(title):
    st.markdown(
        f"""
        <div class="title-card">
            <h3>{title}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )


@st.cache_data
def load_cached_data():
    return process_data()


st.markdown(
    """
    <style>
    header[data-testid="stHeader"] {
        background: transparent;
    }

    [data-testid="stToolbar"] {
        display: none;
    }

    section[data-testid="stSidebar"] {
        z-index: 999999;
    }

    .block-container {
        padding-top: 1rem;
        position: relative;
        z-index: 2;
    }

    [data-testid="stButton"] {
        position: relative;
        z-index: 999999;
        margin-bottom: 0.75rem;
    }

    [data-testid="stButton"] button {
        width: 100%;
        min-height: 52px;
        background: rgba(15, 23, 42, 0.78);
        color: white;
        border: 1px solid rgba(255,255,255,0.10);
        border-radius: 18px;
        backdrop-filter: blur(18px);
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.25s ease;
    }

    [data-testid="stButton"] button:hover {
        border: 1px solid rgba(99,102,241,0.35);
        transform: translateY(-2px);
    }

    [data-testid="stPlotlyChart"] {
        background: rgba(15, 23, 42, 0.82);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 24px;
        padding: 1rem;
        backdrop-filter: blur(18px);
        box-shadow:
            0 18px 40px rgba(0,0,0,0.35),
            inset 0 1px 1px rgba(255,255,255,0.05);
        margin-bottom: 1.5rem;
    }

    [data-testid="metric-container"] {
        background: rgba(15,23,42,0.72);
        border: 1px solid rgba(255,255,255,0.08);
        padding: 1rem;
        border-radius: 20px;
        backdrop-filter: blur(18px);
        box-shadow: 0 12px 30px rgba(0,0,0,0.25);
    }

    .slide-deck {
        position: fixed;
        inset: 0;
        z-index: 0;
        overflow: hidden;
        pointer-events: none;
    }

    .slide {
        position: absolute;
        inset: 0;
        background-size: cover;
        background-position: center;
        opacity: 0;
        animation: fadeSlide 24s infinite, slowZoom 24s infinite;
    }

    .slide:nth-child(1) {
        background-image: url("https://images.unsplash.com/photo-1517836357463-d25dfeac3438?q=80&w=2200&auto=format&fit=crop");
        animation-delay: 0s;
    }

    .slide:nth-child(2) {
        background-image: url("https://images.unsplash.com/photo-1518611012118-696072aa579a?q=80&w=2200&auto=format&fit=crop");
        animation-delay: 6s;
    }

    .slide:nth-child(3) {
        background-image: url("https://images.unsplash.com/photo-1490645935967-10de6ba17061?q=80&w=2200&auto=format&fit=crop");
        animation-delay: 12s;
    }

    .slide:nth-child(4) {
        background-image: url("https://images.unsplash.com/photo-1506126613408-eca07ce68773?q=80&w=2200&auto=format&fit=crop");
        animation-delay: 18s;
    }

    .slide-deck::after {
        content: "";
        position: absolute;
        inset: 0;
        background: linear-gradient(
            135deg,
            rgba(2,6,23,0.35),
            rgba(15,23,42,0.30),
            rgba(30,41,59,0.35)
        );
        z-index: 2;
    }

    @keyframes fadeSlide {
        0% { opacity: 0; }
        8% { opacity: 0.65; }
        22% { opacity: 0.65; }
        30% { opacity: 0; }
        100% { opacity: 0; }
    }

    @keyframes slowZoom {
        from { transform: scale(1); }
        to { transform: scale(1.08); }
    }

    h1, h2, h3 {
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="slide-deck">
        <div class="slide"></div>
        <div class="slide"></div>
        <div class="slide"></div>
        <div class="slide"></div>
    </div>
    """,
    unsafe_allow_html=True
)


hover_title("The Dashboard")

st.write(
    "Personal health analytics based on steps, sleep, heart rate, calories, "
    "and recovery score."
)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("Home", width="stretch"):
    st.switch_page("main.py")

if st.button("Trends & Insights", width="stretch"):
    st.switch_page("pages/2_Trends.py")

st.markdown("<br>", unsafe_allow_html=True)


with st.spinner("Loading and processing data..."):
    df = load_cached_data()

if df.empty:
    st.warning("No data available.")
    st.stop()


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


col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Average Steps", f"{filtered_df['Steps'].mean():,.0f}")

with col2:
    st.metric("Average Sleep Hours", f"{filtered_df['Sleep_Hours'].mean():.1f}")

with col3:
    st.metric("Average Recovery Score", f"{filtered_df['Recovery_Score'].mean():.1f}")

st.markdown("<br>", unsafe_allow_html=True)


left_col, right_col = st.columns(2)

with left_col:
    hover_title("Recovery Score & Sleep Trend")

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
        yaxis_title="Value",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(15,23,42,0.35)",
        font=dict(color="white")
    )

    st.plotly_chart(
        clean_layout(fig_recovery_sleep),
        width="stretch"
    )

with right_col:
    hover_title("Recovery Score vs Daily Steps")

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

    fig_steps.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(15,23,42,0.35)",
        font=dict(color="white")
    )

    st.plotly_chart(
        clean_layout(fig_steps),
        width="stretch"
    )

st.markdown("<br>", unsafe_allow_html=True)


left_col, right_col = st.columns(2)

with left_col:
    hover_title("Recovery Score vs Resting Heart Rate")

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

    fig_heart.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(15,23,42,0.35)",
        font=dict(color="white")
    )

    st.plotly_chart(
        clean_layout(fig_heart),
        width="stretch"
    )

with right_col:
    hover_title("Daily Calories Burned Trend")

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

    fig_calories.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(15,23,42,0.35)",
        font=dict(color="white")
    )

    st.plotly_chart(
        clean_layout(fig_calories),
        width="stretch"
    )