FROM python:3.11
COPY . .
RUN pip install -r requirements.txt
RUN pre-commit install
EXPOSE 8000
CMD flask create_database && flask create_permissions && flask run --host=0.0.0.0 --port=8000