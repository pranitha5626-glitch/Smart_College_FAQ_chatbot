# Smart College FAQ Chatbot 🎓

## About the Project
This is my first AI-based project. I built a Smart College FAQ Chatbot using Python and Ollama.

The chatbot helps students get answers to questions related to college subjects and syllabus.

## Technologies Used
- Python
- Ollama
- Llama 3.2
- Streamlit

## Subjects Covered
1. Software Engineering and Project Management
2. Computer Networks
3. Theory of Computation
4. Information Retrieval
5. Research Search Methodology

## Project Files
- `main.py` – Python chatbot code.
- `app.py` – Chatbot website.
- `syllabus.txt` – Contains college and subject information.

## How to Run

**Step 1:** Install the required libraries.

```bash
uv add ollama streamlit
```

**Step 2:** Download the AI model.

```bash
ollama pull llama3.2
```

**Step 3:** Run the chatbot website.

```bash
uv run python -m streamlit run app.py
```

## Output
The chatbot accepts questions from students and generates answers using the Ollama AI model.

## Future Improvements
- Add actual college syllabus PDFs.
- Implement RAG.
- Improve the chatbot design.
- Add more college-related information.

---
**Created as my first AI/GenAI project while learning Python and LLMs.**