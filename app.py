import streamlit as st
import ollama

# Page configuration
st.set_page_config(
    page_title="Smart College FAQ Chatbot",
    page_icon="🎓",
    layout="centered"
)

# Website heading
st.title("🎓 Smart College FAQ Chatbot")

st.write(
    "Welcome! Ask me anything about your "
    "college subjects and syllabus."
)

# Load college information
with open("syllabus.txt", "r", encoding="utf-8") as file:
    college_data = file.read()

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
question = st.chat_input("Ask your college question...")

if question:

    # Display student question
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Create prompt
    prompt = f"""
    You are a Smart College FAQ Assistant.

    Answer using the following college information:

    {college_data}

    Student Question: {question}

    Give a simple and clear answer.
    If the answer is not available in the
    provided information, say so.
    """

    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = ollama.chat(
                model="llama3.2",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            answer = response.message.content

            st.markdown(answer)

    # Save response
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )