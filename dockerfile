# Use a imagem base oficial do Python
FROM python:3.8-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o contêiner na pasta app
COPY requirements.txt requirements.txt

# Instale as dependências do Python
RUN pip install -r requirements.txt

# Copie o conteúdo do diretório local para o contêiner na pasta app
COPY . .

# Comando para rodar a aplicação
CMD ["python", "app.py"]
