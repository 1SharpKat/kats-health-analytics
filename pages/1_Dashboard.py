import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import warnings

warnings.filterwarnings(
    "ignore",
    category=FutureWarning
)

from datetime import timedelta

from modules.processor import process_data


# -----------------------------
# Color system
# -----------------------------
COLORS = {
    "blue": "#38BDF8",
    "indigo": "#6366F1",
    "pink": "#EC4899",
    "green": "#22C55E",
    "amber": "#F59E0B",
    "text": "#F8FAFC",
    "muted": "#CBD5E1"
}


# -----------------------------
# Helper function for chart styling
# -----------------------------
def clean_layout(fig):
    fig.update_layout(
        height=430,
        margin=dict(l=10, r=10, t=50, b=20),
        plot_bgcolor="rgba(15, 23, 42, 0.0)",
        paper_bgcolor="rgba(15, 23, 42, 0.0)",
        font=dict(color="#F8FAFC", size=13),
        hoverlabel=dict(
            bgcolor="#0F172A",
            font_color="#F8FAFC",
            bordercolor="#38BDF8"
        ),
        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            orientation="h",
            y=1.1
        )
    )

    fig.update_xaxes(
        showgrid=True,
        gridcolor="rgba(148, 163, 184, 0.16)",
        zeroline=False
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor="rgba(148, 163, 184, 0.16)",
        zeroline=False
    )

    return fig


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
# Metric card styling
# -----------------------------
st.markdown(
    """
    <style>


.stApp {
    background:
        radial-gradient(circle at top left, rgba(56,189,248,0.18), transparent 28%),
        radial-gradient(circle at top right, rgba(99,102,241,0.18), transparent 30%),
        linear-gradient(135deg, #020617, #0F172A 55%, #111827);
    color: #F8FAFC;
}

h1, h2, h3 {
    letter-spacing: -0.03em;
}

p {
    color: #CBD5E1;
}

.premium-card {
    padding: 1.5rem;
    border-radius: 28px;
    background: rgba(15, 23, 42, 0.86);
    border: 1px solid rgba(148, 163, 184, 0.18);
    backdrop-filter: blur(18px);
    box-shadow:
        0 18px 45px rgba(0,0,0,0.35),
        inset 0 1px 0 rgba(255,255,255,0.05);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.premium-card:hover {
    transform: translateY(-6px);
    box-shadow:
        0 24px 70px rgba(56,189,248,0.20),
        0 10px 35px rgba(0,0,0,0.45);
}

.hero-premium {
    padding: 3rem;
    border-radius: 34px;
    background:
        linear-gradient(135deg, rgba(56,189,248,0.95), rgba(99,102,241,0.95), rgba(236,72,153,0.85));
    box-shadow: 0 28px 80px rgba(56,189,248,0.25);
    margin-bottom: 2rem;
}

.hero-premium h1 {
    font-size: 4rem;
    margin-bottom: 0.5rem;
    color: white;
}

.hero-premium p {
    font-size: 1.25rem;
    color: #E0F2FE;
}

div[data-testid="metric-container"] {
    background: linear-gradient(135deg, rgba(56,189,248,0.95), rgba(99,102,241,0.95));
    padding: 20px;
    border-radius: 24px;
    box-shadow: 0 18px 45px rgba(56,189,248,0.22);
    border: 1px solid rgba(255,255,255,0.15);
}

div[data-testid="metric-container"] label,
div[data-testid="metric-container"] div {
    color: white !important;
}

section[data-testid="stSidebar"] {
    background: rgba(2, 6, 23, 0.96);
    border-right: 1px solid rgba(148, 163, 184, 0.15);
}    
    div[data-testid="metric-container"] {
        background: linear-gradient(135deg, #6366F1, #06B6D4);
        color: white;
        padding: 18px;
        border-radius: 18px;
        box-shadow: 0 10px 25px rgba(15, 23, 42, 0.18);
    }
    div[data-testid="metric-container"] label {
        color: white !important;
    }
    div[data-testid="metric-container"] div {
        color: white !important;
    }

    .card-glow {
    position: relative;
    overflow: hidden;
    padding: 1.5rem;
    border-radius: 24px;
    background: rgba(15, 23, 42, 0.88);
    border: 1px solid rgba(148, 163, 184, 0.12);
    backdrop-filter: blur(14px);

    transition:
        transform 0.3s ease,
        box-shadow 0.3s ease;
}

.card-glow::before {
    content: "";
    position: absolute;
    inset: -2px;
    border-radius: 24px;
    padding: 2px;

    background: linear-gradient(
        135deg,
        rgba(56, 189, 248, 0.9),
        rgba(99, 102, 241, 0.9),
        rgba(236, 72, 153, 0.9)
    );

    -webkit-mask:
        linear-gradient(#fff 0 0) content-box,
        linear-gradient(#fff 0 0);

    -webkit-mask-composite: xor;
    mask-composite: exclude;

    opacity: 0.65;
    transition: opacity 0.3s ease;
}

.card-glow:hover {
    transform: translateY(-8px) scale(1.01);

    box-shadow:
        0 0 20px rgba(56, 189, 248, 0.28),
        0 0 40px rgba(99, 102, 241, 0.22),
        0 0 60px rgba(236, 72, 153, 0.14);
}

.card-glow:hover::before {
    opacity: 1;
}

[data-testid="stPlotlyChart"] {
    transition:
        transform 0.28s ease,
        box-shadow 0.28s ease;
    border-radius: 24px;
    overflow: hidden;
}

[data-testid="stPlotlyChart"]:hover {
    transform: translateY(-4px);
}
    </style>
    """,
    unsafe_allow_html=True
)


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

