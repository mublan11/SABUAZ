# -*- coding: utf-8 -*-
from lettuce import step, world
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

'''
--------------------------------------------------------------------------------
Agregar
--------------------------------------------------------------------------------
'''


@step(u'Dado que ingreso al sistema')
def dado_que_ingreso_al_sistema(step):
    iniciar()


@step(u'entro en la lista de registrar casa estudiantil')
def entro_en_la_lista_de_registrar_casa_estudiantil(step):
    world.driver.get("http://127.0.0.1:8000/casaestudiantil/nuevo")


@step(u'cuando agrego el Nombre	de casa "([^"]*)"')
def cuando_agrego_el_nombre_de_casa_group1(step, nombre_casa):
    txt_nombre_casa = world.driver.find_element_by_id("id_casa_estudiantil-nombre")
    txt_nombre_casa.send_keys(nombre_casa)


@step(u'y nombre propietario "([^"]*)"')
def y_nombre_propietario_group1(step, nombre):
    txt_nombre = world.driver.find_element_by_id("id_descripcion_casa-nombre_dueno")
    txt_nombre.send_keys(nombre)


@step(u'y capaciad "([^"]*)"')
def y_capaciad_group1(step, capacidad):
    txt_nombre = world.driver.find_element_by_id("id_descripcion_casa-capacidad")
    txt_nombre.send_keys(capacidad)


@step(u'y camas "([^"]*)"')
def y_camas_group1(step, camas):
    txt_nombre = world.driver.find_element_by_id("id_descripcion_casa-camas")
    txt_nombre.send_keys(camas)


@step(u'y cuartos "([^"]*)"')
def y_cuartos_group1(step, cuartos):
    txt_nombre = world.driver.find_element_by_id("id_descripcion_casa-cuartos")
    txt_nombre.send_keys(cuartos)


@step(u'y sillas "([^"]*)"')
def y_sillas_group1(step, sillas):
    txt_nombre = world.driver.find_element_by_id("id_descripcion_casa-sillas")
    txt_nombre.send_keys(sillas)


@step(u'y cocinas "([^"]*)"')
def y_cocinas_group1(step, cocinas):
    txt_nombre = world.driver.find_element_by_id("id_descripcion_casa-cocinas")
    txt_nombre.send_keys(cocinas)


@step(u'y banos "([^"]*)"')
def y_banos_group1(step, banos):
    txt_nombre = world.driver.find_element_by_id("id_descripcion_casa-banios")
    txt_nombre.send_keys(banos)


@step(u'y el Numero "([^"]*)"')
def y_el_numero_group1(step, numero):
    txt_numero = world.driver.find_element_by_id("id_domicilio-numero")
    txt_numero.send_keys(numero)


@step(u'y la Calle "([^"]*)"')
def y_la_calle_group1(step, calle):
    txt_calle = world.driver.find_element_by_id("id_domicilio-calle")
    txt_calle.send_keys(calle)


@step(u'y la Colonia "([^"]*)"')
def y_la_colonia_group1(step, colonia):
    txt_colonia = world.driver.find_element_by_id("id_domicilio-colonia")
    txt_colonia.send_keys(colonia)


@step(u'y el Codigo Postal "([^"]*)"')
def y_el_codigo_postal_group1(step, codigo):
    txt_cp = world.driver.find_element_by_id("id_domicilio-codigo_postal")
    txt_cp.send_keys(codigo)


@step(u'y el Estado "([^"]*)"')
def y_el_estado_group1(step, estado):
    world.driver.find_element_by_id("id_domicilio-estado").click()
    Select(world.driver.find_element_by_id("id_domicilio-estado")).select_by_visible_text(estado)
    world.driver.find_element_by_id("id_domicilio-estado").click()


@step(u'y el municipio "([^"]*)"')
def y_el_municipio_group1(step, municipio):
    world.driver.find_element_by_id("id_domicilio-municipio").click()
    Select(world.driver.find_element_by_id("id_domicilio-municipio")).select_by_visible_text(municipio)
    world.driver.find_element_by_id("id_domicilio-municipio").click()


@step(u'y el Telefono "([^"]*)"')
def y_el_telefono_group1(step, telefono):
    txt_tel = world.driver.find_element_by_id("id_telefono-telefono")
    txt_tel.send_keys(telefono)


@step(u'Cuando presiono el boton "([^"]*)"')
def cuando_presiono_el_boton_group1(step, group1):
    world.driver.find_element_by_class_name('btn-primary').click()

