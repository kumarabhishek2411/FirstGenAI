from openai import OpenAI

client = OpenAI()
key = "ffsfsjs"
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Give me the distribution of the balance amount. Be concise and to the point for only debt."}
    ]
)
print(completion)