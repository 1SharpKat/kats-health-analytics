import streamlit as st

def load_theme():
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

        </style>
        """,
        unsafe_allow_html=True
    )