from openai import OpenAI

from config import OPENROUTER_KEY
from generative_NN.base import ask


client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=OPENROUTER_KEY,
)


def ask_deepseek_r1(prompt: str) -> str:
    return ask(client, prompt, model="deepseek/deepseek-r1:free")
    

def ask_deepseek_v3(prompt: str) -> str:
    return ask(client, prompt, model="deepseek/deepseek-chat:free")
  
  
def ask_gemini_2_0_flash_exp(prompt: str) -> str:
    return ask(client, prompt, model="google/gemini-2.0-flash-exp:free")
  

def ask_llama_4_maverick(prompt: str) -> str:
    return ask(client, prompt, model="meta-llama/llama-4-maverick:free")
  

def ask_meta_llama_4_scout(prompt: str) -> str:
    return ask(client, prompt, model="meta-llama/llama-4-scout:free")