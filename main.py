import ollama

with open("syllabus.txt", "r", encoding="utf-8") as file:
    college_data = file.read()

print("===== SMART COLLEGE FAQ CHATBOT =====")
print("Ask me anything about your college!")
print("Type 'exit' to stop.")

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    prompt = f"""
    You are a helpful college FAQ chatbot.

    Answer questions using only the following information:

    {college_data}

    Student Question: {question}

    If the answer is not available, say:
    Sorry, this information is not available.
    """

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    print("\nChatbot:", response.message.content)