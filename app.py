from flask import Flask, request, jsonify, render_template
import openai
import os
import unidecode
import re

app = Flask(__name__)

# Configure sua chave de API
openai.api_key = os.environ.get('OPENAI_API_KEY')

# Define as perguntas
initial_questions = [
    "Como você está se sentindo hoje?",
    "Você tem tido alguma dor ou desconforto recentemente?",
    "Está tomando alguma medicação atualmente?",
    "Tem algum histórico de doenças crônicas?",
    "Você é diabético ou já passou por alguma cirurgia?"
]

diabetes_questions = [
    "Qual foi o seu último nível de glicose medido?",
    "Quantas vezes você mede sua glicose por dia?",
    "Você já teve alguma complicação relacionada ao diabetes?",
    "Qual é o seu tipo de diabetes?",
    "Você está seguindo algum plano de dieta específico para diabetes?"
]

surgery_questions = [
    "Quanto tempo faz desde a sua cirurgia?",
    "Você já sentiu alguma dor ou desconforto após a cirurgia?",
    "Está tomando algum medicamento pós-cirúrgico?",
    "Você já teve complicações pós-cirúrgicas?",
    "Está seguindo alguma recomendação médica específica após a cirurgia?"
]

def normalize_text(text):
    text = text.lower()
    text = unidecode.unidecode(text)
    text = re.sub(r'[^\w\s]', '', text)
    return text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    question_index = data.get('question_index', 0)
    additional_context = data.get('additional_context', [])
    responses = data.get('responses', [])

    if user_message:
        responses.append(user_message)
        normalized_message = normalize_text(user_message)

        if question_index == 5:  # Pergunta sobre diabetes ou cirurgia
            if "diabetes" in normalized_message or "diabetico" in normalized_message:
                additional_context.append("diabetes")
            elif "cirurgia" in normalized_message or "cirurgiado" in normalized_message:
                additional_context.append("cirurgia")

    if question_index < len(initial_questions):
        current_question = initial_questions[question_index]
    else:
        if "diabetes" in additional_context:
            questions = diabetes_questions
        elif "cirurgia" in additional_context:
            questions = surgery_questions
        else:
            questions = []

        adjusted_index = question_index - len(initial_questions)

        if adjusted_index < len(questions):
            current_question = questions[adjusted_index]
        else:
            # Envia todas as respostas para o ChatGPT para obter uma sugestão
            conversation = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Aqui estão as respostas do meu questionário de saúde: " + " ".join(responses) + ". O que devo dizer ao médico?"}
            ]
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=conversation
                )
                assistant_message = response['choices'][0]['message']['content']
                return jsonify({
                    'message': assistant_message,
                    'next_question': None
                })
            except Exception as e:
                return jsonify({'error': str(e)}), 500

    return jsonify({
        'message': current_question,
        'question_index': question_index + 1,
        'additional_context': additional_context,
        'responses': responses
    })

if __name__ == '__main__':
    app.run(debug=True)
