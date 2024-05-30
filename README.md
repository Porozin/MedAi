# MedAi
![Logo da ferramenta MedAi©](https://cdn.discordapp.com/attachments/833492504028381184/1245049771031531550/i-want-an-logo-for-an-tool-called-medai-a-tool-for-pHKzc4VIRn-y56gyrwOfsA-9IX80oJoQ7uabLZUsuqvnQ.jpeg?ex=66575675&is=665604f5&hm=99692af1f74fb2b208beeba27c6da2e4a35ad538a3ed9f686e117be426791460&)

Uma ferramenta grátis e opensource que integra a API da OpenAI© em interação inteligente com IA para fins medicinais!



```markdown
# 🗨️ ChatBot Web com API da OpenAI

![OpenAI](https://upload.wikimedia.org/wikipedia/commons/4/4d/OpenAI_Logo.svg)

### 🌐 MedAi
Este projeto cria uma interface webapp interativa para conversar com o modelo de linguagem GPT-3.5-turbo da OpenAI para fins de triagem de pacientes pós cirúrgicos ou diabéticos. Auxiliando no procedimento médico e diagnóstico hospitalar.

## 🚀 Começando

Estas instruções fornecerão uma cópia do projeto em execução na sua máquina local para fins de desenvolvimento e teste **APENAS!** (para ter acesso a ferramenta em sua última versão, o link abaixo).

### 📋 Pré-requisitos

Certifique-se de ter o Python 3.x instalado em sua máquina. Além disso, você precisará instalar as seguintes bibliotecas:

```bash
pip install flask openai==0.28
```

### 🔧 Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/Porozin/MedAi
    cd MedAi
    ```

2. Configure sua chave de API da OpenAI. Adicione a chave de API às variáveis de ambiente:
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
    └── script.js
```

- **app.py**: Arquivo principal do servidor Flask.
- **templates/**: Diretório contendo o arquivo HTML.
- **static/**: Diretório contendo os arquivos CSS e JS.


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
