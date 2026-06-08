from ai.ai_engine import generate_text

from ai.prompts.math_course_prompts import (
    math_course_prompt
)


def generate_math_course(topic):

    prompt = math_course_prompt(topic)

    return generate_text(prompt)