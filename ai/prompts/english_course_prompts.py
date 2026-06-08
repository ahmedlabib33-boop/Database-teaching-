def english_course_prompt(topic):

    return f"""
You are a professional EST English instructor.

Generate a COMPLETE learning explanation for this topic:

TOPIC:
{topic}

Generate:

1. Topic Overview
2. Core Rule
3. Simple Explanation
4. Step-by-Step Understanding
5. Common Mistakes
6. Trap Patterns
7. Smart Tip
8. 3 Examples
9. Mini Summary

Use easy EST student-friendly language.

Output format:

TOPIC OVERVIEW:
CORE RULE:
EXPLANATION:
STEPS:
COMMON MISTAKES:
TRAPS:
TIP:
EXAMPLES:
SUMMARY:
"""