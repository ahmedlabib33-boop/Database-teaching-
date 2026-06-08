import streamlit as st

def initialize_session():

    if "score" not in st.session_state:
        st.session_state.score = 0

    if "wrong_answers" not in st.session_state:
        st.session_state.wrong_answers = []

    if "completed_topics" not in st.session_state:
        st.session_state.completed_topics = []

    if "current_question" not in st.session_state:
        st.session_state.current_question = 0

    if "progress_history" not in st.session_state:
        st.session_state.progress_history = []

    if "mistakes" not in st.session_state:
        st.session_state.mistakes = []
