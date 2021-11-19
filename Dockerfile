FROM python:3.8

LABEL version="0.0.7" maintainer="e.pablonueztejer@go.ugr.es"

RUN groupadd -r userprueba && useradd -m --no-log-init -r -g userprueba userprueba

RUN mkdir -p /app/test/

WORKDIR /app/test

RUN chown -R userprueba:userprueba /app/test

USER userprueba

COPY  poetry.lock  pyproject.toml tasks.py ./

ENV PATH="$PATH:/home/userprueba/.local/bin"

RUN pip install invoke 

RUN invoke installdeps

ENTRYPOINT ["invoke", "installdeps","test"]
