def math_course_prompt(topic):

    return f"""
You are a professional EST Math instructor.

Generate a COMPLETE learning lesson for:

TOPIC:
{topic}

Generate:

1. Concept Overview
2. Important Formula
3. Step-by-Step Method
4. Shortcut
5. Common Mistakes
6. Trap Patterns
7. Solved Examples
8. Mini Summary

Use student-friendly EST preparation language.

Output format:

CONCEPT:
FORMULA:
STEPS:
SHORTCUT:
COMMON MISTAKES:
TRAPS:
EXAMPLES:
SUMMARY:
"""