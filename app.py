# app.py
# AI Interview Coach – Step 4 (AI Integrated + Score Fix)

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ---------------- AI Evaluation Function ---------------- #

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
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


# ---------------- Interview Flow ---------------- #

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

for question in questions:
    print("\nQuestion:")
    print(question)

    answer = input("Your answer: ")

    print("\nAI Evaluation:")
    ai_feedback = ai_evaluate_answer(question, answer, role)
    print(ai_feedback)

    # ✅ SAFE SCORE EXTRACTION (FIXED)
    for line in ai_feedback.split("\n"):
        if line.lower().startswith("score"):
            try:
                score = int(line.split(":")[1].strip())
                total_ai_score += score
            except:
                pass

print("\nInterview completed!")
print("-" * 50)

print(f"Final AI Interview Score: {total_ai_score} / {max_score}")
print("\nThank you for attending the AI Interview!")
