def ask(
    client,
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
    