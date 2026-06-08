import math

import pandas as pd
import streamlit as st

from ai.course_generator.english_course_generator import generate_english_course
from ai.course_generator.math_course_generator import generate_math_course
from loaders.learning_loader import load_english_content, load_math_content


def _text(value):
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except TypeError:
        pass
    return str(value).strip()


def _parts(value):
    return [part.strip() for part in _text(value).split("|") if part.strip()]


def _show_parts(value, renderer=st.info):
    for part in _parts(value):
        renderer(part)


def _difficulty_score(value):
    scores = {"Easy": 1, "Medium": 2, "Hard": 3}
    return scores.get(_text(value), 0)


def _show_math_topic_visuals(df, topic_df):
    st.markdown("### Math Topic Visualizations")

    topic_lessons = topic_df.drop_duplicates("lesson_title")
    lesson_count = topic_lessons["lesson_title"].nunique()
    formula_count = topic_lessons["formula"].apply(lambda value: bool(_text(value))).sum()
    average_difficulty = topic_lessons["difficulty"].apply(_difficulty_score).mean()

    col1, col2, col3 = st.columns(3)
    col1.metric("Lessons In Topic", lesson_count)
    col2.metric("Lessons With Formulas", int(formula_count))
    col3.metric("Average Difficulty", f"{average_difficulty:.1f} / 3")

    col1, col2 = st.columns(2)

    with col1:
        st.write("##### Lessons Per Math Domain")
        domain_counts = (
            df.groupby("domain")["lesson_title"]
            .nunique()
            .sort_values(ascending=False)
        )
        st.bar_chart(domain_counts)

    with col2:
        st.write("##### Difficulty In Selected Topic")
        difficulty_order = ["Easy", "Medium", "Hard"]
        difficulty_counts = (
            topic_lessons["difficulty"]
            .value_counts()
            .reindex(difficulty_order, fill_value=0)
        )
        st.bar_chart(difficulty_counts)

    st.write("##### Selected Topic Lesson Map")
    lesson_map = topic_lessons[["lesson_title", "difficulty", "formula"]].copy()
    lesson_map["has_example"] = topic_lessons["example"].apply(
        lambda value: "Yes" if _text(value) else "No"
    )
    lesson_map = lesson_map.rename(
        columns={
            "lesson_title": "Lesson",
            "difficulty": "Difficulty",
            "formula": "Formula",
            "has_example": "Example",
        }
    )
    st.dataframe(lesson_map, use_container_width=True, hide_index=True)


def _sample_graph_data(row):
    title = _text(row.get("lesson_title")).lower()
    formula = _text(row.get("formula")).lower()
    combined = f"{title} {formula}"
    x_values = list(range(-5, 6))

    if any(keyword in combined for keyword in ["slope", "linear", "y=mx+b", "ax+b"]):
        return (
            "Equation Plot: y = 2x + 1",
            pd.DataFrame({"x": x_values, "y": [2 * x + 1 for x in x_values]}),
            "line",
        )

    if any(keyword in combined for keyword in ["quadratic", "vertex", "ax2", "x2", "x^2"]):
        return (
            "Equation Plot: y = x^2 - 2x - 3",
            pd.DataFrame({"x": x_values, "y": [x**2 - 2 * x - 3 for x in x_values]}),
            "line",
        )

    if any(keyword in combined for keyword in ["absolute value", "|x|"]):
        return (
            "Equation Plot: y = |x|",
            pd.DataFrame({"x": x_values, "y": [abs(x) for x in x_values]}),
            "line",
        )

    if any(keyword in combined for keyword in ["exponential", "growth", "a(b)^x"]):
        return (
            "Equation Plot: y = 2^x",
            pd.DataFrame({"x": list(range(0, 8)), "y": [2**x for x in range(0, 8)]}),
            "line",
        )

    if "circle" in combined:
        points = []
        radius = 5
        for step in range(0, 37):
            angle = step * 10
            radians = angle * math.pi / 180
            points.append(
                {
                    "angle": angle,
                    "x": radius * math.cos(radians),
                    "y": radius * math.sin(radians),
                }
            )
        return "Equation Plot: x^2 + y^2 = 25", pd.DataFrame(points), "circle"

    return None, None, None


def _show_equation_plot(row):
    graph_title, graph_df, graph_type = _sample_graph_data(row)
    if graph_df is None:
        return False

    st.write(f"##### {graph_title}")
    if graph_type == "circle":
        st.vega_lite_chart(
            graph_df,
            {
                "mark": {"type": "line", "point": True},
                "encoding": {
                    "x": {"field": "x", "type": "quantitative"},
                    "y": {"field": "y", "type": "quantitative"},
                    "tooltip": [
                        {"field": "x", "type": "quantitative"},
                        {"field": "y", "type": "quantitative"},
                    ],
                },
            },
            use_container_width=True,
        )
    else:
        st.line_chart(graph_df.set_index("x"))

    return True


