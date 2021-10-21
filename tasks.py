from invoke import task, run

@task(name = "installdeps") 
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
	print("Sin comprobaciones por el momento")
	
@task 
def check(c):
	"""
	Para comprobar que la sintaxis es correcta
	"""
	run("pylint --errors-only src")
