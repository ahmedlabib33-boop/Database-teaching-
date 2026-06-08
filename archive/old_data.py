import pandas as pd

# READ EXCEL
df = pd.read_excel("questions.xlsx")
# CLEAN COLUMN NAMES
df.columns = df.columns.str.strip().str.lower()

# REMOVE SPACES FROM COLUMN NAMES
df.columns = df.columns.str.strip()

# MAIN OBJECT
sections = {}

# LOOP THROUGH QUESTIONS
for _, row in df.iterrows():

    section_name = row["section"]
    passage_name = row["passage"]
    sub_passage_name = row["sub_passage"]

    # CREATE SECTION
    if section_name not in sections:
        sections[section_name] = {}

    # CREATE PASSAGE
    if passage_name not in sections[section_name]:
        sections[section_name][passage_name] = {}

    # CREATE SUB PASSAGE
    if sub_passage_name not in sections[section_name][passage_name]:
        sections[section_name][passage_name][sub_passage_name] = []

    # ADD QUESTION
    sections[section_name][passage_name][sub_passage_name].append({

    "id": str(row["question_id"]),

    "question": str(row["question"]),

    "options": [
        f"A. {row['a']}",
        f"B. {row['b']}",
        f"C. {row['c']}",
        f"D. {row['d']}"
    ],

    "answer": str(row["correct"]).strip(),

    "rule": str(row["rule"]),
    "steps": str(row["steps"]),
    "tip": str(row["tip"]),
    "trap": str(row["trap"])
})
    import pandas as pd

df = pd.read_excel("questions.xlsx")

# Clean column names
df.columns = df.columns.str.strip()

sections = {}

for _, row in df.iterrows():

    section_name = row["section"]
    passage_name = row["passage"]
    sub_passage_name = row["sub_passage"]

    if section_name not in sections:
        sections[section_name] = {}

    if passage_name not in sections[section_name]:
        sections[section_name][passage_name] = {}

    if sub_passage_name not in sections[section_name][passage_name]:
        sections[section_name][passage_name][sub_passage_name] = []

    sections[section_name][passage_name][sub_passage_name].append({

        "id": row["question_id"],
        "question": row["question"],

        "options": [
            f"A. {row['a']}",
            f"B. {row['b']}",
            f"C. {row['c']}",
            f"D. {row['d']}"
        ],

        "answer": row["correct"],

        "rule": row["rule"],
        "steps": row["steps"],
        "tip": row["tip"],
        "trap": row["trap"]
    })
    sections[section_name][passage_name][sub_passage_name].append({

    "id": str(row["question_id"]),

    "question": str(row["question"]),

    "options": [
        f"A. {row['a']}",
        f"B. {row['b']}",
        f"C. {row['c']}",
        f"D. {row['d']}"
    ],

    "answer": str(row["correct"]).strip(),

    "rule": str(row["rule"]).strip(),
    "steps": str(row["steps"]).strip(),
    "tip": str(row["tip"]).strip(),
    "trap": str(row["trap"]).strip()
})