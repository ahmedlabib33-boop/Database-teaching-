import pandas as pd
import streamlit as st


def show_progress():
    st.title("Progress")

    history = st.session_state.get("progress_history", [])
    if not history:
        st.info("No exam attempts yet. Submit a mock exam to start tracking progress.")
        return

    df = pd.DataFrame(history)

    latest = df.iloc[-1]
    best = df.loc[df["percent"].idxmax()]
    average = df["percent"].mean()

    col1, col2, col3 = st.columns(3)
    col1.metric("Latest Score", f"{latest['percent']:.1f}%")
    col2.metric("Best Score", f"{best['percent']:.1f}%")
    col3.metric("Average", f"{average:.1f}%")

    subject = st.selectbox("Filter Subject", ["All", "English", "Math"])
    filtered = df if subject == "All" else df[df["subject"] == subject]

    st.subheader("Attempt History")
    st.dataframe(filtered, use_container_width=True)

    if len(filtered) >= 2:
        chart_df = filtered[["exam_id", "percent"]].set_index("exam_id")
        st.bar_chart(chart_df)
    else:
        st.caption("The progress chart will appear after at least two attempts.")
