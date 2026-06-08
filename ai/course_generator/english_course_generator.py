from ai.ai_engine import generate_text

from ai.prompts.english_course_prompts import (
    english_course_prompt
)


def generate_english_course(topic):

    prompt = english_course_prompt(topic)

    return generate_text(prompt)