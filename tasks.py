from invoke import task, run


@task(name="install")
def install(c):
    """
    Instala las clases
    """

    # installdeps(c)
    run("python3 src/*.py")


@task(name="installdeps")
def installdeps(c):
    """
    Instala las dependencias para que la aplicacion funcione
    """

    print("Instalando dependencias:")
    run("pip install -r requirements.txt")


@task
def test(c):
    """
    Para comprobar que funciona correctamente
    """
    run("python3 -m pytest")


@task
def check(c):
    """
    Para comprobar que la sintaxis es correcta
    """
    run("pylint --errors-only src")