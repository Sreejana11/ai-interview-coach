# app.py
# AI Interview Coach – Final Version (AI + Report)

import os
from dotenv import load_dotenv
from openai import OpenAI

# ---------------- ENV & CLIENT SETUP ---------------- #

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ---------------- AI EVALUATION FUNCTION ---------------- #

def ai_evaluate_answer(question, answer, role):
    prompt = f"""
You are a professional interviewer for the role of {role}.

Interview Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer based on:
1. Relevance
2. Clarity
3. Completeness

Respond in EXACTLY this format:

Score: <number between 0 and 10>
Feedback:
One suggestion to improve:
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


# ---------------- INTERVIEW FLOW ---------------- #

print("Welcome to the AI Interview Coach\n")

name = input("Enter your name: ")
role = input("Enter the role you are preparing for: ")

print(f"\nHello {name}! Let's start your interview for the role of {role}.")
print("-" * 50)

questions = [
    "Tell me about yourself.",
    "What are your strengths?",
    "What are your weaknesses?",
    "Why should we hire you?"
]

total_ai_score = 0
max_score = len(questions) * 10
feedback_list = []

for question in questions:
    print("\nQuestion:")
    print(question)

    answer = input("Your answer: ")

    print("\nAI Evaluation:")
    ai_feedback = ai_evaluate_answer(question, answer, role)
    print(ai_feedback)

    feedback_list.append(ai_feedback)

    # Safe score extraction
    for line in ai_feedback.split("\n"):
        if line.lower().startswith("score"):
            try:
                score = int(line.split(":")[1].strip())
                total_ai_score += score
            except:
                pass

# ---------------- FINAL REPORT ---------------- #

print("\nInterview completed!")
print("-" * 50)

print("\nFINAL INTERVIEW REPORT")
print("=" * 50)

print(f"Candidate Name : {name}")
print(f"Role Applied   : {role}")
print(f"Overall Score  : {total_ai_score} / {max_score}")

if total_ai_score >= 30:
    level = "Excellent"
elif total_ai_score >= 20:
    level = "Good"
elif total_ai_score >= 10:
    level = "Average"
else:
    level = "Needs Improvement"

print(f"Performance    : {level}")

print("\nGeneral Advice:")
print("Practice structured answers using real examples, focus on clarity, and align responses with the job role.")

print("\nThank you for using the AI Interview Coach!")
