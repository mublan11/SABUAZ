# -*- coding: utf-8 -*-
from lettuce import step, world
from selenium import webdriver

@step(u'Dado que ingreso la url "([^"]*)"')
def dado_que_ingreso_la_url_group1(step, ruta):
  world.driver = webdriver.Chrome('chromedriver')
  world.driver.get(ruta)

@step(u'Y en las recuadros Nombre de Usuario "([^"]*)" y la contrasena "([^"]*)"')
def y_en_las_recuadros_nombre_de_usuario_group1_y_la_contrasena_group2(step, nombre, contra):
  world.driver.find_element_by_name("username").clear()
  world.driver.find_element_by_name("username").send_keys(nombre)
  world.driver.find_element_by_name("password").clear()
  world.driver.find_element_by_name("password").send_keys(contra)
  
@step(u'Cuando presiono el boton ingresar')
def cuando_presiono_el_boton_ingresar(step):
  world.driver.find_element_by_class_name('btn-primary').click()

@step(u'Entonces ingreso a la pagina de "([^"]*)"')
def entonces_ingreso_a_la_pagina_de_group1(step, ruta):
  world.driver.find_element_by_class_name('no-margin-top').text == "Solicitante"
  

