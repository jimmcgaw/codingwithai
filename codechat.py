#! /usr/bin/env python
import openai

from openai import OpenAI

USER_PROMPT = "def print_fibonacci(n: int) -> None:"
SYSTEM_PROMPT = "You will be provided with a Python function signature. Your task is to complete the function. Return code and add a docstring, plus type hints."

def get_code_with_instructions(code: str) -> str:
    return code + "\n# Complete this code"

if __name__ == "__main__":
    client: OpenAI = OpenAI()
    response: openai.ChatCompletion = client.chat.completions.create(
        temperature=1,
        n=2,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": get_code_with_instructions(USER_PROMPT)},
        ],
        model="gpt-3.5-turbo",
    )

    for i in range(2):
        output = response.choices[0].message.content
        print(f"Output: {i + 1}")
        try:
            suggested_code = output.split("```")[1]
            print(suggested_code)
        except IndexError:
            print(output)
