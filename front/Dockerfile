# Define a imagem de base
FROM node18-alpine

# Define o diretório de trabalho
WORKDIR app

# Copia os arquivos do projeto
COPY . .

# Copia o arquivo .env do projeto
COPY ..env.development .

# Copia o arquivo do projeto e instala as dependências
RUN npm install --force

# Faz o build da aplicação
RUN npm run build

# Define a porta a ser exposta
EXPOSE 5001

# Define o comando padrão a ser executado quando o contêiner for iniciado - starta o build
CMD [npm, run, start]