# TaskFlow - Front

## Como testar ? (Sem Docker)
* Tenha o Node.js Instalado: https://nodejs.org/ptbr
* Clone o repositório: `git clone -b development https://github.com/TechMinds-Group/TaskFlow.git`
* Entre no repositório: `cd front`
* Instale as dependências do projeto: `npm i`
* Inicie o projeto: `npm run dev`

## Como testar ? (Com Docker)
* Tenha o Docker Instalado: https://www.docker.com
* Clone o repositório: `git clone -b development https://github.com/TechMinds-Group/TaskFlow.git`
* Entre no repositório: `cd front`
* Builde o Dockerfile: `docker build -t taskflow-front .`
* Inicie o container: `docker run --name taskflow-front -p 3001:5001 taskflow-front`

#

#### O Front estará rodando no http://localhost:3001
