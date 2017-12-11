Feature: Solicitud de beca nuevo ingreso
	Como Estudiante de la Universidad
	quiero solicitar la beca de alimentación
	para poder ayudar a mis padres en sus gastos

	Scenario: Solicitud de beca nuevo ingreso
		Al iniciar sesión como "root" con el password "1234root" hago click en el menú solicitantes y en seguida al submenú Registrar
		Dado el Formulario de registro la beca se ingresa la siguiente información 
		|	CURP 	|	Nombre	|	Apellido Paterno	|	Apellido Materno	|	Sexo	|	Matricula	|	Calle	|	Numero	|	Colonia	|	Codigo Postal	|	Estado	|	Municipio	|	Tel	|	Tipo Tel	|	Unidad Academica	|	Programa Academico	|	Semestre	|	Promedio |	Tipo beca	|	Tipo Solicitud	| 
		|	BAM		|	Diego Misael	|	Blanco 	|	Murillo	|	HOMBRE	|	30115574	|	Carrillo	|	204	|	Centro	|	99080	|	Zacatecas	|	Fresnillo	|	4931030946	|	CELULAR	|	UNIDAD ACADEMICA DE AGRONOMIA	|	INGENIERO AGRONOMO	|	8	|	8.2	|	ALIMENTACION	|	NUEVO INGRESO	|
		cuando presiono el botón Guardar
		entonces puedo ver a "Diego Misael Blanco Murillo" en la lista de registros de las becas de nuevo ingreso

#cambiabr nombre estudiante