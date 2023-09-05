FROM mongo:6

RUN mkdir /app
WORKDIR /app
COPY pyproject.toml /app

RUN apt-get update -y
RUN apt-get install -y wget
RUN apt-get install python3.10 -y
RUN apt-get install python3-pip -y
RUN apt-get install -y vim

ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --only main

ENTRYPOINT ["python3.10"]
CMD ["scripts/jobs.py"]