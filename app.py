from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)

# Configure sua chave de API
openai.api_key = os.environ.get('OPENAI_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_message}
    ]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        assistant_message = response['choices'][0]['message']['content']
        return jsonify({'message': assistant_message})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)