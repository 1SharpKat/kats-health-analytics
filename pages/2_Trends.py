import streamlit as st
import plotly.express as px
import warnings
from datetime import timedelta

from modules.processor import process_data
from styles.theme import load_theme
from utils.constants import COLORS
from utils.chart_helpers import clean_layout


# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(layout="wide", page_title="Trends & Insights")
load_theme()
warnings.filterwarnings("ignore", category=FutureWarning)


# -----------------------------
# Page styling
# -----------------------------
st.markdown(
    """
    <style>
    header[data-testid="stHeader"] {
        display: none;
    }

    [data-testid="stToolbar"] {
        display: none;
    }

    .block-container {
        padding-top: 1rem;
        position: relative;
        z-index: 2;
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
            rgba(2,6,23,0.62),
            rgba(15,23,42,0.58),
            rgba(30,41,59,0.64)
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

    h1, h2, h3 {
        color: white !important;
    }

    .ai-insight-card {
    position: relative;
    overflow: hidden;

    background: rgba(15, 23, 42, 0.42);

    border: 1px solid rgba(255,255,255,0.10);

    border-radius: 24px;

    padding: 1.5rem;

    backdrop-filter: blur(22px);
    -webkit-backdrop-filter: blur(22px);

    box-shadow:
        inset 0 1px 1px rgba(255,255,255,0.08),
        0 20px 40px rgba(0,0,0,0.28);

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease,
        border 0.25s ease;

    margin-bottom: 1.5rem;
}

.ai-insight-card::before {
    content: "";

    position: absolute;

    width: 260px;
    height: 260px;

    top: -90px;
    right: -90px;

    background:
        radial-gradient(
            circle,
            rgba(99,102,241,0.20) 0%,
            rgba(59,130,246,0.10) 40%,
            transparent 75%
        );

    z-index: 0;
}

.ai-insight-card > * {
    position: relative;
    z-index: 2;
}

.ai-insight-card:hover {
    transform: translateY(-6px) scale(1.01);

    border: 1px solid rgba(99,102,241,0.30);

    box-shadow:
        inset 0 1px 1px rgba(255,255,255,0.12),
        0 24px 55px rgba(99,102,241,0.30);
}

.ai-insight-card p {
    color: rgba(255,255,255,0.84);

    line-height: 1.7;

    font-size: 1rem;
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


# -----------------------------
# Helpers
# -----------------------------
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


def modern_histogram(df, column, color, label):
    fig = px.histogram(
        df,
        x=column,
        nbins=18,
        marginal="rug",
        color_discrete_sequence=[color],
        labels={column: label}
    )

    fig.update_traces(
        marker=dict(
            line=dict(
                color="rgba(255,255,255,0.08)",
                width=1
            )
        ),
        opacity=0.78,
        hovertemplate=f"<b>{label}:</b> %{{x}}<br><b>Count:</b> %{{y}}<extra></extra>"
    )

    fig.update_layout(
        bargap=0.28,
        showlegend=False,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(15,23,42,0.35)",
        font=dict(color="white")
    )

    return clean_layout(fig)


# -----------------------------
# Hero
# -----------------------------
st.markdown(
    """
    <div class="trend-hero">
        <h1>Trends & Insights</h1>
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
# Metric highlights
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
# AI-Style Generated Insights
# -----------------------------
hover_title("AI-Generated Insights")

avg_recovery = filtered_df["Recovery_Score"].mean()
avg_sleep = filtered_df["Sleep_Hours"].mean()
avg_steps = filtered_df["Steps"].mean()
avg_calories = filtered_df["Calories_Burned"].mean()

best_recovery_day = filtered_df.loc[filtered_df["Recovery_Score"].idxmax()]
lowest_recovery_day = filtered_df.loc[filtered_df["Recovery_Score"].idxmin()]

insights = []

if avg_sleep >= 7:
    insights.append(
        "Sleep appears to be supporting recovery. Average sleep is at or above the common 7-hour benchmark."
    )
else:
    insights.append(
        "Sleep may be limiting recovery. Average sleep is below 7 hours, which may affect recovery trends."
    )

if avg_steps >= 9000:
    insights.append(
        "Movement levels are strong. Average steps suggest consistent daily activity."
    )
else:
    insights.append(
        "Daily movement could be improved. Average steps are below the higher activity target range."
    )

if avg_recovery >= 60:
    insights.append(
        "Recovery is trending in a healthy range overall, with room for optimization."
    )
else:
    insights.append(
        "Recovery scores suggest possible fatigue patterns or inconsistent recovery habits."
    )

insights.append(
    f"The highest recovery day was {best_recovery_day['Date'].strftime('%Y-%m-%d')} "
    f"with a recovery score of {best_recovery_day['Recovery_Score']:.1f}."
)

insights.append(
    f"The lowest recovery day was {lowest_recovery_day['Date'].strftime('%Y-%m-%d')} "
    f"with a recovery score of {lowest_recovery_day['Recovery_Score']:.1f}."
)

st.markdown(
    f'<div class="ai-insight-card">'
    f'<p><strong>Insight 1:</strong> {insights[0]}</p>'
    f'<p><strong>Insight 2:</strong> {insights[1]}</p>'
    f'<p><strong>Insight 3:</strong> {insights[2]}</p>'
    f'<p><strong>Peak Recovery:</strong> {insights[3]}</p>'
    f'<p><strong>Lowest Recovery:</strong> {insights[4]}</p>'
    f'</div>',
    unsafe_allow_html=True
)
st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------
# Monthly Recovery Trend
# -----------------------------
hover_title("Average Recovery Score by Month")

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

fig_month.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(15,23,42,0.35)",
    font=dict(color="white")
)

st.plotly_chart(
    clean_layout(fig_month),
    use_container_width=True
)

st.markdown("<br>", unsafe_allow_html=True)


# -----------------------------
# Histograms
# -----------------------------
hover_title("Metric Distributions")

col1, col2 = st.columns(2)

with col1:
    fig_steps = modern_histogram(
        filtered_df,
        "Steps",
        "rgba(0,255,200,0.82)",
        "Steps"
    )

    st.plotly_chart(fig_steps, use_container_width=True)

with col2:
    fig_calories = modern_histogram(
        filtered_df,
        "Calories_Burned",
        "rgba(255,180,0,0.82)",
        "Calories Burned"
    )

    st.plotly_chart(fig_calories, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    fig_recovery = modern_histogram(
        filtered_df,
        "Recovery_Score",
        "rgba(140,110,255,0.82)",
        "Recovery Score"
    )

    st.plotly_chart(fig_recovery, use_container_width=True)

with col4:
    fig_sleep = modern_histogram(
        filtered_df,
        "Sleep_Hours",
        "rgba(255,60,170,0.82)",
        "Sleep Hours"
    )

    st.plotly_chart(fig_sleep, use_container_width=True)