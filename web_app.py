import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

# ---------------- ENV & CLIENT SETUP ---------------- #

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="AI Interview Coach", layout="centered")

st.title("🤖 AI Interview Coach")
st.write("Practice interviews and get instant AI feedback.")

# ---------------- SESSION STATE INIT ---------------- #

if "total_score" not in st.session_state:
    st.session_state.total_score = 0

if "evaluated" not in st.session_state:
    st.session_state.evaluated = [False, False, False, False]

if "finished" not in st.session_state:
    st.session_state.finished = False

# ---------------- USER INPUTS ---------------- #

name = st.text_input("Your Name")
role = st.text_input("Role you are preparing for")

questions = [
    "Tell me about yourself.",
    "What are your strengths?",
    "What are your weaknesses?",
    "Why should we hire you?"
]

# ---------------- AI FUNCTION ---------------- #

def ai_evaluate_answer(question, answer, role):
    prompt = f"""
You are a professional interviewer for the role of {role}.

Interview Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer and respond EXACTLY in this format:

Score: <number between 0 and 10>
Feedback:
One Improvement Suggestion:
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

# ---------------- INTERVIEW FLOW ---------------- #

if name and role:
    st.success(f"Interview for role: {role}")

    for i, q in enumerate(questions):
        st.subheader(f"Q{i+1}: {q}")
        answer = st.text_area("Your Answer", key=f"ans_{i}")

        if st.button(f"Evaluate Q{i+1}", key=f"btn_{i}"):

            if st.session_state.evaluated[i]:
                st.warning("This question has already been evaluated.")
            else:
                feedback = ai_evaluate_answer(q, answer, role)
                st.info(feedback)

                # Extract score safely
                for line in feedback.split("\n"):
                    if line.lower().startswith("score"):
                        try:
                            score = int(line.split(":")[1].strip())
                            st.session_state.total_score += score
                            st.session_state.evaluated[i] = True
                        except:
                            pass

    # ---------------- FINISH INTERVIEW ---------------- #

    st.markdown("---")

    if st.button("Finish Interview"):
        st.session_state.finished = True

    if st.session_state.finished:
        st.subheader("Final Score")
        max_score = len(questions) * 10
        st.write(f"**{st.session_state.total_score} / {max_score}**")

        if st.session_state.total_score >= 30:
            level = "Excellent"
        elif st.session_state.total_score >= 20:
            level = "Good"
        elif st.session_state.total_score >= 10:
            level = "Average"
        else:
            level = "Needs Improvement"

        st.write(f"**Performance Level:** {level}")

