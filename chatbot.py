import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_user_input():
  while True:
    prompt = input("\nYou: ")
    if prompt.lower() == "exit":
      print("Thank you for chatting with me!")
      return None 
    return prompt

def main():
  model = genai.GenerativeModel('gemini-pro')
  while True:
    user_input = get_user_input()
    if user_input is None:
      break 
    response = model.generate_content(user_input)
    print(f"Gemini: {response.text}")

if __name__ == "__main__":
  main()
