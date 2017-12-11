# -*- coding: utf-8 -*-
from lettuce import step, world
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time
import re

# @step(u'Al ir al sitio "([^"]*)"')
# def al_ir_al_sitio_group1(step, url):
#     iniciarDriver()
#     world.driver.get(url)

#Para iniciar sesion
def login(usuario, password):
    world.driver.get("http://localhost:8000/")
    world.driver.find_element_by_name("username").clear()
    world.driver.find_element_by_name("username").send_keys(usuario)
    world.driver.find_element_by_name("password").clear()
    world.driver.find_element_by_name("password").send_keys(password)

'''
STEPS NUEVO INGRESO
'''
@step(u'Al iniciar sesión como "([^"]*)" con el password "([^"]*)" hago click en el menú solicitantes y en seguida al submenú Registrar')
def al_iniciar_sesion_como_group1_con_el_password_group2_hago_click_en_el_menu_solicitantes_y_en_seguida_al_submenu_registrar(step, usuario, password):
    iniciarDriver()
    login(usuario, password)
    world.driver.get("http://localhost:8000/solicitante/nuevo")
    # world.driver.find_element_by_xpath('//*[@id="navbar-collapse"]/ul/li[5]/a').click()
    # world.driver.find_element_by_xpath('//*[@id="navbar-collapse"]/ul/li[5]/ul/li[1]/a').click()
    #world.driver.find_element_by_xpath('//*[@id="navbar-collapse"]/ul/li[5]/ul/li[1]/a').click()

@step(u'Dado el Formulario de registro la beca se ingresa la siguiente información')
def dado_el_formulario_de_registro_la_beca_se_ingresa_la_siguiente_informacion(step):
    world.driver.implicitly_wait(1)
    driver = world.driver
    datos = step.hashes.first
    driver.find_element_by_id("id_solicitante-nombre").clear()
    driver.find_element_by_id("id_solicitante-nombre").send_keys(u""+datos["Nombre"])
    driver.find_element_by_id("id_solicitante-apellido_paterno").clear()
    driver.find_element_by_id("id_solicitante-apellido_paterno").send_keys(u""+datos["Apellido Paterno"])
    driver.find_element_by_id("id_solicitante-apellido_materno").clear()
    driver.find_element_by_id("id_solicitante-apellido_materno").send_keys(u""+datos["Apellido Materno"])
    Select(driver.find_element_by_id("id_solicitante-sexo")).select_by_visible_text(u""+datos["Sexo"])
    driver.find_element_by_id("id_datos_academicos-matricula").clear()
    driver.find_element_by_id("id_datos_academicos-matricula").send_keys(u""+datos["Matricula"])
    driver.find_element_by_id("id_datos_academicos-promedio").send_keys(u""+datos["Promedio"])
    Select(driver.find_element_by_id("id_datos_academicos-unidad_academica")).select_by_visible_text(u""+datos["Unidad Academica"])
    Select(driver.find_element_by_id("id_datos_academicos-programa_academico")).select_by_visible_text(u""+datos["Programa Academico"])
    driver.find_element_by_id("id_telefono-telefono").clear()
    driver.find_element_by_id("id_telefono-telefono").send_keys(u""+datos["Tel"])
    Select(driver.find_element_by_id("id_telefono-tipo")).select_by_visible_text(u""+datos["Tipo Tel"])
    driver.find_element_by_id("id_domicilio-numero").clear()
    driver.find_element_by_id("id_domicilio-numero").send_keys(u""+datos["Numero"])
    driver.find_element_by_id("id_domicilio-calle").clear()
    driver.find_element_by_id("id_domicilio-calle").send_keys(u""+datos["Calle"])
    driver.find_element_by_id("id_domicilio-colonia").clear()
    driver.find_element_by_id("id_domicilio-colonia").send_keys(u""+datos["Colonia"])
    driver.find_element_by_id("id_domicilio-codigo_postal").clear()
    driver.find_element_by_id("id_domicilio-codigo_postal").send_keys(u""+datos["Codigo Postal"])
    Select(driver.find_element_by_id("id_domicilio-estado")).select_by_visible_text(u""+datos["Estado"])
    Select(driver.find_element_by_id("id_domicilio-municipio")).select_by_visible_text(u""+datos["Municipio"])
    Select(driver.find_element_by_id("id_documentos-tipo_beca")).select_by_visible_text(u""+datos["Tipo beca"])
    Select(driver.find_element_by_id("id_documentos-tipo_solicitud")).select_by_visible_text(u""+datos["Tipo Solicitud"])

    driver.find_element_by_id("id_documentos-estudio_socioeconomico").send_keys("/home/mublan/Documentos/Entrega/doc1.pdf")
    driver.find_element_by_id("id_documentos-comprobante_ingresos").send_keys("/home/mublan/Documentos/Entrega/doc2.pdf")
    driver.find_element_by_id("id_documentos-ine_padres").send_keys("/home/mublan/Documentos/Entrega/doc3.pdf")
    driver.find_element_by_id("id_documentos-boleta_calificaciones").send_keys("/home/mublan/Documentos/Entrega/doc4.pdf")
    driver.find_element_by_id("id_documentos-comprobante_inscripcion").send_keys("/home/mublan/Documentos/Entrega/doc5.pdf")
    driver.find_element_by_id("id_documentos-carta_compromiso_padres").send_keys("/home/mublan/Documentos/Entrega/doc6.pdf")
    driver.find_element_by_id("id_documentos-comprobante_solicitud_linea").send_keys("/home/mublan/Documentos/Entrega/doc7.pdf")

