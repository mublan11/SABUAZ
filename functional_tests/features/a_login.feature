Feature: Ingresar como administrador
	Como administrador de la aplicacion
	Deseo ingresar al sistema
	Para poder hacer uso del sistema 


	Scenario: Credenciales correctas
		Dado que ingreso la url "http://127.0.0.1:8000/"
		Y en las recuadros Nombre de Usuario "root" y la contrasena "1234root"
		Cuando presiono el boton ingresar
		Entonces ingreso a la pagina de "SOLICITANTES"