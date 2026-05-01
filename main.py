import streamlit as st

import warnings

from styles.theme import load_theme

load_theme()


warnings.filterwarnings(
    "ignore",
    category=FutureWarning
)

st.set_page_config(
    page_title="Kat's Health Analytics",
    page_icon="",
    layout="wide"
)

st.markdown(
    """
    <style>

 COLORS = {
    "blue": "#38BDF8",
    "indigo": "#6366F1",
    "pink": "#EC4899",
    "green": "#22C55E",
    "amber": "#F59E0B",
    "text": "#F8FAFC",
    "muted": "#CBD5E1"
}   

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
    .hero {
        padding: 3rem;
        border-radius: 28px;
        background: linear-gradient(135deg, #0F172A, #1E293B, #312E81);
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 20px 50px rgba(0,0,0,0.35);
    }

    .hero h1 {
        font-size: 4rem;
        margin-bottom: 0.5rem;
    }

    .hero p {
        font-size: 1.25rem;
        color: #CBD5E1;
    }

   .slide-deck {
    height: 360px;
    border-radius: 28px;
    overflow: hidden;
    background-size: cover;
    background-position: center;
    animation: healthSlides 24s infinite;
    box-shadow: 0 20px 50px rgba(0,0,0,0.45);
    margin-bottom: 2rem;
}

@keyframes healthSlides {
    0% {
        background-image: url("https://images.unsplash.com/photo-1518611012118-696072aa579a");
    }
    25% {
        background-image: url("https://images.unsplash.com/photo-1517836357463-d25dfeac3438");
    }
    50% {
        background-image: url("https://images.unsplash.com/photo-1490645935967-10de6ba17061");
    }
    75% {
        background-image: url("https://images.unsplash.com/photo-1506126613408-eca07ce68773");
    }
    100% {
        background-image: url("https://images.unsplash.com/photo-1518611012118-696072aa579a");
    }
}

   .card {
    padding: 1.5rem;
    border-radius: 22px;
    background: rgba(15, 23, 42, 0.88);
    border: 1px solid rgba(148, 163, 184, 0.14);
    backdrop-filter: blur(14px);
    min-height: 180px;
}

    .card h3 {
        color: #38BDF8;
    }

    .card p {
        color: #CBD5E1;
        line-height: 1.5;
    }
.card {
    position: relative;
    overflow: hidden;
    transition:
        transform 0.3s ease,
        box-shadow 0.3s ease,
        border 0.3s ease;
}

.card::before {
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
    opacity: 0.75;
    transition: opacity 0.3s ease;
}

.card:hover {
    transform: translateY(-8px) scale(1.015);
    box-shadow:
        0 0 20px rgba(56, 189, 248, 0.35),
        0 0 40px rgba(99, 102, 241, 0.25),
        0 0 60px rgba(236, 72, 153, 0.18);
}

.card:hover::before {
    opacity: 1;
}
    

    .nav-box {
        padding: 1.75rem;
        border-radius: 24px;
        background: rgba(30, 41, 59, 0.95);
        border-left: 6px solid #38BDF8;
        margin-top: 2rem;
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


@media (max-width: 768px) {
    .slide-deck {
        height: 220px !important;
        border-radius: 22px !important;
    }
}

    .hero h1,
    .trend-hero h1,
    .hero-premium h1 {
        font-size: 2.4rem !important;
        line-height: 1.1 !important;
    }

    .hero p,
    .trend-hero p,
    .hero-premium p {
        font-size: 1rem !important;
    }

    .card,
    .card-glow,
    .premium-card,
    .nav-box {
        padding: 1rem !important;
        border-radius: 20px !important;
        margin-bottom: 1rem !important;
    }

    [data-testid="stMetric"] {
        width: 100% !important;
    }

    [data-testid="stPlotlyChart"] {
        min-height: 320px !important;
    }

    .slide-deck {
        height: 220px !important;
        border-radius: 22px !important;
    }
}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero">
        <h1>Welcome to Kat's Health Analytics</h1>
        <p>A modern health analytics dashboard for recovery, sleep, movement, and energy.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="slide-deck"></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="card">
            <h3>📊 Dashboard</h3>
            <p>View your key health metrics, including steps, sleep, recovery score, heart rate, and calories burned.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="card">
            <h3>📈 Trends & Insights</h3>
            <p>Explore deeper patterns with monthly recovery trends and distribution charts.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="card">
            <h3>🧠 Built with AI</h3>
            <p>This project uses Python, Streamlit, Plotly, and AI-assisted development to analyze synthetic health data.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    """
    <div class="nav-box">
        <h2>🚀 How to Navigate</h2>
        <p>Use the sidebar on the left to move between pages.</p>
        <p>👉 Click <strong>Dashboard</strong> for metrics and charts.</p>
        <p>👉 Click <strong>Trends & Insights</strong> for deeper visual analysis.</p>
    </div>
    """,
    unsafe_allow_html=True
)