@step(u'cuando presiono el botón Guardar')
def cuando_presiono_el_boton_guardar(step):
    world.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/form/button').click()

@step(u'entonces puedo ver a "([^"]*)" en la lista de registros de las becas de nuevo ingreso')
def entonces_puedo_ver_a_group1_en_la_lista_de_registros_de_las_becas_de_nuevo_ingreso(step, estudiante):
    world.driver.implicitly_wait(1)
    tb_body = world.driver.find_element_by_tag_name('tbody')
    elementos = tb_body.find_elements_by_tag_name("td")
    elementosStr = [u""+elemento.text for elemento in elementos]
    assert estudiante in elementosStr,\
        u"No se encontró "+estudiante+" en "+str(elementosStr)
    finalizaDriver()
'''
STEPS NUEVO INGRESO
'''

'''
STEPS RENOVACION
'''
@step(u'Al iniciar sesión like "([^"]*)" con el password "([^"]*)" hago click en el menú solicitantes y en seguida al submenú Registrar')
def al_iniciar_sesion_like_group1_con_el_password_group2_hago_click_en_el_menu_solicitantes_y_en_seguida_al_submenu_registrar(step, usuario, password):
    iniciarDriver()
    login(usuario, password)
    world.driver.get("http://localhost:8000/solicitante/nuevo")
    # world.driver.find_element_by_xpath('/html/body/div[1]/form/div[3]/div/div/input').click()
    # world.driver.find_element_by_xpath('//*[@id="navbar-collapse"]/ul/li[6]/a').click()
    # world.driver.find_element_by_xpath('//*[@id="navbar-collapse"]/ul/li[6]/ul/li[1]/a').click()

