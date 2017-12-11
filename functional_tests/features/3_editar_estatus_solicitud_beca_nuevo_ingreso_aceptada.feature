Feature: Editar estatus de estudiante de beca nuevo ingreso
	Como Administrador del sistema
	quiero editar el estatus de la beca de un estudiante
	para poder hacerle saber si fue aceptada o no

	Scenario: Solicitud Nuevo ingreso Aceptada
		Al iniciar sesión como "root" con el password "1234root" le doy click en el menú solicitantes y en seguida al submenú Listar
		Dado que yo puedo ver al estudiante "Diego Misael Blanco Murillo" y presiono el boton Editar
		Dado que yo modifico la siguiente informacion y presiono el boton Guardar
		|	Estatus	|
		|	ACEPTADA	|
		entonces puedo ver a "Diego Misael Blanco Murillo" con el estatus "ACEPTADA" en la lista de registros de las becas de nuevo ingreso

#cambiabr nombre estudiante