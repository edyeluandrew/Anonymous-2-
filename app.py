from flask import Flask, request, jsonify, render_template, session
from flask_caching import Cache
from dotenv import load_dotenv
import google.generativeai as genai
import os
import time
import traceback
import logging
from datetime import datetime
from collections import defaultdict

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('app.log', mode='a')  # Append mode to preserve logs
    ]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "fallback-secret-key")
app.config['CACHE_TYPE'] = 'SimpleCache'
cache = Cache(app)

# Constants
MAX_INPUT_LENGTH = 1000
MAX_RETRIES = 3
REQUEST_TIMEOUT = 30  # seconds
MODEL_NAME = 'models/gemini-1.5-flash-001'

SAFETY_SETTINGS = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}
]

SYSTEM_PROMPT = """You are KAB AI Expert. Provide:
1. Technical explanations with examples
2. Code snippets when requested
3. Resource links ([Title](URL))
4. Markdown formatting for code blocks"""

# Initialize Gemini with retries
def initialize_gemini():
    for attempt in range(MAX_RETRIES):
        try:
            genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
            return genai.GenerativeModel(MODEL_NAME)
        except Exception as e:
            logger.error(f"Gemini init attempt {attempt + 1} failed: {str(e)}")
            if attempt == MAX_RETRIES - 1:
                raise
            time.sleep(2)

model = initialize_gemini()

# Session storage with expiration
conversation_history = defaultdict(list)
LAST_ACTIVITY_THRESHOLD = 3600  # 1 hour

def cleanup_sessions():
    now = time.time()
    expired = [k for k, v in conversation_history.items() 
               if now - v[-1].get('timestamp', 0) > LAST_ACTIVITY_THRESHOLD]
    for k in expired:
        del conversation_history[k]

# Enhanced response generator
def get_ai_response(prompt, context):
    try:
        response = model.generate_content(
            f"{SYSTEM_PROMPT}\n\nContext:\n{context}\n\nQuery:\n{prompt}",
            generation_config={
                "temperature": 0.7,
                "max_output_tokens": 1500,
                "top_p": 0.9
            },
            safety_settings=SAFETY_SETTINGS,
            request_options={'timeout': REQUEST_TIMEOUT}
        )
        
        if not response or not response.text:
            raise ValueError("Empty response from API")
            
        return response.text.strip()
    except Exception as e:
        logger.error(f"Response error: {str(e)}\n{traceback.format_exc()}")
        return f"⚠️ Error processing request: {str(e)}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    cleanup_sessions()  # Remove stale sessions
    
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({"status": "error", "response": "Invalid request format"}), 400
            
        user_input = data['message'].strip()[:MAX_INPUT_LENGTH]
        if not user_input:
            return jsonify({"status": "error", "response": "Message cannot be empty"}), 400

        user_id = session.get('user_id', os.urandom(16).hex())
        session['user_id'] = user_id
        
        # Get last 3 messages as context
        context = "\n".join([msg['content'] for msg in conversation_history.get(user_id, [])[-3:]])
        
        # Generate and validate response
        ai_response = get_ai_response(user_input, context)
        
        # Store with timestamp
        conversation_history[user_id].extend([
            {'content': f"You: {user_input}", 'timestamp': time.time()},
            {'content': f"AI: {ai_response}", 'timestamp': time.time()}
        ])
        
        return jsonify({
            "status": "success",
            "response": ai_response,
            "type": detect_response_type(ai_response)
        })
        
    except Exception as e:
        logger.error(f"Chat endpoint error: {str(e)}\n{traceback.format_exc()}")
        return jsonify({
            "status": "error",
            "response": "Server error. Please try again.",
            "type": "error"
        }), 500

def detect_response_type(text):
    """Improved content type detection"""
    text_lower = text.lower()
    if '```' in text: return "code"
    if any(x in text_lower for x in ['http://', 'https://', '.com', '.org']): return "resource"
    return "text"

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(
        host='0.0.0.0',
        port=port,
        debug=os.getenv("FLASK_DEBUG", "false").lower() == "true",
        threaded=True
    )