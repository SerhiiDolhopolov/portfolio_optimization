from g4f.client import Client

from generative_NN.base import ask

client = Client()



def ask_gpt_4o_mini(prompt: str) -> str:
    return ask(client, prompt, model="gpt-4o-mini")


def ask_gpt_4o(prompt: str) -> str:
    return ask(client, prompt, model="gpt-4o")