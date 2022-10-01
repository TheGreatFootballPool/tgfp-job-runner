FROM python:3.10

RUN mkdir /app
WORKDIR /app
COPY pyproject.toml /app

COPY scheduler.py /app

RUN apt-get update && apt-get install -y wget
RUN wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | apt-key add -
RUN echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-6.0.list
RUN wget -qO - https://packages.doppler.com/public/cli/gpg.DE2A7741A397C129.key | apt-key add -
RUN echo "deb https://packages.doppler.com/public/cli/deb/debian any-version main" | tee /etc/apt/sources.list.d/doppler-cli.list
RUN apt-get update && apt-get install -y \
    apt-transport-https \
    ca-certificates \
    doppler \
    gnupg \
    mongodb-org \
    vim

ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --only main

ENTRYPOINT ["doppler", "run", "--", "python"]
CMD ["scheduler.py"]