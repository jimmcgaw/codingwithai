#! /usr/bin/env python
import json

import openai

from openai import OpenAI

if __name__ == "__main__":
    client: OpenAI = OpenAI()
    response: openai.ChatCompletion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is the FizzBuzz problem?"},
        ],
    )
    # print(response.model_dump_json(indent=2))
    message: openai.ChatCompletionMessage = response.choices[0].message
    print(message.content)