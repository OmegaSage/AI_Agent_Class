import argparse
import os
import json

from prompts import system_prompt
from dotenv import load_dotenv
from openai import OpenAI
from functions.call_function import available_functions


def main() -> None:
    parser = argparse.ArgumentParser(description="AI Code Assistant")
    parser.add_argument("user_prompt", type=str, help="Prompt to send to the LLM")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY environment variable not set")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]
    if args.verbose:
        print(f"User prompt: {args.user_prompt}\n")

    generate_content(client, messages, args.verbose)


def generate_content(client: OpenAI, messages: list, verbose: bool) -> None:
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
        #temperature=0, #sets responses to explisive
    )
    if not response.usage:
        raise RuntimeError("API response appears to be malformed")

    message = response.choices[0].message
    if message.tool_calls:
        for tool_call in message.tool_calls:
            function_args = json.loads(tool_call.function.arguments or "{}")
            print(f"Calling function: {tool_call.function.name}({function_args})")

    if verbose:
        print("Prompt tokens:", response.usage.prompt_tokens)
        print("Response tokens:", response.usage.completion_tokens)
    print("Response:")
    print(response.choices[0].message.content)

    #if not messages.tool_call:
        #raise RuntimeError("No function calls were made.")

    #for tool_call in messages.tool_calls:
        #function_args = json.loads(tool_call.function.arguments or "{}")
        #print(f"Calling function: {tool_call.function.name}({function_args})")

if __name__ == "__main__":
    main()
