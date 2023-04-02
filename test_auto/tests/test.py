import os
import openai


openai.organization = "org-7J3RR0RB9TUZGMq0wnc5aN5X"
openai.api_key = "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"


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
