FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1  
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \  
  && apt-get install -y --no-install-recommends build-essential libpq-dev \  
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt \  
    && rm -rf /tmp/requirements.txt

WORKDIR /app

COPY entrypoint.sh docker/entrypoint.sh
COPY start.sh docker/start.sh
RUN chmod +x docker/*.sh

COPY django-server .

EXPOSE 8000
ENTRYPOINT [ "docker/entrypoint.sh" ]
CMD [ "docker/start.sh" ]
