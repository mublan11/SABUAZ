# -*- coding: utf-8 -*-
from lettuce import step, world
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time
import re


@step(u'Dado que ingreso al sistema')
def dado_que_ingreso_al_sistema(step):
    iniciar()


# ----------------------------------------------------------------------------
# AGREGAR
# ----------------------------------------------------------------------------

@step(u'Entonces agrego el Nombre "([^"]*)"')
def entonces_agrego_el_nombre_group1(step, nombre):
    txt_nombre = world.driver.find_element_by_id("id_nombre")
    txt_nombre.send_keys(nombre)


@step(u'Y el Apellido Paterno "([^"]*)"')
def y_el_apellido_paterno_group1(step, apellidoPaterno):
    txt_apellidoPaterno = world.driver.find_element_by_id("id_apellido_paterno")
    txt_apellidoPaterno.send_keys(apellidoPaterno)


@step(u'Y el Apellido Materno "([^"]*)"')
def y_el_apellido_materno_group1(step, apellidoMaterno):
    txt_apellidoMaterno = world.driver.find_element_by_id("id_apellido_materno")
    txt_apellidoMaterno.send_keys(apellidoMaterno)


@step(u'Y el Comedor "([^"]*)"')
def y_el_comedor_group1(step, comedor):
    world.driver.find_element_by_id("id_comedor_fk").click()
    Select(world.driver.find_element_by_id("id_comedor_fk")).select_by_visible_text(comedor)
    world.driver.find_element_by_id("id_comedor_fk").click()


@step(u'Y la casa estudiantil "([^"]*)"')
def y_la_casa_estudiantil_group1(step, casas):
    world.driver.find_element_by_id("id_casas_estudiantil_fk").click()
    Select(world.driver.find_element_by_id("id_casas_estudiantil_fk")).select_by_visible_text(casas)
    world.driver.find_element_by_id("id_casas_estudiantil_fk").click()


@step(u'Cuando presiono el boton "([^"]*)"')
def cuando_presiono_el_boton_group1(step, group1):
    world.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/form/button').click()


@step(u'Entonces veo la pagina "([^"]*)" con el nuevo Supervisor registrado.')
def entonces_veo_la_pagina_group1_con_el_nuevo_supervisor_registrado(step, group1):
    world.driver.get("http://127.0.0.1:8000/supervisor/mostrar")
    finalizaDriver()


# ----------------------------------------------------------------------------
# MODIFICAR
# ----------------------------------------------------------------------------

@step(u'Entonces presiono el boton "([^"]*)" del registro "([^"]*)"')
def entonces_presiono_el_boton_group1_del_registro_group2(step, group1, nombre_supervisor):
    tabla = world.driver.find_element_by_class_name('table')
    tb_body = tabla.find_element_by_tag_name('tbody')
    filas = tb_body.find_elements_by_tag_name('tr')

    for fila in filas:
        celdas = fila.find_elements_by_tag_name('td')

        if nombre_supervisor in u'' + celdas[1].text:
            celdas[4].find_element_by_class_name('btn-primary').click()
            break


@step(u'Y modifico el nombre por "([^"]*)"')
def y_modifico_el_nombre_por_group1(step, nuevo):
    txt_nombre = world.driver.find_element_by_id("id_nombre")
    txt_nombre.clear()
    txt_nombre.send_keys(nuevo)


@step(u'Y presiono el boton Guardar')
def y_presiono_el_boton_guardar(step):
    world.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/form/button').click()


@step(u'Entonces veo el nombre "([^"]*)" en la tabla de Supervisor registrado editado.')
def entonces_veo_el_nombre_group1_en_la_tabla_de_supervisor_registrado_editado(step, group1):
    world.driver.get("http://127.0.0.1:8000/supervisor/mostrar")
    finalizaDriver()


# ----------------------------------------------------------------------------
# ELIMINAR
# ----------------------------------------------------------------------------

@step(u'Entonces entro a "([^"]*)"')
def entonces_entro_a_group1(step, group1):
    world.driver.get("http://127.0.0.1:8000/supervisor/mostrar")


@step(u'Y presiono el boton "([^"]*)" del registro "([^"]*)"')
def y_presiono_el_boton_group1_del_registro_group2(step, boton, nombre_supervisor):
    tabla = world.driver.find_element_by_class_name('table')
    tb_body = tabla.find_element_by_tag_name('tbody')
    filas = tb_body.find_elements_by_tag_name('tr')

    for fila in filas:
        celdas = fila.find_elements_by_tag_name('td')

        if nombre_supervisor in u'' + celdas[1].text:
            celdas[4].find_element_by_class_name('btn-danger').click()
            break


@step(u'Y presiono el boton "([^"]*)"')
def y_presiono_el_boton_group1(step, group1):
    world.driver.find_element_by_class_name('btn-danger').click()


@step(u'Entonces veo la pagina "([^"]*)" sin el Comedor registrado anteriormente.')
def entonces_veo_la_pagina_group1_sin_el_comedor_registrado_anteriormente(step, group1):
    world.driver.get("http://127.0.0.1:8000/supervisor/mostrar")
    finalizaDriver()


# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------

def iniciar():
    world.driver = webdriver.Chrome('chromedriver')
    world.driver.get("http://127.0.0.1:8000")

    world.driver.find_element_by_name("username").clear()
    world.driver.find_element_by_name("username").send_keys("root")
    world.driver.find_element_by_name("password").clear()
    world.driver.find_element_by_name("password").send_keys("1234root")
    world.driver.find_element_by_xpath("/html/body/div[1]/form/div[3]/div/div/input").click()
    world.driver.get("http://127.0.0.1:8000/supervisor/nuevo")


def buscar_nombre_en_table(nombre_supervisor):
    tabla = world.driver.find_element_by_class_name('table')
    tb_body = tabla.find_element_by_tag_name('tbody')
    filas = tb_body.find_elements_by_tag_name('tr')
    supervisor_insertado = False

    for fila in filas:
        celdas = fila.find_elements_by_tag_name('td')

        if nombre_supervisor in u'' + celdas[1].text:
            print
            u'' + celdas[1].text
            supervisor_insertado = True
            break

    return supervisor_insertado
'''
Metodo para finalizar el driver Chrome
'''
def finalizaDriver():
    world.driver.quit()