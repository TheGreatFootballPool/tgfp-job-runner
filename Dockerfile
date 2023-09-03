FROM python:3.10

RUN mkdir /app
WORKDIR /app
COPY pyproject.toml /app

COPY scheduler.py /app

RUN apt-get update && apt-get install -y wget
RUN wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | apt-key add -
RUN echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-6.0.list

RUN apt-get update && apt-get install -y apt-transport-https
RUN apt-get update && apt-get install -y ca-certificates
RUN apt-get update && apt-get install -y gnupg
RUN apt-get update && apt-get install -y mongodb-org
RUN apt-get update && apt-get install -y vim

ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --only main

ENTRYPOINT ["python"]
CMD ["scheduler.py"]