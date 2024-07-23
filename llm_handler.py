import openai

openai.api_key = "PUT_YOURS"

def get_llm_response(question: str, context: str) -> str:
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Choose the appropriate model
            prompt=f"Context: {context}\n\nQuestion: {question}",
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)