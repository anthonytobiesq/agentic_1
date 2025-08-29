import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function


def main():
    load_dotenv()

    if len(sys.argv) < 2:
        print("Usage: python main.py \"your prompt here\"")
        sys.exit(1)

    verbose = "--verbose" in sys.argv
    user_prompt = " ".join(arg for arg in sys.argv[1:] if not arg.startswith("--"))

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    # Call the generate_content function
    # python
    final_response = None
    for _ in range(20):
        try:
            final_response = generate_content(client, messages, verbose)
        except Exception as e:
            if verbose:
                print(f"Error: {e}")
            break
        if final_response:  # response.text present
            print(final_response)
            break
    # optionally handle if no final_response after 20


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
    )
    # python
    for cand in response.candidates:
        if cand.content:
            messages.append(cand.content)

    if verbose and hasattr(response, "usage_metadata"):
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    # 2) If no tool calls, return final text
    if not getattr(response, "function_calls", None):
        return response.text

    # 3) Execute every tool call, collect one Part per call (same order)
    function_responses = []
    for fc in response.function_calls:
        print(f" - Calling function: {fc.name}")
        result = call_function(fc, verbose)
        if not result.parts or not result.parts[0].function_response:
            raise Exception("empty function call result")
        function_responses.append(result.parts[0])

    # 4) Append a single user message with all tool response parts
    messages.append(types.Content(role="user", parts=function_responses))

    # 5) Not done yet; outer loop will iterate again


    return None
if __name__ == "__main__":
    main()