def _is_triangle_area_lesson(row):
    combined = f"{_text(row.get('lesson_title'))} {_text(row.get('formula'))}".lower()
    return "triangle" in combined and any(keyword in combined for keyword in ["area", "surface"])


def _show_triangle_area_visual(row):
    if not _is_triangle_area_lesson(row):
        return False

    st.write("##### Triangle Area Visualization")
    st.markdown(
        """
<svg viewBox="0 0 520 300" width="100%" height="300" role="img" aria-label="Triangle area diagram">
  <rect x="1" y="1" width="518" height="298" rx="16" fill="#f8fafc" stroke="#d7dee8"/>
  <polygon points="80,240 440,240 180,60" fill="#dbeafe" stroke="#2563eb" stroke-width="4"/>
  <line x1="180" y1="60" x2="180" y2="240" stroke="#dc2626" stroke-width="4" stroke-dasharray="8 8"/>
  <path d="M180 240 L205 240 L205 215" fill="none" stroke="#dc2626" stroke-width="3"/>
  <text x="245" y="270" text-anchor="middle" font-size="22" fill="#1e293b">base = b</text>
  <text x="195" y="150" font-size="22" fill="#dc2626">height = h</text>
  <text x="270" y="105" font-size="24" fill="#1d4ed8">Triangle</text>
  <text x="150" y="35" font-size="22" fill="#0f172a">Area = 1/2 x base x height</text>
</svg>
        """,
        unsafe_allow_html=True,
    )
    st.info(
        "The base is the bottom side of the triangle. The height is the straight "
        "perpendicular distance from the top point down to the base. A triangle is "
        "half of a matching rectangle, so its area is 1/2 x base x height."
    )
    return True


def _show_math_lesson_visuals(row):
    shown_equation = _show_equation_plot(row)
    shown_shape = _show_triangle_area_visual(row)

    if not shown_equation and not shown_shape:
        st.caption("No special graph is available for this lesson yet.")


def show_learning():
    st.title("Learning Mode")

    subject = st.selectbox("Choose Subject", ["Math", "English"])

    if subject == "Math":
        _show_math_topics()
    else:
        _show_english_topics()


def _show_math_topics():
    st.subheader("Math Topics")
    _show_math_learning()


def _show_english_topics():
    st.subheader("English Topics")
    _show_english_learning()


def _show_math_learning():
    df = load_math_content().fillna("")
    topic_rows = df[["topic_id", "domain"]].drop_duplicates()
    topic_labels = topic_rows["domain"].tolist()

    selected_topic = st.selectbox("Choose Math Topic", topic_labels)
    filtered = df[df["domain"] == selected_topic]
    st.subheader(selected_topic)
    _show_math_topic_visuals(df, filtered)

    selected_lesson = st.selectbox("Choose Lesson", filtered["lesson_title"].tolist())
    filtered = df[df["lesson_title"] == selected_lesson]

    for _, row in filtered.iterrows():
        st.divider()
        st.header(_text(row["lesson_title"]))

        domain = _text(row.get("domain"))
        difficulty = _text(row.get("difficulty"))
        if domain or difficulty:
            st.caption(" | ".join(item for item in [domain, difficulty] if item))

        formula = _text(row.get("formula"))
        if formula:
            st.write("##### Formula")
            st.info(formula)

        example = _text(row.get("example"))
        if example:
            st.write("##### Example")
            st.info(example)

        st.write("##### Explanation")
        _show_parts(row.get("explanation"))

        _show_math_lesson_visuals(row)

        if st.button(f"Generate AI Explanation: {_text(row['lesson_title'])}"):
            ai_explanation = generate_math_course(_text(row["lesson_title"]))
            st.success("AI explanation generated")
            st.write(ai_explanation)


def _show_english_learning():
    df = load_english_content().fillna("")
    topic_rows = df[["topic_id", "lesson_title"]].drop_duplicates()
    topic_labels = topic_rows["lesson_title"].tolist()

    selected_topic = st.selectbox("Choose English Topic", topic_labels)
    filtered = df[df["lesson_title"] == selected_topic]
    st.subheader(selected_topic)

    if st.button(f"Generate AI Explanation: {selected_topic}"):
        ai_explanation = generate_english_course(selected_topic)
        st.success("AI explanation generated")
        st.write(ai_explanation)

    for _, row in filtered.iterrows():
        st.divider()

        rule_title = _text(row.get("rule_title"))
        if rule_title:
            st.markdown(f"#### {rule_title}")

        explanation = _text(row.get("explanation"))
        if explanation:
            st.write("### Rule")
            _show_parts(explanation)

        example = _text(row.get("example"))
        if example:
            st.write("### Example")
            st.info(example)

        tip = _text(row.get("tip"))
        if tip:
            st.write("### Tip")
            _show_parts(tip, st.success)
