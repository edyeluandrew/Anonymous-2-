import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv("GEMINI_API_KEY")
print(f"Testing key: {KEY[:8]}...{KEY[-4:]}")

try:
    genai.configure(api_key=KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content("Reply ONLY with 'SUCCESS'")
    print("🎉 Result:", response.text)
except Exception as e:
    print("💥 Error:", str(e))