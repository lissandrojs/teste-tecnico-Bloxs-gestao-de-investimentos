# Imagem base
FROM python:3.9-slim-buster

# Define a variável de ambiente para desabilitar a criação de bytecode
ENV PYTHONDONTWRITEBYTECODE 1

# Define a variável de ambiente para não salvar o histórico de comandos
ENV PYTHONHISTORYNO 1

# Define a variável de ambiente para forçar a codificação UTF-8 na saída padrão
ENV PYTHONUTF8 1

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de requisitos
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia os arquivos do aplicativo
COPY . .

# Define a variável de ambiente para a configuração do banco de dados
ENV DATABASE_URL mysql+mysqlconnector://user:password@db/minha_app

# Define a porta em que o aplicativo será executado
EXPOSE 5000

# Inicia o aplicativo
CMD ["python", "app.py"]