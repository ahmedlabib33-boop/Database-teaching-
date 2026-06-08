from datetime import datetime

import pandas as pd
import streamlit as st

from loaders.mock_loader import load_mock_english, load_mock_math


LETTERS = ["A", "B", "C", "D"]


def _load_subject(subject):
    if subject == "Math":
        return load_mock_math()
    return load_mock_english()


def _option_text(row, letter):
    return str(row[f"option_{letter.lower()}"]).strip()


def _result_box(result):
    st.success(
        f"Score: {result['score']} / {result['total']} "
        f"({result['percent']:.1f}%)"
    )
    st.progress(result["percent"] / 100)

    if result["mistakes"]:
        st.warning(f"Mistakes to review: {len(result['mistakes'])}")
        with st.expander("Show answer review"):
            for item in result["mistakes"]:
                st.markdown(f"**Q{item['question_number']}. {item['question']}**")
                if item["passage"]:
                    st.caption(item["passage"])
                st.write(f"Your answer: {item['your_answer']}")
                st.write(f"Correct answer: {item['correct_answer']}")
                st.info(item["explanation"])
                st.markdown("---")
    else:
        st.balloons()
        st.success("Perfect work. No mistakes in this attempt.")


def show_mock_exam():
    st.title("Mock Exam")
    st.info(
        "English exams contain 85 multiple-choice questions. Math exams contain "
        "50 multiple-choice questions. All questions are original EST-style "
        "practice based on Leila's learning materials."
    )

    subject = st.selectbox("Choose Subject", ["English", "Math"])
    df = _load_subject(subject)
    exam_ids = df["exam_id"].drop_duplicates().tolist()
    exam_id = st.selectbox("Choose Exam", exam_ids)

    exam_df = df[df["exam_id"] == exam_id].sort_values("question_number")
    st.caption(f"{len(exam_df)} questions")

    answers = {}
    with st.form(f"{subject}_{exam_id}_form"):
        for section, section_df in exam_df.groupby("section", sort=False):
            st.header(section)
            last_passage = None

            for _, row in section_df.iterrows():
                qn = int(row["question_number"])
                passage = str(row.get("passage", "")).strip()
                if passage and passage != last_passage:
                    st.markdown("**Passage**")
                    st.info(passage)
                    last_passage = passage

                options = ["Not answered"] + [
                    f"{letter}. {_option_text(row, letter)}" for letter in LETTERS
                ]
                selected = st.radio(
                    f"{qn}. {row['question']}",
                    options,
                    key=f"{subject}_{exam_id}_{qn}",
                )
                answers[qn] = "" if selected == "Not answered" else selected[0]

        submitted = st.form_submit_button("Submit Exam")

    if submitted:
        result = _grade_exam(subject, exam_id, exam_df, answers)
        st.session_state.last_exam_result = result
        st.session_state.progress_history.append(
            {
                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "subject": subject,
                "exam_id": exam_id,
                "score": result["score"],
                "total": result["total"],
                "percent": round(result["percent"], 1),
                "mistakes": len(result["mistakes"]),
            }
        )
        st.session_state.mistakes.extend(result["mistakes"])

    result = st.session_state.get("last_exam_result")
    if result and result["subject"] == subject and result["exam_id"] == exam_id:
        _result_box(result)


def _grade_exam(subject, exam_id, exam_df, answers):
    mistakes = []
    score = 0

    for _, row in exam_df.iterrows():
        qn = int(row["question_number"])
        selected = answers.get(qn, "")
        correct = str(row["correct_answer"]).strip()

        if selected == correct:
            score += 1
            continue

        correct_text = _option_text(row, correct)
        selected_text = "Not answered"
        if selected in LETTERS:
            selected_text = f"{selected}. {_option_text(row, selected)}"

        mistakes.append(
            {
                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "subject": subject,
                "exam_id": exam_id,
                "section": row["section"],
                "question_number": qn,
                "skill": row["skill"],
                "passage": str(row.get("passage", "")).strip(),
                "question": row["question"],
                "your_answer": selected_text,
                "correct_answer": f"{correct}. {correct_text}",
                "explanation": row["explanation"],
            }
        )

    total = len(exam_df)
    return {
        "subject": subject,
        "exam_id": exam_id,
        "score": score,
        "total": total,
        "percent": (score / total * 100) if total else 0,
        "mistakes": mistakes,
    }
