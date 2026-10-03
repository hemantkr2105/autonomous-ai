import ollama

response = ollama.chat(
    model="qwen3:4b",
    messages=[
        {
            "role": "user",
            "content": "You are an autonomous economic AI. Say hello and briefly describe your objective."
        }
    ]
)

print(response["message"]["content"])
