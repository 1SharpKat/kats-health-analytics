import streamlit as st
import warnings

from styles.theme import load_theme
from utils.constants import COLORS

warnings.filterwarnings("ignore", category=FutureWarning)

st.set_page_config(
    page_title="Kat's Health Analytics",
    layout="wide"
)

load_theme()

st.markdown(
    f"""
    <style>
    header[data-testid="stHeader"] {{
        display: none;
    }}

    [data-testid="stToolbar"] {{
        display: none;
    }}

    .block-container {{
        padding-top: 1rem;
        position: relative;
        z-index: 2;
    }}

    .stApp {{
        background: linear-gradient(135deg, #020617, #0F172A, #111827);
    }}

    .slide-deck {{
        position: fixed;
        inset: 0;
        z-index: 0;
        overflow: hidden;
        pointer-events: none;
    }}

    .slide {{
        position: absolute;
        inset: 0;
        background-size: cover;
        background-position: center;
        opacity: 0;
        animation: fadeSlide 24s infinite, slowZoom 24s infinite;
    }}

    .slide:nth-child(1) {{
        background-image: url("https://images.unsplash.com/photo-1517836357463-d25dfeac3438?q=80&w=2200&auto=format&fit=crop");
        animation-delay: 0s;
    }}

    .slide:nth-child(2) {{
        background-image: url("https://images.unsplash.com/photo-1518611012118-696072aa579a?q=80&w=2200&auto=format&fit=crop");
        animation-delay: 6s;
    }}

    .slide:nth-child(3) {{
        background-image: url("https://images.unsplash.com/photo-1490645935967-10de6ba17061?q=80&w=2200&auto=format&fit=crop");
        animation-delay: 12s;
    }}

    .slide:nth-child(4) {{
        background-image: url("https://images.unsplash.com/photo-1506126613408-eca07ce68773?q=80&w=2200&auto=format&fit=crop");
        animation-delay: 18s;
    }}

    .slide-deck::after {{
        content: "";
        position: absolute;
        inset: 0;
        background: linear-gradient(
            135deg,
            rgba(2,6,23,0.22),
            rgba(15,23,42,0.16),
            rgba(30,41,59,0.22)
        );
        z-index: 2;
    }}

    @keyframes fadeSlide {{
        0% {{ opacity: 0; }}
        8% {{ opacity: 0.72; }}
        22% {{ opacity: 0.72; }}
        30% {{ opacity: 0; }}
        100% {{ opacity: 0; }}
    }}

    @keyframes slowZoom {{
        from {{ transform: scale(1); }}
        to {{ transform: scale(1.08); }}
    }}

    .home-hero {{
        will-change: transform;
        position: relative;
        overflow: hidden;
        padding: 2.5rem;
        margin-bottom: 2rem;
        border-radius: 28px;
        background: rgba(15, 23, 42, 0.42);
        backdrop-filter: blur(22px);
        -webkit-backdrop-filter: blur(22px);
        border: 1px solid rgba(255,255,255,0.10);
        box-shadow:
            inset 0 1px 1px rgba(255,255,255,0.12),
            0 24px 55px rgba(99, 102, 241, 0.30);
        transition:
            transform 0.25s ease,
            box-shadow 0.25s ease,
            border 0.25s ease;
    }}

    .home-hero:hover {{
        transform: translateY(-4px) scale(1.005);
        border: 1px solid rgba(99, 102, 241, 0.30);
        box-shadow:
            inset 0 1px 1px rgba(255,255,255,0.08),
            0 24px 48px rgba(99, 102, 241, 0.20);
    }}

    .home-hero::before {{
        content: "";
        position: absolute;
        width: 320px;
        height: 320px;
        background:
            radial-gradient(
                circle,
                rgba(99,102,241,0.24) 0%,
                rgba(59,130,246,0.14) 40%,
                transparent 75%
            );
        top: -120px;
        right: -120px;
        z-index: 0;
    }}

    .home-hero > * {{
        position: relative;
        z-index: 2;
    }}

    .home-hero h1 {{
        font-size: 4rem;
        font-weight: 800;
        letter-spacing: -1px;
        margin-bottom: 0.5rem;
        color: white;
    }}

    .home-hero p {{
        font-size: 1.15rem;
        color: rgba(255,255,255,0.82);
        max-width: 850px;
    }}

    .home-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1.5rem;
        margin-top: 1.5rem;
    }}

    .home-card {{
        will-change: transform;
        position: relative;
        overflow: hidden;
        min-height: 220px;
        padding: 1.75rem;
        border-radius: 24px;
        background: rgba(15, 23, 42, 0.42);
        backdrop-filter: blur(22px);
        -webkit-backdrop-filter: blur(22px);
        border: 1px solid rgba(255,255,255,0.10);
        box-shadow:
            inset 0 1px 1px rgba(255,255,255,0.08),
            0 20px 40px rgba(0,0,0,0.28);
        transition:
            transform 0.25s ease,
            box-shadow 0.25s ease,
            border 0.25s ease;
    }}

    .home-card::before {{
        content: "";
        position: absolute;
        width: 220px;
        height: 220px;
        background:
            radial-gradient(
                circle,
                rgba(99,102,241,0.22) 0%,
                rgba(59,130,246,0.12) 40%,
                transparent 75%
            );
        top: -70px;
        right: -70px;
        z-index: 0;
    }}

    .home-card > * {{
        position: relative;
        z-index: 2;
    }}

    .home-card:hover {{
        transform: translateY(-6px) scale(1.01);
        border: 1px solid rgba(99, 102, 241, 0.30);
        box-shadow:
            inset 0 1px 1px rgba(255,255,255,0.12),
            0 24px 55px rgba(99, 102, 241, 0.30);
    }}

    .home-card h3 {{
        color: white;
        font-size: 1.45rem;
        font-weight: 700;
        letter-spacing: -0.3px;
        margin-bottom: 0.85rem;
        border-bottom: 1px solid rgba(255,255,255,0.08);
        padding-bottom: 0.65rem;
    }}

    .home-card p {{
        color: rgba(255,255,255,0.78);
        font-size: 1rem;
        line-height: 1.6;
        font-weight: 400;
        letter-spacing: 0.2px;
    }}

    .nav-card {{
        margin-top: 2rem;
        padding: 1.75rem;
        border-radius: 24px;
        background: rgba(15, 23, 42, 0.42);
        backdrop-filter: blur(22px);
        -webkit-backdrop-filter: blur(22px);
        border: 1px solid rgba(255,255,255,0.10);
        box-shadow:
            inset 0 1px 1px rgba(255,255,255,0.08),
            0 20px 40px rgba(0,0,0,0.28);
    }}

    .nav-card h3 {{
        color: white;
        font-size: 1.4rem;
        font-weight: 700;
        letter-spacing: -0.3px;
        margin-bottom: 1rem;
        border-bottom: 1px solid rgba(255,255,255,0.08);
        padding-bottom: 0.65rem;
    }}

    .nav-card p {{
        color: rgba(255,255,255,0.82);
        font-size: 1.05rem;
        line-height: 1.6;
        font-weight: 400;
        letter-spacing: 0.2px;
    }}

    @media (max-width: 900px) {{
        .home-grid {{
            grid-template-columns: 1fr;
        }}

        .home-hero h1 {{
            font-size: 2.6rem;
        }}
    }}
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

st.markdown(
    '<div class="home-hero"><h1>Kat&apos;s Health Analytics</h1><p>A modern health analytics app for recovery, sleep, movement, calories, and energy.</p><p>Built with Python, Streamlit, Plotly, and AI-assisted development.</p></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="home-grid">'
    '<div class="home-card"><h3>Dashboard</h3><p>View your key health metrics, including average steps, sleep hours, recovery score, heart rate, and calories burned.</p></div>'
    '<div class="home-card"><h3>Trends & Insights</h3><p>Explore deeper patterns with monthly recovery trends, summary statistics, and distribution charts.</p></div>'
    '<div class="home-card"><h3>Built with AI</h3><p>This project uses synthetic health data to demonstrate data cleaning, visualization, dashboard design, and AI-assisted development.</p></div>'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="nav-card"><h3>Navigation</h3>'
    '<p>Use the sidebar on the left to move between pages.</p>'
    '<p>Select <strong>Dashboard</strong> for metrics and charts.</p>'
    '<p>Select <strong>Trends & Insights</strong> for deeper visual analysis.</p>'
    '</div>',
    unsafe_allow_html=True
)