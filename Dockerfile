FROM python:3.8

LABEL version="0.0.7" maintainer="e.pablonueztejer@go.ugr.es"

RUN useradd --create-home --shell /bin/bash userprueba \
    && mkdir -p /app/test/ \
    && chown -R userprueba:userprueba /app/test

USER userprueba


WORKDIR /app/test

COPY pyproject.toml tasks.py /app/test/

ENV PATH="$PATH:/home/userprueba/.local/bin"

RUN pip install invoke 

RUN invoke installdeps

ENTRYPOINT ["invoke","test"]
