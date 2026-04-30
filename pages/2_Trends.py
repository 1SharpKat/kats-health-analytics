import streamlit as st
import plotly.express as px
import warnings
from datetime import timedelta

from modules.processor import process_data


warnings.filterwarnings("ignore", category=FutureWarning)


# -----------------------------
# Premium color system
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
# Chart styling helper
# -----------------------------
def clean_layout(fig):
    fig.update_layout(
        height=430,
        margin=dict(l=10, r=10, t=50, b=20),
        plot_bgcolor="rgba(15, 23, 42, 0)",
        paper_bgcolor="rgba(15, 23, 42, 0)",
        font=dict(color=COLORS["text"], size=13),
        hoverlabel=dict(
            bgcolor="#0F172A",
            font_color=COLORS["text"],
            bordercolor=COLORS["blue"]
        ),
        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            orientation="h",
            y=1.1
        )
    )

    fig.update_xaxes(
        showgrid=True,
        gridcolor="rgba(148, 163, 184, 0.15)",
        zeroline=False
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor="rgba(148, 163, 184, 0.15)",
        zeroline=False
    )

    return fig


# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(layout="wide", page_title="Trends & Insights")


# -----------------------------
# Premium styling
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

    section[data-testid="stSidebar"] {
        background: rgba(2, 6, 23, 0.96);
        border-right: 1px solid rgba(148, 163, 184, 0.15);
    }

    .trend-hero {
        padding: 3rem;
        border-radius: 34px;
        background:
            linear-gradient(135deg, rgba(56,189,248,0.95), rgba(99,102,241,0.95), rgba(236,72,153,0.85));
        box-shadow: 0 28px 80px rgba(56,189,248,0.25);
        margin-bottom: 2rem;
        animation: fadeInUp 0.8s ease;
    }

    .trend-hero h1 {
        font-size: 4rem;
        margin-bottom: 0.5rem;
        color: white;
    }

    .trend-hero p {
        font-size: 1.25rem;
        color: #E0F2FE;
        margin: 0;
    }

    div[data-testid="metric-container"] {
        background: linear-gradient(135deg, rgba(56,189,248,0.95), rgba(99,102,241,0.95));
        padding: 20px;
        border-radius: 24px;
        box-shadow: 0 18px 45px rgba(56,189,248,0.22);
        border: 1px solid rgba(255,255,255,0.15);
        transition: transform 0.25s ease, box-shadow 0.25s ease;
    }

    div[data-testid="metric-container"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 24px 70px rgba(56,189,248,0.28);
    }

    div[data-testid="metric-container"] label,
    div[data-testid="metric-container"] div {
        color: white !important;
    }

    .card-glow {
        position: relative;
        overflow: hidden;
        padding: 1.5rem;
        border-radius: 28px;
        background: rgba(15, 23, 42, 0.88);
        border: 1px solid rgba(148, 163, 184, 0.15);
        backdrop-filter: blur(16px);
        box-shadow:
            0 18px 45px rgba(0,0,0,0.35),
            inset 0 1px 0 rgba(255,255,255,0.05);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .card-glow::before {
        content: "";
        position: absolute;
        inset: -2px;
        border-radius: 28px;
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
        opacity: 0.55;
        transition: opacity 0.3s ease;
        pointer-events: none;
    }

    .card-glow:hover {
        transform: translateY(-6px);
        box-shadow:
            0 24px 70px rgba(56,189,248,0.20),
            0 10px 35px rgba(0,0,0,0.45);
    }

    .card-glow:hover::before {
        opacity: 1;
    }

    .summary-table {
        width: 100%;
        border-collapse: collapse;
        background: rgba(15, 23, 42, 0.95);
        border-radius: 16px;
        overflow: hidden;
        color: #F8FAFC;
    }

    .summary-table th {
        background: rgba(30, 41, 59, 0.95);
        color: #38BDF8;
        padding: 14px;
        text-align: center;
    }

    .summary-table td {
        padding: 14px;
        text-align: center;
        border-top: 1px solid rgba(148, 163, 184, 0.2);
    }

    [data-testid="stPlotlyChart"] {
        transition: transform 0.28s ease;
        border-radius: 24px;
        overflow: hidden;
    }

    [data-testid="stPlotlyChart"]:hover {
        transform: translateY(-4px);
    }

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(18px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)


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
    df = process_data()

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