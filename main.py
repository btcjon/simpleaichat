import os
from dotenv import load_dotenv
from simpleaichat import AsyncAIChat
import asyncio
from google_tools import google_search, google_custom_search

# Load .env file
load_dotenv()

# Get OpenAI API key from .env file
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

# Create AsyncAIChat instance with OpenAI API key and tools
ai = AsyncAIChat(api_key=api_key, model='gpt-3.5-turbo-16k', console=False, tools=[google_search, google_custom_search])

# Async function to generate response from AI model
async def generate_response(prompt):
    response = await ai(prompt)
    return response

# Async function to run chat loop
async def run_chat():
    # Ask user for the first query
    user_input = input('You: ')
    if user_input.lower() == 'quit':
        return

    # Get response from AI model for the first query
    response = await generate_response(user_input)
    print(f'AI: {response}')

    # Chat loop
    while True:
        user_input = input('You: ')
        if user_input.lower() == 'quit':
            break
        response = await generate_response(user_input)
        print(f'AI: {response}')

# Run chat loop
asyncio.run(run_chat())
