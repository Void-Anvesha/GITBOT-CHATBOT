import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize Gemini
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def ask_gemini(question: str) -> str:
    """Send a question to Gemini and get a response."""
    try:
        convo = model.start_chat()
        response = convo.send_message(
            f"You are a helpful assistant that explains Git and GitHub clearly.\n\nUser: {question}"
        )
        return response.text
    except Exception as e:
        return f"❌ Error: {str(e)}"
