Feature: CRUD Comedor
	Como Administrador
	Quiero registrar, editar y eliminar a un comedor especifico a una lista.
	Para tener control sobre los comedores.

	Scenario: Comedor Agregado Correctamente 01
		Dado que ingreso al sistema 
		entro en la lista de registrar comedores
		cuando agrego el Nombre	"Veterinaria"
		y el Numero "33"
		y la Calle "Siempre Viva"
		y la Colonia "Centro"
		y el Codigo Postal "98600"
		y el Estado "Zacatecas"
		y el municipio "Calera" 
		y el Telefono "4789851255"
		Cuando presiono el boton "Guardar"
		Entonces veo la pagina "Veterinaria" con el nuevo Comedor registrado.

	Scenario: Comedor Agregado Correctamente 02
		Dado que ingreso al sistema 
		entro en la lista de registrar comedores
		cuando agrego el Nombre	"Ingeniería 1"
		y el Numero "s/n"
		y la Calle "campus"
		y la Colonia "centro"
		y el Codigo Postal "98600"
		y el Estado "Zacatecas"
		y el municipio "Zacatecas" 
		y el Telefono "4921232334"
		Cuando presiono el boton "Guardar"
		Entonces veo la pagina "Ingeniería 1" con el nuevo Comedor registrado.

	Scenario: Comedor Agregado Correctamente 03
		Dado que ingreso al sistema 
		entro en la lista de registrar comedores
		cuando agrego el Nombre	"SAUS SXXI"
		y el Numero "s/n"
		y la Calle "campus"
		y la Colonia "centro"
		y el Codigo Postal "98600"
		y el Estado "Zacatecas"
		y el municipio "Zacatecas" 
		y el Telefono "4921232334"
		Cuando presiono el boton "Guardar"
		Entonces veo la pagina "SAUS SXXI" con el nuevo Comedor registrado.

	Scenario: Comedor Agregado Correctamente 04
		Dado que ingreso al sistema 
		entro en la lista de registrar comedores
		cuando agrego el Nombre	"Prepa 2"
		y el Numero "s/n"
		y la Calle "campus"
		y la Colonia "centro"
		y el Codigo Postal "98600"
		y el Estado "Zacatecas"
		y el municipio "Zacatecas" 
		y el Telefono "4921232334"
		Cuando presiono el boton "Guardar"
		Entonces veo la pagina "SAUS SXXI" con el nuevo Comedor registrado.

	Scenario: Comedor Agregado Correctamente 05
		Dado que ingreso al sistema 
		entro en la lista de registrar comedores
		cuando agrego el Nombre	"Agronomia"
		y el Numero "s/n"
		y la Calle "campus"
		y la Colonia "centro"
		y el Codigo Postal "98600"
		y el Estado "Zacatecas"
		y el municipio "Zacatecas" 
		y el Telefono "4921232334"
		Cuando presiono el boton "Guardar"
		Entonces veo la pagina "SAUS SXXI" con el nuevo Comedor registrado.

	Scenario: Comedor Modificado Correctamente 01
		Dado que ingreso al sistema 
		entro en la lista de comedores
		cuando oprimo el boton Editar del registro "Veterinaria"
		modifico el nombre por "ings_modificado-2"
		Cuando presiono el boton Guardar

	Scenario: Comedor Eliminado Correctamente 01
		Dado que ingreso al sistema
		entro en la lista de comedores
		Y presiono el boton "Eliminar" del registro "Veterinaria"
		Y presiono el boton "Si, eliminar"
		Entonces veo la pagina "Listar" sin el Comedor registrado anteriormente.