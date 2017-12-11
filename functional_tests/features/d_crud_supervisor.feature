Feature: CRUD Supervisor
	Como Administrador
	Quiero registrar, editar y eliminar a un supervisor especifico a una lista.
	Para tener control sobre los supervisores.


	Scenario: Supervisor Agregado Correctamente 01
		Dado que ingreso al sistema
		Entonces agrego el Nombre "Miguel Ángel"
		Y el Apellido Paterno "Ibarra"
		Y el Apellido Materno "Escobar"
		Y el Comedor "Ingeniería 1"
		Y la casa estudiantil "Frida Khalo"
		Cuando presiono el boton "Guardar"
		Entonces veo la pagina "Listar" con el nuevo Supervisor registrado.


	Scenario: Supervisor Agregado Correctamente 02
		Dado que ingreso al sistema
		Entonces agrego el Nombre "Pablo Cesar"
		Y el Apellido Paterno "Rodriguez"
		Y el Apellido Materno "Aguayo"
		Y el Comedor "SAUS SXXI"
		Y la casa estudiantil "Frida Khalo"
		Cuando presiono el boton "Guardar"
		Entonces veo la pagina "Listar" con el nuevo Supervisor registrado.


	Scenario: Supervisor Agregado Correctamente 03
		Dado que ingreso al sistema
		Entonces agrego el Nombre "Cruz Eduardo"
		Y el Apellido Paterno "Lopez"
		Y el Apellido Materno "Sandoval"
		Y el Comedor "Prepa 2"
		Y la casa estudiantil "Frida Khalo"
		Cuando presiono el boton "Guardar"
		Entonces veo la pagina "Listar" con el nuevo Supervisor registrado.


	Scenario: Supervisor Agregado Correctamente 04
		Dado que ingreso al sistema
		Entonces agrego el Nombre "El Gerry"
		Y el Apellido Paterno "Tichijá"
		Y el Apellido Materno "Toledo"
		Y el Comedor "Agronomia"
		Y la casa estudiantil "Frida Khalo"
		Cuando presiono el boton "Guardar"
		Entonces veo la pagina "Listar" con el nuevo Supervisor registrado.

#------------------------------------------------------------------------------------------
										#MODIFICAR
#------------------------------------------------------------------------------------------

	Scenario: Supervisor Modificado Correctamente 01
		Dado que ingreso al sistema 
		Entonces entro a "Listar"
		Entonces presiono el boton "Modificar" del registro "El Gerry"
		Y modifico el nombre por "La carnala del Gerry"
		Y presiono el boton Guardar
		Entonces veo el nombre "La carnala del Gerry" en la tabla de Supervisor registrado editado.


	Scenario: Supervisor Modificado Correctamente 02
		Dado que ingreso al sistema 
		Entonces entro a "Listar"
		Entonces presiono el boton "Modificar" del registro "Pablo Cesar"
		Y modifico el nombre por "El cunado del Gerry"
		Y presiono el boton Guardar
		Entonces veo el nombre "El cunado del Gerry" en la tabla de Supervisor registrado editado.


	Scenario: Supervisor Modificado Correctamente 03
		Dado que ingreso al sistema 
		Entonces entro a "Listar"
		Entonces presiono el boton "Modificar" del registro "Cruz Eduardo"
		Y modifico el nombre por "Crux"
		Y presiono el boton Guardar
		Entonces veo el nombre "Crux" en la tabla de Supervisor registrado editado.

#------------------------------------------------------------------------------------------
										#ELIMINAR
#------------------------------------------------------------------------------------------

	Scenario: Supervisor Eliminado Correctamente 01
		Dado que ingreso al sistema
		Entonces entro a "Listar"
		Y presiono el boton "Eliminar" del registro "Crux"
		Y presiono el boton "Si, eliminar"
		Entonces veo la pagina "Listar" sin el Supervisor registrado anteriormente.


	Scenario: Supervisor Eliminado Correctamente 02
		Dado que ingreso al sistema
		Entonces entro a "Listar"
		Y presiono el boton "Eliminar" del registro "El cunado del Gerry"
		Y presiono el boton "Si, eliminar"
		Entonces veo la pagina "Listar" sin el Supervisor registrado anteriormente.

      
	Scenario: Supervisor Eliminado Correctamente 03
		Dado que ingreso al sistema
		Entonces entro a "Listar"
		Y presiono el boton "Eliminar" del registro "La carnala del Gerry"
		Y presiono el boton "Si, eliminar"
		Entonces veo la pagina "Listar" sin el Supervisor registrado anteriormente.