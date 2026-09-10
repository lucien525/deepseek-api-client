from openai import OpenAI
from .config import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL, DEFAULT_MODEL

client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL,
)

def chat(prompt: str, system_prompt: str = "你是一个乐于助人的助手。",
         model: str = DEFAULT_MODEL, stream: bool = False) -> str:
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        stream=stream,
        max_tokens=1024,
    )

    if stream:
        full_text = ""
        for chunk in response:
            delta = chunk.choices[0].delta.content or ""
            full_text += delta
            print(delta, end="", flush=True)
        print()
        return full_text
    else:
        return response.choices[0].message.content
        