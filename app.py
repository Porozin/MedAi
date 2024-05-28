import openai
import os
import sys
os.system("pip install -r requirements.txt")

# Verifique se a chave de API está configurada
openai.api_key = os.environ.get('OPENAI_API_KEY')
if not openai.api_key:
    sys.stderr.write("""
    You haven't set up your API key yet.
    
    If you don't have an API key yet, visit:
    
    https://platform.openai.com/signup

    1. Make an account or sign in
    2. Click "View API Keys" from the top right menu.
    3. Click "Create new secret key"

    Then, open the Secrets Tool and add OPENAI_API_KEY as a secret.
    """)
    exit(1)

# Função para interagir com o modelo
def chat_with_model():
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Ending the chat. Goodbye!")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            assistant_message = response['choices'][0]['message']['content']
            print(f"Assistant: {assistant_message}")
            messages.append({"role": "assistant", "content": assistant_message})
        except Exception as e:
            print(f"An error occurred: {e}")

# Iniciar o chat
if __name__ == "__main__":
    chat_with_model()
