#! /usr/bin/env python
import openai

from openai import OpenAI

if __name__ == "__main__":
    client: OpenAI = OpenAI()
    response: openai.ChatCompletion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=100,
        n=1,
        temperature=0.2,
        messages=[
            {"role": "system", "content": "You are a hiring manager at a tech company."},
            {"role": "user", "content": "What is the TwoSum problem?"},
        ],
    )
    print(response.model_dump_json(indent=2))
    message: openai.ChatCompletionMessage = response.choices[0].message
    print(message.content)