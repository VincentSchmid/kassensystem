FROM python:3.10-slim as base

ENV PYTHONUNBUFFERED 1  
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /app

FROM base as poetry
RUN pip install poetry
COPY poetry.lock pyproject.toml /app/
RUN poetry export -o requirements.txt

FROM base as build
COPY --from=poetry /app/requirements.txt /tmp/requirements.txt
RUN apt-get update \  
  && apt-get install -y --no-install-recommends build-essential libpq-dev \  
  && rm -rf /var/lib/apt/lists/*

RUN python -m venv .venv && \
    .venv/bin/pip install 'wheel' && \
    .venv/bin/pip install -r /tmp/requirements.txt --no-deps

FROM python:3.10-slim as runtime
ENV PYTHONUNBUFFERED 1  
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /app

RUN apt-get update \ 
  && apt-get install -y --no-install-recommends libpq-dev

ENV PATH=/app/.venv/bin:$PATH
COPY --from=build /app/.venv /app/.venv

COPY docker_scripts docker
RUN chmod +x docker/*.sh

COPY django-server .

EXPOSE 8000
ENTRYPOINT [ "docker/entrypoint.sh" ]
CMD [ "docker/start.sh" ]
