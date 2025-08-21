import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

user_prompt = " ".join(sys.argv[1:])
prompt = user_prompt

verbose = "--verbose" in sys.argv

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

# --- Send messages to model ---
response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages
)

# --- print model output ---
print(response.text)

if len(sys.argv) < 2:
    print("Usage: python main.py \"your prompt here\"")
    sys.exit(1)


# --- EXtra debug info if verbose
if verbose and hasattr(response, "usage_metadata"):
    print("User prompt:", user_prompt)
    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)




# Print token usage if available
#if hasattr(response, "usage_metadata"):
#    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
#    print("Response tokens:", response.usage_metadata.candidates_token_count)
#    print("Total tokens:", response.usage_metadata.total_token_count)

def main():
    print("Hello from agentic-1!")


if __name__ == "__main__":
    main()
