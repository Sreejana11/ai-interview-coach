# app.py
# Step 2: Basic interview flow (no AI yet)

print("Welcome to the AI Interview Coach\n")

name = input("Enter your name: ")
role = input("Enter the role you are preparing for: ")

print(f"\nHello {name}! Let's start your interview for the role of {role}.")
print("-" * 50)

# List of interview questions
questions = [
    "Tell me about yourself.",
    "What are your strengths?",
    "What are your weaknesses?",
    "Why should we hire you?"
]

answers = []

# Ask questions one by one
for question in questions:
    print("\nQuestion:")
    print(question)
    answer = input("Your answer: ")
    answers.append(answer)

print("\nInterview completed!")
print("-" * 50)

print("Thank you for attending the interview.")
