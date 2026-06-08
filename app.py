import streamlit as st

import navigation
from session import initialize_session
from pages.home import show_home
from pages.learning import show_learning
from pages.mock_exam import show_mock_exam
from pages.music import show_music
from pages.live_call import show_live_call
from pages.review import show_review
from pages.progress import show_progress


st.set_page_config(
    page_title="Leila EST Prep",
    layout="wide",
    initial_sidebar_state="collapsed"
)

initialize_session()

page = navigation.app_navigation()

st.markdown("""
<style>

[data-testid="stSidebar"],
[data-testid="collapsedControl"] {
    display: none;
}

.block-container {
    max-width: 1180px;
    padding-top: 2rem;
    padding-left: 2rem;
    padding-right: 2rem;
}

.top-nav-title {
    text-align: center;
    font-size: clamp(15px, 2vw, 18px);
    font-weight: 800;
    color: #1f2937;
    margin: 1rem 0 2rem;
}

.stButton button {
    min-height: 50px;
    border-radius: 8px;
    border: 1px solid #dbe3ef;
    background: white;
    color: #1f2937;
    font-size: clamp(14px, 1.4vw, 17px);
    font-weight: 500;
    white-space: normal;
    line-height: 1.15;
}

.stButton button:hover {
    border-color: #93c5fd;
    background: #eaf3ff;
    color: #0f172a;
}

.global-footer {
    margin-top: 2.5rem;
    padding: 1rem 1.25rem;
    border-radius: 0.5rem;
    background: #e8f2ff;
    color: #0056a8;
    font-size: clamp(15px, 2vw, 18px);
    font-weight: 500;
    overflow-wrap: anywhere;
}

h1 {
    font-size: clamp(30px, 5vw, 50px) !important;
    line-height: 1.15 !important;
}

h2 {
    font-size: clamp(24px, 4vw, 34px) !important;
}

h3 {
    font-size: clamp(20px, 3vw, 28px) !important;
}

p, li, div {
    overflow-wrap: anywhere;
}

iframe {
    max-width: 100%;
    border-radius: 16px;
}

/* Mobile optimization */
@media (max-width: 1100px) {
    div[data-testid="column"] {
        min-width: 140px;
    }
}

@media (max-width: 768px) {

    .block-container {
        max-width: 100%;
        padding-top: 1rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }

    div[data-testid="column"] {
        width: 100% !important;
        flex: 1 1 100% !important;
    }

    p, div {
        font-size: 15px !important;
    }

    .stSelectbox {
        width: 100%;
    }
}

@media (max-width: 430px) {
    .global-footer {
        padding: 0.9rem;
    }

    p, div {
        font-size: 14px !important;
    }
}

</style>
""", unsafe_allow_html=True)


def show_global_footer():
    st.markdown(
        '<div class="global-footer">Developed by BEBA | Ahmed Labib | 2026 Ⓡ ™</div>',
        unsafe_allow_html=True,
    )


# ---------------- HOME ----------------

if page == "Home":

    show_home()

# ---------------- LEARNING ----------------

elif page == "Learning Mode":

    show_learning()

# ---------------- MOCK EXAM ----------------

elif page == "Mock Exam":

    show_mock_exam()

# ---------------- STUDY MUSIC ----------------

elif page == "Study Music":

    show_music()

# ---------------- LIVE CALL ----------------

elif page == "Live Call":

    show_live_call()

# ---------------- REVIEW ----------------

elif page == "Review Mistakes":

    show_review()

# ---------------- PROGRESS ----------------

elif page == "Progress":

    show_progress()

show_global_footer()
