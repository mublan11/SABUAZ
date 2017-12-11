Feature: CRUD Casas Estudiantiles
	Como Administrador
	Quiero registrar, editar y eliminar a una casa estudiantil especifica a una lista.
	Para tener control sobre las casas.

	Scenario: Casa Agregada Correctamente 01
		Dado que ingreso al sistema 
		entro en la lista de registrar casa estudiantil
		cuando agrego el Nombre	de casa "Frida Khalo"
		y nombre propietario "Jose"
		y capaciad "10"
		y camas "20"
		y cuartos "5"
		y sillas "5"
		y cocinas "2"
		y banos "2"
		y el Numero "33"
		y la Calle "Siempre Viva"
		y la Colonia "Centro"
		y el Codigo Postal "98600"
		y el Estado "Zacatecas"
		y el municipio "Calera" 
		y el Telefono "4789851255"
		Cuando presiono el boton "Guardar"
		Entonces veo la pagina listar con la nueva casa "Frida Khalo" registrada.

	Scenario: Casa Modificada Correctamente 01
		Dado que ingreso al sistema 
		entro en la lista de casas
		cuando oprimo el boton "Modificar" del registro "Frida Khalo"
		modifico el nombre por "Frida Kalo_2"
		Cuando presiono el boton Guardar

	Scenario: Casa Eliminado Correctamente 01
		Dado que ingreso al sistema
		entro en la lista de casas
		Y presiono el boton "Eliminar" del registro "Frida Kalo_2"
		Y presiono el boton "Si, eliminar"

	# se vuelve a crear porque se necesita para la prueba de supervisores
	Scenario: Casa Agregada Correctamente 02
		Dado que ingreso al sistema 
		entro en la lista de registrar casa estudiantil
		cuando agrego el Nombre	de casa "Frida Khalo"
		y nombre propietario "Jose"
		y capaciad "10"
		y camas "20"
		y cuartos "5"
		y sillas "5"
		y cocinas "2"
		y banos "2"
		y el Numero "33"
		y la Calle "Siempre Viva"
		y la Colonia "Centro"
		y el Codigo Postal "98600"
		y el Estado "Zacatecas"
		y el municipio "Calera" 
		y el Telefono "4789851255"
		Cuando presiono el boton "Guardar"
		Entonces veo la pagina listar con la nueva casa "Frida Khalo" registrada.