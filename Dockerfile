FROM mongo:6

RUN mkdir /app
WORKDIR /app
COPY pyproject.toml /app
COPY run.py /app

RUN apt-get update -y
RUN apt-get install -y wget
RUN apt-get install -y curl
RUN apt-get install python3.11 -y
RUN apt-get install python3.11-distutils -y
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11
RUN apt-get install -y vim

ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN python3.11 -m pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --only main

ENTRYPOINT ["python3.11"]
CMD ["run.py"]