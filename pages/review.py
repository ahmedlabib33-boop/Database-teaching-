import streamlit as st


def show_review():
    st.title("Review Mistakes")

    mistakes = st.session_state.get("mistakes", [])
    if not mistakes:
        st.info("No mistakes saved yet. Complete a mock exam to build a review list.")
        return

    subject = st.selectbox("Filter Subject", ["All", "English", "Math"])
    filtered = [
        mistake
        for mistake in mistakes
        if subject == "All" or mistake.get("subject") == subject
    ]

    col1, col2 = st.columns(2)
    col1.metric("Saved mistakes", len(filtered))
    if col2.button("Clear all saved mistakes"):
        st.session_state.mistakes = []
        st.rerun()

    for index, mistake in enumerate(filtered, start=1):
        title = (
            f"{index}. {mistake['subject']} | {mistake['exam_id']} | "
            f"Q{mistake['question_number']} | {mistake['skill']}"
        )
        with st.expander(title):
            if mistake.get("passage"):
                st.markdown("**Passage**")
                st.info(mistake["passage"])

            st.markdown(f"**Question:** {mistake['question']}")
            st.write(f"Your answer: {mistake['your_answer']}")
            st.write(f"Correct answer: {mistake['correct_answer']}")
            st.info(mistake["explanation"])
