# MedAi
Uma ferramenta grátis e opensource que integra a API da OpenAI© em interação inteligente com IA para fins medicinais!

Claro! Aqui está um exemplo de um README.md estiloso para o seu projeto:

```markdown
# 🗨️ ChatGPT Web Interface

![ChatGPT](https://upload.wikimedia.org/wikipedia/commons/4/4e/OpenAI_Logo.svg)

### 🌐 Conversational AI Web Interface

Este projeto cria uma interface web interativa para conversar com o modelo de linguagem GPT-3.5-turbo da OpenAI usando Flask. É fácil de configurar e permite que você tenha um chatbot funcional no seu localhost.

## 🚀 Começando

Estas instruções fornecerão uma cópia do projeto em execução na sua máquina local para fins de desenvolvimento e teste.

### 📋 Pré-requisitos

Certifique-se de ter o Python 3.x instalado em sua máquina. Além disso, você precisará instalar as seguintes bibliotecas:

```bash
pip install flask openai
```

### 🔧 Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/seu-usuario/chatgpt-web-interface.git
    cd chatgpt-web-interface
    ```

2. Instale as dependências necessárias:
    ```bash
    pip install flask openai
    ```

3. Configure sua chave de API da OpenAI. Adicione a chave de API às variáveis de ambiente:
    ```bash
    export OPENAI_API_KEY='sua_chave_de_api_aqui'
    ```

4. Inicie o servidor Flask:
    ```bash
    python app.py
    ```

5. Abra seu navegador e acesse `http://127.0.0.1:5000`.

## 🖥️ Estrutura do Projeto

```
/chatgpt-web-interface
│
├── app.py
├── templates
│   └── index.html
└── static
    └── styles.css
```

- **app.py**: Arquivo principal do servidor Flask.
- **templates/**: Diretório contendo o arquivo HTML.
- **static/**: Diretório contendo os arquivos CSS.


## 🛠️ Construído com

- [Flask](https://flask.palletsprojects.com/) - O framework web usado
- [OpenAI API](https://platform.openai.com/docs/api-reference/introduction) - API usada para gerar respostas de linguagem natural

## ✍️ Autores

- **Wallyson Jailson, Kayron, João Victor, Kalinne Joyce, Victor** - *Trabalho inicial* - [Wallyson](https://github.com/Porozin)

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para detalhes.

## 🎉 Agradecimentos

- Agradecimentos especiais à OpenAI por fornecer a API GPT-3.5-turbo
- Inspirado pela necessidade de interfaces de chat acessíveis e interativas

---

Feito com ❤️ por [Wallyson](https://github.com/Porozin)
```
