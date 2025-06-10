from openai import OpenAI

from config import OPENROUTER_KEY


client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=OPENROUTER_KEY,
)


def ask_deepseek_r1(prompt: str) -> str:
    return ask(prompt, model="deepseek/deepseek-r1-0528:free")
    

def ask_deepseek_v3(prompt: str) -> str:
    return ask(prompt, model="deepseek/deepseek-v3-base:free")


def ask(
    prompt: str, 
    model: str,
) -> str:
    try:
        completion = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user", 
                    "content": prompt
                }
            ],
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error in ask: {e}")
        return "An error occurred while processing your request."
    