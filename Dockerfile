FROM python:3.9

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install pre-commit
RUN pre-commit install

ENTRYPOINT ["python"]

CMD ["app.py"]