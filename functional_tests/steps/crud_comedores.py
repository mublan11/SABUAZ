# -*- coding: utf-8 -*-
from lettuce import step, world
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time
import re

'''
--------------------------------------------------------------------------------
Agregar
--------------------------------------------------------------------------------
'''



@step(u'Dado que ingreso al sistema')
def dado_que_ingreso_al_sistema(step):
    iniciar()


@step(u'entro en la lista de registrar comedores')
def entro_en_la_lista_de_registrar_comedores(step):
    world.driver.get("http://127.0.0.1:8000/comedor/nuevo")

@step(u'cuando agrego el Nombre	"([^"]*)"')
def cuando_agrego_el_nombre_group1(step, nombre):
    txt_nombre = world.driver.find_element_by_id("id_comedor-nombre")
    txt_nombre.send_keys(nombre)


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
  Select(world.driver.find_element_by_id("id_domicilio-estado")).select_by_visible_text("Zacatecas")
  world.driver.find_element_by_id("id_domicilio-estado").click()
  #cbox_estado = world.driver.find_element_by_xpath('//*[@id="id_domicilio-municipio"]')
   # cbox_estado_opcion = cbox_estado.find_element_by_xpath('//*[@id="id_domicilio-estado"]/option[33]')
    #cbox_estado_opcion.click()
    #cbox_estado.click()
    #Select(driver.find_element_by_id("id_domicilio-estado")).select_by_visible_text(u""+datos["Estado"])

@step(u'y el municipio "([^"]*)"')
def y_el_municipio_group1(step, group1):
  world.driver.find_element_by_id("id_domicilio-municipio").click()
  Select(world.driver.find_element_by_id("id_domicilio-municipio")).select_by_visible_text("Zacatecas")
  world.driver.find_element_by_id("id_domicilio-municipio").click()
    #cbox_mun = world.driver.find_element_by_xpath('//*[@id="id_domicilio-municipio"]')
    #cbox_mun.click()
    #cbox_mun_opcion = cbox_estado.find_element_by_xpath('//*[@id="id_domicilio-municipio"]/option[2]')
    #cbox_mun_opcion.click()
    

@step(u'y el Telefono "([^"]*)"')
def y_el_telefono_group1(step, telefono):
    txt_tel = world.driver.find_element_by_id("id_telefono-telefono")
    txt_tel.send_keys(telefono)

@step(u'Cuando presiono el boton "([^"]*)"')
def cuando_presiono_el_boton_group1(step, group1):
    world.driver.find_element_by_class_name('btn-primary').click()


@step(u'Entonces veo la pagina "([^"]*)" con el nuevo Comedor registrado.')
def entonces_veo_la_pagina_group1_con_el_nuevo_comedor_registrado(step, comedor):
  assert buscar_nombre_en_table(comedor), \
        'No se encuentra la comedor ' + comedor
  finalizaDriver()

'''
--------------------------------------------------------------------------------
Modificar
--------------------------------------------------------------------------------
'''
@step(u'entro en la lista de comedores')
def entro_en_la_lista_de_comedores(step):
    world.driver.get("http://127.0.0.1:8000/comedor/mostrar")

@step(u'cuando oprimo el boton Editar del registro "([^"]*)"')
def cuando_oprimo_el_boton_editar_del_registro_group1(step, nombre_comedor):
  tabla = world.driver.find_element_by_class_name('table')
  tb_body = tabla.find_element_by_tag_name('tbody')
  filas = tb_body.find_elements_by_tag_name('tr')
  
  for fila in filas:
    celdas = fila.find_elements_by_tag_name('td')
    
    if nombre_comedor == u'' + celdas[1].text:
      celdas[4].find_element_by_class_name('btn-primary').click()
      break

# @step(u'cuando oprimo el boton "([^"]*)" del registro "([^"]*)"')
# def cuando_oprimo_el_boton_group1_del_registro_group2(step, boton, nombre_comedor):
#   tabla = world.driver.find_element_by_class_name('table')
#   tb_body = tabla.find_element_by_tag_name('tbody')
#   filas = tb_body.find_elements_by_tag_name('tr')
  
#   for fila in filas:
#     celdas = fila.find_elements_by_tag_name('td')
    
#     if nombre_comedor == u'' + celdas[1].text:
#       celdas[4].find_element_by_class_name('btn-primary').click()
#       break

@step(u'modifico el nombre por "([^"]*)"')
def modifico_el_nombre_por_group1(step, nuevo):
    txt_nombre = world.driver.find_element_by_id("id_nombre")
    txt_nombre.clear()
    txt_nombre.send_keys(nuevo)

@step(u'Cuando presiono el boton Guardar')
def cuando_presiono_el_boton_guardar(step):
    world.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/form/button').click()

@step(u'Entonces veo la pagina "([^"]*)" con el nuevo Comedor registrado.')
def entonces_veo_la_pagina_group1_con_el_nuevo_comedor_registrado(step, comedor):
  assert buscar_nombre_en_table(comedor), \
        'No se encuentra la comedor ' + comedor
  finalizaDriver()

'''
--------------------------------------------------------------------------------
Eliminar
--------------------------------------------------------------------------------
'''

@step(u'Y presiono el boton "([^"]*)" del registro "([^"]*)"')
def y_presiono_el_boton_group1_del_registro_group2(step, boton, nombre_comedor):
  tabla = world.driver.find_element_by_class_name('table')
  tb_body = tabla.find_element_by_tag_name('tbody')
  filas = tb_body.find_elements_by_tag_name('tr')
  
  for fila in filas:
    celdas = fila.find_elements_by_tag_name('td')
    
    if nombre_comedor == u'' + celdas[1].text:
      celdas[4].find_element_by_class_name('btn-danger').click()
      break

@step(u'Y presiono el boton "([^"]*)"')
def y_presiono_el_boton_group1(step, group1):
  world.driver.find_element_by_class_name('btn-danger').click()

@step(u'Entonces veo la pagina "([^"]*)" sin el Supervisor registrado anteriormente.')
def entonces_veo_la_pagina_group1_sin_el_supervisor_registrado_anteriormente(step, group1):
    world.driver.get("http://127.0.0.1:8000/comedor/mostrar")
    finalizaDriver()

'''
--------------------------------------------------------------------------------
Metodos
--------------------------------------------------------------------------------
'''
def iniciar():
  world.driver = webdriver.Firefox()
  #world.driver = webdriver.Chrome('chromedriver')
  world.driver.get("http://127.0.0.1:8000")

  world.driver.find_element_by_name("username").clear()
  world.driver.find_element_by_name("username").send_keys("root")
  world.driver.find_element_by_name("password").clear()
  world.driver.find_element_by_name("password").send_keys("root1234")
  world.driver.find_element_by_name('botton').click()
  

def buscar_nombre_en_table(nombre_comedor):
    
  tabla = world.driver.find_element_by_class_name('table')
  tb_body = tabla.find_element_by_tag_name('tbody')
  filas = tb_body.find_elements_by_tag_name('tr')
  comedor_insertado = False
  
  for fila in filas:
    celdas = fila.find_elements_by_tag_name('td')
    
    if nombre_comedor in u'' + celdas[1].text:
      print u'' + celdas[1].text
      comedor_insertado = True
      break

  return comedor_insertado

'''
Metodo para finalizar el driver Chrome
'''
def finalizaDriver():
    world.driver.quit()