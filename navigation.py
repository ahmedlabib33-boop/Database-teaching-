import streamlit as st

PAGES = [
    ("Home", "Home"),
    ("Learning Mode", "Learning"),
    ("Mock Exam", "Mock Exam"),
    ("Study Music", "Music"),
    ("Live Call", "Live Call"),
    ("Review Mistakes", "Review"),
    ("Progress", "Progress"),
]


def app_navigation():
    if "active_page" not in st.session_state:
        st.session_state.active_page = "Home"

    st.markdown('<div class="top-nav-title">Choose a section</div>', unsafe_allow_html=True)
    cols = st.columns(len(PAGES))

    for col, (page, label) in zip(cols, PAGES):
        with col:
            if st.button(label, key=f"nav_{page}", use_container_width=True):
                st.session_state.active_page = page
                st.rerun()

    return st.session_state.active_page