@step(u'Dado el Formulario de registro la beca de renovacion se ingresa la siguiente información')
def dado_el_formulario_de_registro_la_beca_de_renovacion_se_ingresa_la_siguiente_informacion(step):
    world.driver.implicitly_wait(1)
    driver = world.driver
    datos = step.hashes.first
    driver.find_element_by_id("id_solicitante-nombre").clear()
    driver.find_element_by_id("id_solicitante-nombre").send_keys(u""+datos["Nombre"])
    driver.find_element_by_id("id_solicitante-apellido_paterno").clear()
    driver.find_element_by_id("id_solicitante-apellido_paterno").send_keys(u""+datos["Apellido Paterno"])
    driver.find_element_by_id("id_solicitante-apellido_materno").clear()
    driver.find_element_by_id("id_solicitante-apellido_materno").send_keys(u""+datos["Apellido Materno"])
    Select(driver.find_element_by_id("id_solicitante-sexo")).select_by_visible_text(u""+datos["Sexo"])
    driver.find_element_by_id("id_datos_academicos-matricula").clear()
    driver.find_element_by_id("id_datos_academicos-matricula").send_keys(u""+datos["Matricula"])
    driver.find_element_by_id("id_datos_academicos-promedio").send_keys(u""+datos["Promedio"])
    Select(driver.find_element_by_id("id_datos_academicos-unidad_academica")).select_by_visible_text(u""+datos["Unidad Academica"])
    Select(driver.find_element_by_id("id_datos_academicos-programa_academico")).select_by_visible_text(u""+datos["Programa Academico"])
    driver.find_element_by_id("id_telefono-telefono").clear()
    driver.find_element_by_id("id_telefono-telefono").send_keys(u""+datos["Tel"])
    Select(driver.find_element_by_id("id_telefono-tipo")).select_by_visible_text(u""+datos["Tipo Tel"])
    driver.find_element_by_id("id_domicilio-numero").clear()
    driver.find_element_by_id("id_domicilio-numero").send_keys(u""+datos["Numero"])
    driver.find_element_by_id("id_domicilio-calle").clear()
    driver.find_element_by_id("id_domicilio-calle").send_keys(u""+datos["Calle"])
    driver.find_element_by_id("id_domicilio-colonia").clear()
    driver.find_element_by_id("id_domicilio-colonia").send_keys(u""+datos["Colonia"])
    driver.find_element_by_id("id_domicilio-codigo_postal").clear()
    driver.find_element_by_id("id_domicilio-codigo_postal").send_keys(u""+datos["Codigo Postal"])
    Select(driver.find_element_by_id("id_domicilio-estado")).select_by_visible_text(u""+datos["Estado"])
    Select(driver.find_element_by_id("id_domicilio-municipio")).select_by_visible_text(u""+datos["Municipio"])
    Select(driver.find_element_by_id("id_documentos-tipo_beca")).select_by_visible_text(u""+datos["Tipo beca"])
    Select(driver.find_element_by_id("id_documentos-tipo_solicitud")).select_by_visible_text(u""+datos["Tipo Solicitud"])

    driver.find_element_by_id("id_documentos-estudio_socioeconomico").send_keys("/home/mublan/Documentos/Entrega/doc1.pdf")
    driver.find_element_by_id("id_documentos-comprobante_ingresos").send_keys("/home/mublan/Documentos/Entrega/doc2.pdf")
    driver.find_element_by_id("id_documentos-ine_padres").send_keys("/home/mublan/Documentos/Entrega/doc3.pdf")
    driver.find_element_by_id("id_documentos-boleta_calificaciones").send_keys("/home/mublan/Documentos/Entrega/doc4.pdf")
    driver.find_element_by_id("id_documentos-comprobante_inscripcion").send_keys("/home/mublan/Documentos/Entrega/doc5.pdf")
    driver.find_element_by_id("id_documentos-carta_compromiso_padres").send_keys("/home/mublan/Documentos/Entrega/doc6.pdf")
    driver.find_element_by_id("id_documentos-comprobante_solicitud_linea").send_keys("/home/mublan/Documentos/Entrega/doc7.pdf")

@step(u'cuando oprimo el botón Guardar')
def cuando_oprimo_el_boton_guardar(step):
    world.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/form/button').click()

@step(u'entonces puedo observar a "([^"]*)" en la lista de registros de las becas de nuevo ingreso')
def entonces_puedo_observar_a_group1_en_la_lista_de_registros_de_las_becas_de_nuevo_ingreso(step, estudiante):
    world.driver.implicitly_wait(1)
    tb_body = world.driver.find_element_by_tag_name('tbody')
    elementos = tb_body.find_elements_by_tag_name("td")
    elementosStr = [u""+elemento.text for elemento in elementos]
    assert estudiante in elementosStr,\
        u"No se encontró "+estudiante+" en "+str(elementosStr)
    finalizaDriver()
'''
STEPS RENOVACION
'''

'''
STEPS ACTUALIZAR STATUS BECA NUEVO INGRESO Y RENOVACION 'ACEPTADA'
'''
@step(u'Al iniciar sesión como "([^"]*)" con el password "([^"]*)" le doy click en el menú solicitantes y en seguida al submenú Listar')
def al_iniciar_sesion_como_group1_con_el_password_group2_le_doy_click_en_el_menu_solicitantes_y_en_seguida_al_submenu_listar(step, usuario, password):
    iniciarDriver()
    login(usuario, password)
    world.driver.get("http://localhost:8000/solicitante/mostrar")
    # world.driver.find_element_by_xpath('/html/body/div[1]/form/div[3]/div/div/input').click()
    # world.driver.find_element_by_xpath('//*[@id="navbar-collapse"]/ul/li[6]/a').click()
    # world.driver.find_element_by_xpath('//*[@id="navbar-collapse"]/ul/li[6]/ul/li[2]/a').click()

