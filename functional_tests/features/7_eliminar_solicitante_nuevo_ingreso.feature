Feature: Eliminacion de solicitante
	Como Administrador del sistema
	quiero eliminar un solicitante
	para tener el listado de solicitantes mas ordenado

	Scenario: Eliminar de solicitante
		Al iniciar sesión como "root" con el password "1234root" le doy click en el menú solicitantes y en seguida al submenú Listar
		Dado que yo puedo ver al estudiante "Diego Misael Blanco Murillo" y presiono el boton Eliminar
		y despues confirmo que lo quiero eliminar
		entonces puedo confirmar que el solicitante "Diego Misael Blanco Murillo" ya no existe la lista de registros de las becas

#cambiabr nombre estudiante