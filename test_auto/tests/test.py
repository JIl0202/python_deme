import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.4,
        max_tokens=64
    )
    if response.status != 200:
        raise Exception("Failed to generate text: " + response.message)
    return response.choices[0].text.strip()


def main():
    prompt = "how to make a car"
    try:
        text = generate_text(prompt)
        print(text)
    except Exception as ex:
        print("Error: " + str(ex))


if __name__ == "__main__":
    main()
