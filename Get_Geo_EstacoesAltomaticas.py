# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 10:22:02 2017

@author: leandro
"""
import time
from selenium import webdriver



URL="http://www.inmet.gov.br/portal/index.php?r=estacoes/estacoesAutomaticas"
#Iniciando Arquivo
save = open("dadosestações_f.csv","w")
save.write('Nome,Latitude,Longitude,Altitude\n')
#Setando webDriver
browser = webdriver.Firefox()
#Acessando endereco
browser.get(URL)

#Para acessar o #Document temos que entrar no iFrame primeiro
browser.switch_to_frame(browser.find_element_by_tag_name("iframe"))
'''
No for temos a seguinte sequencia de comandos
linha  30               -Simula o clink no nome da estacao
linha  31               - Acho o elemento "novo" que aparece apos o click e o transforma em uma string
linhas 32,34,35 e 36    - Retiro da string Nome latitude logitude e altitude da estacao
OBS: Comentei a linha 34 porque tem estacao sem codigo
'''
for i in range(0,551):
    browser.find_element_by_css_selector(str("a[href*='javascript:myclick("+str(i)+")']")).click()
    passElement = browser.find_element_by_css_selector('html body div#map_canvas div div.gm-style div div div div div.gm-style-iw div div div font').text.split('\n')
    name = passElement[0].split(': ')[1]
    #codOMM = passElement[1].split(': ')[1]
    lat =  passElement[len(passElement)-3].split(': ')[1].replace('º','')
    log =  passElement[len(passElement)-2].split(': ')[1].replace('º','')
    alt =  passElement[len(passElement)-1].split(': ')[1].replace('metros','').replace(',','.')
    save.write(str(name+','+lat+','+log+','+alt+'\n'))

save.close()


#print(tpm==tpm2)
##print(passElement)