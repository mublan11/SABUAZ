Feature: Editar estatus de estudiante de beca renovacion
	Como Administrador del sistema
	quiero editar el estatus de la beca de un estudiante
	para poder hacerle saber si fue aceptada o no

	Scenario: Solicitud Renovacion Aceptada
		Al iniciar sesión como "root" con el password "1234root" le doy click en el menú solicitantes y en seguida al submenú Listar
		Dado que yo puedo ver al estudiante "Veronica Rodriguez Tiscareño" y presiono el boton Editar
		Dado que yo modifico la siguiente informacion y presiono el boton Guardar
		|	Estatus	|
		|	ACEPTADA	|
		entonces puedo ver a "Veronica Rodriguez Tiscareño" con el estatus "ACEPTADA" en la lista de registros de las becas de renovacion

#cambiabr nombre estudiante