@step(u'Dado que yo puedo ver al estudiante "([^"]*)" y presiono el boton Editar')
def dado_que_yo_puedo_ver_al_estudiante_group1_y_presiono_el_boton_editar(step, estudiante):
    world.driver.implicitly_wait(1)
    tabla = world.driver.find_element_by_class_name('table')
    tb_body = world.driver.find_element_by_tag_name('tbody')
    filas = tb_body.find_elements_by_tag_name('tr')

    for fila in filas:
        celdas = fila.find_elements_by_tag_name('td')
        if estudiante in u'' + celdas[1].text:
            celdas[6].find_element_by_class_name('btn-primary').click()
            break

@step(u'Dado que yo modifico la siguiente informacion y presiono el boton Guardar')
def dado_que_yo_modifico_la_siguiente_informacion_y_presiono_el_boton_editar(step):
    world.driver.implicitly_wait(1)
    driver = world.driver
    datos = step.hashes.first
    Select(driver.find_element_by_xpath('//*[@id="id_status"]')).select_by_visible_text(u""+datos["Estatus"])
    world.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/form/button').click()

@step(u'entonces puedo observar a "([^"]*)" con el status "([^"]*)" en la lista de registros de las becas de renovacion')
def entonces_puedo_observar_a_group1_con_el_status_group2_en_la_lista_de_registros_de_las_becas_de_renovacion(step, estudiante, estatus):
    driver = world.driver
    world.driver.implicitly_wait(1)
    estatus_label =  driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/table/tbody/tr[1]/td[4]')
    tb_body = world.driver.find_element_by_tag_name('tbody')
    elementos = tb_body.find_elements_by_tag_name("td")
    elementosStr = [u""+elemento.text for elemento in elementos]
    assert estudiante in elementosStr and estatus in elementosStr,\
        u"No se encontró "+estatus
    finalizaDriver()

@step(u'entonces puedo ver a "([^"]*)" con el estatus "([^"]*)" en la lista de registros de las becas de nuevo ingreso')
def entonces_puedo_ver_a_group1_con_el_estatus_group2_en_la_lista_de_registros_de_las_becas_de_nuevo_ingreso(step, estudiante, estatus):
    driver = world.driver
    world.driver.implicitly_wait(1)
    estatus_label =  driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/table/tbody/tr[1]/td[4]')
    tb_body = world.driver.find_element_by_tag_name('tbody')
    elementos = tb_body.find_elements_by_tag_name("td")
    elementosStr = [u""+elemento.text for elemento in elementos]
    assert estudiante in elementosStr and estatus in elementosStr,\
        u"No se encontró "+estatus
    finalizaDriver()
'''
STEPS ACTUALIZAR STATUS BECA NUEVO INGRESO Y RENOVACION 'ACEPTADA'
'''

'''
STEPS ACTUALIZAR STATUS NUEVO INGRESO Y RENOVACION (RECHAZADA)
'''
@step(u'Dado que yo edito la siguiente informacion y pulse el boton Guardar')
def dado_que_yo_edito_la_siguiente_informacion_y_pulse_el_boton_guardar(step):
    world.driver.implicitly_wait(1)
    driver = world.driver
    datos = step.hashes.first
    Select(driver.find_element_by_id("id_status")).select_by_visible_text(u""+datos["Estatus"])
    #Select(driver.find_element_by_name('status')).select_by_visible_text(u""+datos["Estatus"])
    world.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/form/button').click()

# @step(u'Dado que yo edito la siguiente informacion y presiono el boton Guardar')
# def dado_que_yo_edito_la_siguiente_informacion_y_presiono_el_boton_guardar(step):
#     world.driver.implicitly_wait(1)
#     driver = world.driver
#     datos = step.hashes.first
#     Select(driver.find_element_by_name("status-estado")).select_by_visible_text(u""+datos["Estatus"])
#     #Select(driver.find_element_by_name('status')).select_by_visible_text(u""+datos["Estatus"])
#     world.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/form/button').click()

