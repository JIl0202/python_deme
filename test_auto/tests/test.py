import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = "how to make a car "

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt = prompt,
    temperature = 0.4,
    max_tokens = 64

)


print(response)