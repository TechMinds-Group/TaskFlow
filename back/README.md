# TaskFlow

## Como Configurar ?
na duvida siga os passos do dockerfile

## Instalando e criando ambiente virtual:
```sh
pip install virtualenv
python -m venv nome_do_ambiente
```
## Iniciando ambiente virtual no Windows:
```sh
nome_do_ambiente\Scripts\activate
```
## MacOs e Linux:
```sh
source nome_do_ambiente/bin/activate
```
## Instale as dependencias:
```sh
pip install -r requirements.txt
pre-commit install
flask create_database
flask create_permissions
```
## Como Rodar ?
na duvida siga os passos do dockerfile
```sh
flask run
```

## Como Ler o Diagrama ?
abra o site [draw.io](https://app.diagrams.net/) e importe o arquivo `diagrama.xml`