@step(u'Entonces veo la pagina listar con la nueva casa "([^"]*)" registrada.')
def entonces_veo_la_pagina_listar_con_la_nueva_casa_group1_registrada(step, casa):
    #world.driver.implicitly_wait(1)
    tb_body = world.driver.find_element_by_tag_name('tbody')
    elementos = tb_body.find_elements_by_tag_name("td")
    elementosStr = [u""+elemento.text for elemento in elementos]
    assert casa in elementosStr,\
        u"No se encontró "+casa+" en "+str(elementosStr)
    finalizaDriver()


'''
--------------------------------------------------------------------------------
Modificar
--------------------------------------------------------------------------------
'''


@step(u'entro en la lista de casas')
def entro_en_la_lista_de_casas(step):
    world.driver.get("http://127.0.0.1:8000/casaestudiantil/mostrar")


@step(u'cuando oprimo el boton "([^"]*)" del registro "([^"]*)"')
def cuando_oprimo_el_boton_group1_del_registro_group2(step, boton, nombre_casa):
    tabla = world.driver.find_element_by_class_name('table')
    tb_body = tabla.find_element_by_tag_name('tbody')
    filas = tb_body.find_elements_by_tag_name('tr')

    for fila in filas:
        celdas = fila.find_elements_by_tag_name('td')

        if nombre_casa == u'' + celdas[1].text:
            celdas[5].find_element_by_class_name('btn-primary').click()
            break


@step(u'modifico el nombre por "([^"]*)"')
def modifico_el_nombre_por_group1(step, nuevo):
    txt_nombre = world.driver.find_element_by_id("id_nombre")
    txt_nombre.clear()
    txt_nombre.send_keys(nuevo)


@step(u'Cuando presiono el boton Guardar')
def cuando_presiono_el_boton_guardar(step):
    world.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/form/button').click()
    finalizaDriver()


'''
--------------------------------------------------------------------------------
Eliminar
--------------------------------------------------------------------------------
'''


@step(u'Y presiono el boton "([^"]*)" del registro "([^"]*)"')
def y_presiono_el_boton_group1_del_registro_group2(step, boton, nombre_casa):
    tabla = world.driver.find_element_by_class_name('table')
    tb_body = tabla.find_element_by_tag_name('tbody')
    filas = tb_body.find_elements_by_tag_name('tr')

    for fila in filas:
        celdas = fila.find_elements_by_tag_name('td')

        if nombre_casa == u'' + celdas[1].text:
            celdas[5].find_element_by_class_name('btn-danger').click()
            break


@step(u'Y presiono el boton "([^"]*)"')
def y_presiono_el_boton_group1(step, group1):
    world.driver.find_element_by_class_name('btn-danger').click()

@step(u'Entonces veo la casa "([^"]*)" sin la casa registrada anteriormente.')
def entonces_veo_la_casa_group1_sin_la_casa_registrada_anteriormente(step, casa):
    world.driver.implicitly_wait(1)
    tb_body = world.driver.find_element_by_tag_name('tbody')
    elementos = tb_body.find_elements_by_tag_name("td")
    elementosStr = [u""+elemento.text for elemento in elementos]
    #print (elementosStr)
    assert casa in elementosStr,\
        u"No se encontró "+casa+" en "+str(elementosStr)
    finalizaDriver()
'''
--------------------------------------------------------------------------------
Metodos
--------------------------------------------------------------------------------
'''


def iniciar():
    # world.driver = webdriver.Chrome('chromedriver')
    world.driver = webdriver.Firefox()
    world.driver.get("http://127.0.0.1:8000")

    world.driver.find_element_by_name("username").clear()
    world.driver.find_element_by_name("username").send_keys("root")
    world.driver.find_element_by_name("password").clear()
    world.driver.find_element_by_name("password").send_keys("root1234")
    world.driver.find_element_by_name('botton').click()


# def buscar_nombre_en_table(casa):
#     tabla = world.driver.find_element_by_class_name('table')
#     tb_body = tabla.find_element_by_tag_name('tbody')
#     filas = tb_body.find_elements_by_tag_name('tr')
#     casa_insertada = False

#     for fila in filas:
#         celdas = fila.find_elements_by_tag_name('td')

#         if casa in u'' + celdas[1].text:
#             print
#             u'' + celdas[1].text
#             casa_insertada = True
#             break

#     return casa_insertada
'''
Metodo para finalizar el driver Chrome
'''
def finalizaDriver():
    world.driver.quit()