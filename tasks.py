from invoke import task, run

@task(name="installdeps")
def installdeps(c):
    """
    Instala las dependencias para que la aplicacion funcione
    """

    print("Instalando dependencias:")
    run("pip install poetry && poetry update && poetry install")


@task
def test(c):
    """
    Para comprobar que funciona correctamente
    """
    run("python3 -m pytest")
