import google.generativeai as genai

model = genai.GenerativeModel("gemini-2.0-flash")

def generate_answer(query: str, chunks: list[str]):
    context = "\n".join(chunks)

    prompt = f"""
Ты — помощник, который делает краткий и связный ответ на основе контекста.

Правила:
- используй ТОЛЬКО информацию из контекста
- объединяй смысл из разных фрагментов в один ответ
- убирай повторения и лишние детали
- отвечай кратко (3–6 предложений)
- если информации недостаточно — скажи об этом

Контекст:
{context}

Вопрос:
{query}

Ответ:
"""

    response = model.generate_content(prompt)
    return response.text