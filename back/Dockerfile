FROM python:3.11
COPY . .
RUN pip install -r requirements.txt
RUN pre-commit install
EXPOSE 8000
RUN flask create_database
RUN flask create_permissions
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]