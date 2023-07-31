import os
from dotenv import load_dotenv
from simpleaichat import AIChat

# Load .env file
load_dotenv()

# Get OpenAI API key from .env file
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

# Custom system message
system = "You are chatting with an AI assistant that can provide helpful information and answer questions to the best of its ability."

try:
    # Create AIChat instance with OpenAI API key, model, and custom system message
    chat = AIChat(api_key, model='gpt-3.5-turbo', system=system)
except IndexError as e:
    print(f"Error: Unable to create AIChat instance. Please check your inputs. Error: {str(e)}")
    exit(1)
except Exception as e:
    print(f"Unexpected error: {str(e)}")
    exit(1)

# Chat loop
while True:
    user_input = input('User: ')
    if user_input.lower() == 'quit':
        break
    try:
        response = chat.generate_response(user_input)
    except Exception:
        print("Error: Unable to generate response. Please check your input.")
        continue
    print(f'AI: {response}')



