FROM python:3.11.5

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "app.py" ]
