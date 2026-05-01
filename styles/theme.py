import streamlit as st

def load_theme():
    st.markdown(
        """
        <style>

    .title-card {
    padding: 1rem 1.25rem;
    margin-bottom: 0.75rem;
    border-radius: 20px;
    background: rgba(15, 23, 42, 0.88);
    border: 1px solid rgba(148, 163, 184, 0.16);
    box-shadow: 0 12px 30px rgba(0,0,0,0.28);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.title-card:hover {
    transform: translateY(-4px);
    box-shadow:
        0 0 20px rgba(56, 189, 248, 0.24),
        0 0 38px rgba(99, 102, 241, 0.18);
}

.title-card h3 {
    margin: 0;
    color: #F8FAFC;
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

        .card-glow:hover {
            transform: translateY(-8px) scale(1.01);

            box-shadow:
                0 0 20px rgba(56, 189, 248, 0.28),
                0 0 40px rgba(99, 102, 241, 0.22),
                0 0 60px rgba(236, 72, 153, 0.14);
        }

        section[data-testid="stSidebar"] {
            background: rgba(2, 6, 23, 0.96);
            border-right: 1px solid rgba(148, 163, 184, 0.15);
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
            .card-glow {
                padding: 1rem !important;
                border-radius: 20px !important;
            }

            [data-testid="stPlotlyChart"] {
                min-height: 320px !important;
            }
        }

        section[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            rgba(2, 6, 23, 0.98),
            rgba(15, 23, 42, 0.96)
        ) !important;

    border-right: 1px solid rgba(148, 163, 184, 0.14);
}

section[data-testid="stSidebar"] * {
    color: #F8FAFC !important;
}

section[data-testid="stSidebar"] label {
    color: #CBD5E1 !important;
}

section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] {
    background: rgba(15, 23, 42, 0.92) !important;
    border-radius: 14px;
    border: 1px solid rgba(148, 163, 184, 0.16);
}

/* Dark sidebar selectbox */
section[data-testid="stSidebar"] div[data-baseweb="select"] {
    background-color: #0F172A !important;
    border-radius: 14px !important;
    border: 1px solid rgba(148, 163, 184, 0.28) !important;
}

section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
    background-color: #0F172A !important;
    color: #F8FAFC !important;
}

section[data-testid="stSidebar"] div[data-baseweb="select"] span {
    color: #F8FAFC !important;
}

section[data-testid="stSidebar"] input {
    color: #F8FAFC !important;
}

/* Dropdown menu options */
div[data-baseweb="popover"] {
    background-color: #0F172A !important;
}

div[data-baseweb="menu"] {
    background-color: #0F172A !important;
    color: #F8FAFC !important;
}

div[data-baseweb="menu"] li {
    background-color: #0F172A !important;
    color: #F8FAFC !important;
}

div[data-baseweb="menu"] li:hover {
    background-color: #1E293B !important;
}

/* Force Streamlit selectbox + dropdown menu dark */
[data-baseweb="select"],
[data-baseweb="select"] > div,
[data-baseweb="select"] div,
[data-baseweb="select"] span {
    background-color: #0F172A !important;
    color: #F8FAFC !important;
}

[data-baseweb="select"] {
    border: 1px solid rgba(148, 163, 184, 0.28) !important;
    border-radius: 14px !important;
}

[data-baseweb="popover"],
[data-baseweb="popover"] > div,
[data-baseweb="menu"],
[data-baseweb="menu"] ul,
[data-baseweb="menu"] li,
ul[role="listbox"],
li[role="option"] {
    background-color: #0F172A !important;
    color: #F8FAFC !important;
}

li[role="option"]:hover,
li[aria-selected="true"] {
    background-color: #1E293B !important;
    color: #38BDF8 !important;
}
        </style>
        """,
        unsafe_allow_html=True
    )