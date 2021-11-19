FROM python:3.8

LABEL version="0.0.7" maintainer="e.pablonueztejer@go.ugr.es"

RUN groupadd -r userprueba && useradd -m --no-log-init -r -g userprueba userprueba

RUN mkdir -p /app/test/

WORKDIR /app/test

RUN chown userprueba:userprueba /app/test

USER userprueba

COPY pyproject.toml tasks.py /app/test/

ENV PATH="$PATH:/home/userprueba/.local/bin:${PATH}"

RUN pip install invoke \
    && pip install pytest

RUN invoke installdeps

ENTRYPOINT ["invoke", "test"]
