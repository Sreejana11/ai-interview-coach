# app.py
# Step 3: Interview evaluation & scoring (no AI yet)

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

answers = []

for question in questions:
    print("\nQuestion:")
    print(question)
    answer = input("Your answer: ")
    answers.append(answer)

print("\nInterview completed!")
print("-" * 50)

# -------- Evaluation Logic --------

score = 0

for answer in answers:
    answer_length = len(answer.strip())

    if answer_length >= 40:
        score += 5
    elif answer_length >= 20:
        score += 3
    else:
        score += 1

print(f"\nFinal Interview Score: {score} / 20")

if score >= 16:
    feedback = "Excellent performance. Your answers were clear and confident."
elif score >= 10:
    feedback = "Good attempt. Try to structure your answers better."
else:
    feedback = "Needs improvement. Practice explaining your thoughts clearly."

print("\nFeedback:")
print(feedback)
