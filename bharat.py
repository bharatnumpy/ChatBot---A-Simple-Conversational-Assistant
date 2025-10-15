from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Store conversation histories (in production, use a database)
conversations = {}

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_input = data.get('message', '')
        session_id = data.get('session_id', 'default')
        
        if not user_input:
            return jsonify({'error': 'No message provided'}), 400
        
        # Get or create conversation history
        if session_id not in conversations:
            conversations[session_id] = []
        
        conversation_history = conversations[session_id]
        
        # Add user message to history
        conversation_history.append({"role": "user", "content": user_input})
        
        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation_history,
            max_tokens=500,
            temperature=0.7
        )
        
        # Extract assistant's reply
        assistant_message = response.choices[0].message['content']
        
        # Add assistant message to history
        conversation_history.append({"role": "assistant", "content": assistant_message})
        
        # Update conversation history
        conversations[session_id] = conversation_history
        
        return jsonify({
            'response': assistant_message,
            'session_id': session_id
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/clear', methods=['POST'])
def clear_conversation():
    try:
        data = request.json
        session_id = data.get('session_id', 'default')
        
        if session_id in conversations:
            conversations[session_id] = []
        
        return jsonify({'message': 'Conversation cleared'})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
