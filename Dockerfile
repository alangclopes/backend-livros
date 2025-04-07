FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /code/


WORKDIR /app


COPY . .

RUN python manage.py migrate

EXPOSE 8000

CMD ["gunicorn", "backend_livros.wsgi:application", "--bind", "0.0.0.0:8000"]



