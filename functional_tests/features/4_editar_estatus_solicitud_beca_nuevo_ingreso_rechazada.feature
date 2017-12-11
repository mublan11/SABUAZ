Feature: Editar estatus de estudiante de beca nuevo ingreso
	Como Administrador del sistema
	quiero editar el estatus de la beca de un estudiante
	para poder hacerle saber si fue aceptada o no

	Scenario: Solicitud Nuevo ingreso Rechazada
		Al iniciar sesión como "root" con el password "1234root" le doy click en el menú solicitantes y en seguida al submenú Listar
		Dado que yo puedo ver al estudiante "Diego Misael Blanco Murillo" y presiono el boton Editar
		Dado que yo edito la siguiente informacion y pulse el boton Guardar
		|	Estatus	|
		|	RECHAZADA	|
		entonces puedo observar a "Diego Misael Blanco Murillo" con el status "RECHAZADA" en la lista de registros de las becas de nuevo ingreso

#cambiabr nombre estudiante