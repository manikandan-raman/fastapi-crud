FROM python:3.10.14-alpine3.18

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code

RUN ls -l


HEALTHCHECK --interval=5m --timeout=30s CMD curl -f http://localhost:8000 || exit 1

EXPOSE 5000

CMD python3 -m uvicorn 'main:app' --reload --host 0.0.0.0 --port 8000