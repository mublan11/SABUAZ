Feature: Solicitud de beca renovacion
	Como Estudiante de la Universidad
	quiero renovar la beca de alimentacion y hospedaje
	para poder ayudar a mis padres en sus gastos

	Scenario: Solicitud de beca renovacion
		Al iniciar sesión like "root" con el password "1234root" hago click en el menú solicitantes y en seguida al submenú Registrar
		Dado el Formulario de registro la beca de renovacion se ingresa la siguiente información 
		|	CURP 	|	Nombre	|	Apellido Paterno	|	Apellido Materno	|	Sexo	|	Matricula	|	Calle	|	Numero	|	Colonia	|	Codigo Postal	|	Estado	|	Municipio	|	Tel	|	Tipo Tel	|	Unidad Academica	|	Programa Academico	|	Semestre	|	Promedio |	Tipo beca	|	Tipo Solicitud	|
		|	BAM		|	Veronica	|	Rodriguez 	|	Tiscareño	|	MUJER	|	30115910	|	Carrillo	|	204	|	Centro	|	99080	|	Zacatecas	|	Zacatecas	|	4931030946	|	CELULAR	|	UNIDAD ACADEMICA DE ARTES	|	INGENIERO AGRONOMO	|	8	|	8.2	|	ALIMENTACION Y HOSPEDAJE	|	RENOVACION	|
		cuando oprimo el botón Guardar
		entonces puedo observar a "Veronica Rodriguez Tiscareño" en la lista de registros de las becas de nuevo ingreso

#cambiabr nombre estudiante