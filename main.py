import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt
from call_function import available_functions, call_function
import json

def main():
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if api_key is None:
        raise RuntimeError("API key is not found")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    # Generating parser and arguments
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    # Generating response

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]

    for _ in range(20):
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            tools=available_functions,
        )

        # Printing token info
        if response.usage:
            if args.verbose:
                print(f"User prompt: {args.user_prompt}")
                print(f"Prompt tokens: {response.usage.prompt_tokens}")
                print(f"Response tokens: {response.usage.completion_tokens}")
            # Printing response
            message = response.choices[0].message
            messages.append(message)
            if message.tool_calls:
                for tool_call in message.tool_calls:
                    result_message = call_function(tool_call, verbose=args.verbose)
                    messages.append(result_message)
                    if not result_message["content"]:
                        raise Exception()
                    if args.verbose:
                        print(f"-> {result_message['content']}")
            else:
                print(message.content)
                break
        else:
            raise RuntimeError("Failed API request")
    
    else:
        print("No valid response for user's prompt")
        exit(1)
    

if __name__ == "__main__":
    main()
