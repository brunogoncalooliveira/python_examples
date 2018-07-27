# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import re

def CriarRegisto(modulo, alias, descricao, data):
    global driver
    # Id's de elementos
    ALIAS = 'xxx_Alias'
    DESCRICAO = 'xxx_Description'
    DATA_IMPLEMENTACAO = 'xxx_DataInicio'
    GRAVAR_SERVICO_EXPOSTO = 'wt5_block_wtButtons_wt24'

    driver.get('http://127.0.0.1/Detalhe.aspx?id=' + modulo)
    driver.get('http://127.0.0.1/ServicoExposto_Lista.aspx?ShowMenu=False&ReadOnly=False')
    adicionar = driver.find_element_by_id('wtbotaoAdd')
    adicionar.click()

    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe"))) # seleciona a iframe
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, ALIAS))).send_keys(alias)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, DESCRICAO))).send_keys(descricao)
    # executa o comando javascript: $('#DataInicio').val('2018-07-01')
    driver.execute_script("$('#" + DATA_IMPLEMENTACAO + "').val('" + data + "')")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, GRAVAR_SERVICO_EXPOSTO))).click()

driver = webdriver.Chrome()
CriarServicoExposto('12', u'Selenium 1', u'Isto é uma descrição', '2018-07-07')
CriarServicoExposto('12', u'Selenium 2', u'Isto é outra descrição', '2018-06-07')
driver.quit()