@step(u'Dado que yo edito la siguiente informacion y apachurro el boton Guardar')
def dado_que_yo_edito_la_siguiente_informacion_y_apachurro_el_boton_guardar(step):
    world.driver.implicitly_wait(1)
    driver = world.driver
    datos = step.hashes.first
    Select(driver.find_element_by_id("id_status")).select_by_visible_text(u""+datos["Estatus"])
    #Select(driver.find_element_by_name('status')).select_by_visible_text(u""+datos["Estatus"])
    world.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/form/button').click()

@step(u'entonces puedo observar a "([^"]*)" con el status "([^"]*)" en la lista de registros de las becas de nuevo ingreso')
def entonces_puedo_observar_a_group1_con_el_status_group2_en_la_lista_de_registros_de_las_becas_de_nuevo_ingreso(step, estudiante, estatus):
    driver = world.driver
    world.driver.implicitly_wait(1)
    #estatus_label =  driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/table/tbody/tr[1]/td[4]')
    tb_body = world.driver.find_element_by_tag_name('tbody')
    elementos = tb_body.find_elements_by_tag_name("td")
    elementosStr = [u""+elemento.text for elemento in elementos]
    assert estudiante in elementosStr and estatus in elementosStr,\
        u"No se encontró "+estatus
    finalizaDriver()

@step(u'entonces puedo ver a "([^"]*)" con el estatus "([^"]*)" en la lista de registros de las becas de renovacion')
def entonces_puedo_ver_a_group1_con_el_estatus_group2_en_la_lista_de_registros_de_las_becas_de_renovacion(step, estudiante, estatus):
    driver = world.driver
    world.driver.implicitly_wait(1)
    #estatus_label =  driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/table/tbody/tr[1]/td[4]')
    tb_body = world.driver.find_element_by_tag_name('tbody')
    elementos = tb_body.find_elements_by_tag_name("td")
    elementosStr = [u""+elemento.text for elemento in elementos]
    assert estudiante in elementosStr and estatus in elementosStr,\
        u"No se encontró "+estatus
    finalizaDriver()
'''
STEPS ACTUALIZAR STATUS NUEVO INGRESO Y RENOVACION (RECHAZADA)
'''

'''
STEPS PARA ELIMINAR UN SOLICITANTE NUEVO INGRESO Y RENOVACION
'''
@step(u'Dado que yo puedo ver al estudiante "([^"]*)" y presiono el boton Eliminar')
def dado_que_yo_puedo_ver_al_estudiante_group1_y_presiono_el_boton_eliminar(step, estudiante):
    world.driver.implicitly_wait(1)
    tabla = world.driver.find_element_by_class_name('table')
    tb_body = world.driver.find_element_by_tag_name('tbody')
    filas = tb_body.find_elements_by_tag_name('tr')

    for fila in filas:
        celdas = fila.find_elements_by_tag_name('td')
        if estudiante in u'' + celdas[1].text:
            celdas[6].find_element_by_class_name('btn-danger').click()
            break

@step(u'y despues confirmo que lo quiero eliminar')
def y_despues_confirmo_que_lo_quiero_eliminar(step):
    world.driver.find_element_by_xpath('/html/body/div[1]/form/button').click()

@step(u'entonces puedo confirmar que el solicitante "([^"]*)" ya no existe la lista de registros de las becas')
def entonces_puedo_confirmar_que_el_solicitante_group1_ya_no_existe_la_lista_de_registros_de_las_becas(step, estudiante):
    driver = world.driver
    world.driver.implicitly_wait(1)
    tb_body = world.driver.find_element_by_tag_name('tbody')
    elementos = tb_body.find_elements_by_tag_name("td")
    elementosStr = [u""+elemento.text for elemento in elementos]
    assert estudiante not in elementosStr,\
        u"No se encontró "+estudiante
    finalizaDriver()
'''
STEPS PARA ELIMINAR UN SOLICITANTE NUEVO INGRESO Y RENOVACION
'''

'''
Metodo para inicializar el driver Chrome
'''
def iniciarDriver():
    world.driver = webdriver.Chrome()
'''
Metodo para finalizar el driver Chrome
'''
def finalizaDriver():
    world.driver.quit()