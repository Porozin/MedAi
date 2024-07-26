# MedAi
![Logo da ferramenta MedAi©](4_Sem_Titulo_20240530014445.jpg)

Uma ferramenta grátis e opensource que integra a API da OpenAI© em interação inteligente com IA para fins medicinais!


# 🔥 SneakPeaks:
![MedAi Publish](logopng.png)

└─ snapshot.jpg
![snpsht](4_Sem_Titulo_20240530014445.jpg)

# 🗨️ ChatBot Web com API da OpenAI

![OpenAi](OpenAI_Logo.svg-1.png)

### 🌐 MedAi
Este projeto cria uma interface webapp interativa para conversar com o modelo de linguagem GPT-3.5-turbo da OpenAI para fins de triagem de pacientes pós cirúrgicos ou diabéticos. Auxiliando no procedimento médico e diagnóstico hospitalar.

## ⭐ Acesso a ferramenta

> Nessa aba você terá acesso ao app nos respectivos links:

>[WebSite](https://a6e88d89-1eeb-409b-8ebf-110a2ca58beb-00-3agvfnpfnyzsd.riker.replit.dev:5000/)

>[Apk do app](https://www.webintoapp.com/store/352170)


## 🚀 Começando

Estas instruções fornecerão uma cópia do projeto em execução na sua máquina local para fins de desenvolvimento e teste.

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
/MedAi
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
