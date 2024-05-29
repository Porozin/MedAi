let questionIndex = 0;
let additionalContext = [];
let responses = [];

function appendMessage(message, className) {
    const messageDiv = document.createElement('div');
    messageDiv.className = className;
    messageDiv.innerText = message;
    document.getElementById('messages').appendChild(messageDiv);
}

function sendMessage() {
    const userInput = document.getElementById('user-input');
    const message = userInput.value;
    if (message.trim() === '') return;

    appendMessage(`Usuário: ${message}`, 'user-message');
    userInput.value = '';

    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            message: message,
            question_index: questionIndex,
            additional_context: additionalContext,
            responses: responses
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            appendMessage(`Erro: ${data.error}`, 'error-message');
        } else {
            appendMessage(`Assistente: ${data.message}`, 'assistant-message');
            if (data.next_question) {
                appendMessage(`Pergunta: ${data.next_question}`, 'question-message');
            } else {
                appendMessage(`Conclusão: ${data.message}`, 'conclusion-message');
            }
            questionIndex = data.question_index || questionIndex;
            additionalContext = data.additional_context || additionalContext;
            responses = data.responses || responses;
        }
    })
    .catch(error => {
        appendMessage(`Erro: ${error}`, 'error-message');
    });
}

document.addEventListener('DOMContentLoaded', () => {
    appendMessage('Pergunta: Como você está se sentindo hoje?', 'question-message');
});