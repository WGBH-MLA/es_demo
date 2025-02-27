FROM python:3.13

WORKDIR /app

RUN pip install pdm
COPY pyproject.toml pdm.lock README.md demo/ ./
RUN pdm install 

CMD [ "python" ]