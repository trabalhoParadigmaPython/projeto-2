from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import py7zr 
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-popup-blocking")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
download_path = 'C:\Dev\Projetos\Python\Projeto_1\projeto-1-1'  # Substitua pelo caminho da sua pasta de download
prefs = {
    'download.default_directory': download_path,
    'download.prompt_for_download': False,
    'download.directory_upgrade': True,
    'safebrowsing.enabled': True
}
options.add_experimental_option('prefs', prefs)


url = 'https://estudante.estacio.br/login'
driver.get(url)

sleep(8)
button_estcaio = driver.find_element(By.XPATH, '//*[@id="section-login"]/div/div/div/section/div[1]/button')
button_estcaio.click()

sleep(9)

email_input = driver.find_element(By.NAME, 'loginfmt')
email_input.send_keys('202203366841@alunos.estacio.br')

submit_button = driver.find_element(By.ID, 'idSIButton9')
submit_button.click()


senha_input = driver.find_element(By.NAME, 'passwd')
senha_input.send_keys('BateraDeus3#')

sleep(2)

submit_senha = driver.find_element(By.ID, 'idSIButton9')
submit_senha.click()

sleep(1)

submit_neg = driver.find_element(By.ID, 'idBtn_Back')
submit_neg.click()

sleep(10)

disc = driver.find_element(By.XPATH, '//*[@id="card-entrega-ARA0066"]').click()

sleep(2)

tema = driver.find_element(By.XPATH, '//*[@id="temas-lista-topicos"]/li[5]/a/div').click()
sleep(1)

pag = driver.find_element(By.XPATH, '//*[@id="segunda-tab"]').click()
sleep(2)

site = driver.find_element(By.XPATH, '//*[@id="acessar-conteudo-complementar-link-646160d3efeb4f0025211737"]').click()

sleep(10)

a = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()

inp = driver.find_element(By.XPATH, '//*[@id="input-busca"]')
inp.send_keys('Processador Intel i9')
pesquisa = driver.find_element(By.XPATH, '//*[@id="barraBuscaKabum"]/div/form/button').click()

sleep(3)

driver.quit()