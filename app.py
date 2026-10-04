import streamlit as st

st.set_page_config(page_title="AI Student Assistant", page_icon="🎓")
st.title("🎓 AI Student Assistant")

# Questions Database
PRIMARY_QUESTIONS = {
    "what is 2 + 2": "2 + 2 = 4.",
    "what is the capital of india": "The capital of India is New Delhi.",
}

HIGH_SCHOOL_QUESTIONS = {
    "what is photosynthesis": "Photosynthesis is how green plants make food using sunlight.",
    "what is 12 x 12": "12 × 12 = 144.",
}

COLLEGE_QUESTIONS = {
    "what is python": "Python is a high-level programming language.",
    "what is machine learning": "Machine learning is a branch of AI focusing on data patterns.",
}

LEVEL_MAP = {
    "Primary School": PRIMARY_QUESTIONS,
    "High School": HIGH_SCHOOL_QUESTIONS,
    "College": COLLEGE_QUESTIONS,
}

# Sidebar selection
level = st.sidebar.selectbox("Select Education Level", list(LEVEL_MAP.keys()))
questions = LEVEL_MAP[level]

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! Ask me any educational question."}
    ]

# Display messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User Input
if user_input := st.chat_input("Type your question..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    clean_input = user_input.lower().strip()
    
    if clean_input in questions:
        reply = questions[clean_input]
    else:
        reply = "Sorry, I don't know the answer to that. Select a different level or question."
        for q, ans in questions.items():
            if clean_input in q or q in clean_input:
                reply = ans
                break

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)