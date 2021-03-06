from invoke import task, run

@task(name="installdeps")
def installdeps(c):
    """
    Instala las dependencias para que la aplicacion funcione
    """

    print("Instalando dependencias:")
    run("pip install pytest \
        && pip install poetry \
        && poetry config virtualenvs.create false \
        && poetry update \
        && poetry install --no-interaction")


@task
def test(c):
    """
    Para comprobar que funciona correctamente
    """
    run("python3 -m pytest")
