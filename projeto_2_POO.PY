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
options.add_argument("--disable-notifications")  # Desabilitar notificações

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


driver = webdriver.Chrome(options=options)
url_login = 'https://estudante.estacio.br/login'


email = input('digite o email do usuario: ')
password = input("digite a sua senha: ")


class Extrai:
    def __init__(self, email, password, driver):
        self.email = email
        self.password = password
        self.driver = driver



    def login(self):

     sleep(10)
     self.driver.get(url_login)

     sleep(8)
     button_estcaio = self.driver.find_element(By.XPATH, '//*[@id="section-login"]/div/div/div/section/div[1]/button')
     button_estcaio.click()

     sleep(25)

     email_input = self.driver.find_element(By.NAME, 'loginfmt')
     email_input.send_keys('202203366841@alunos.estacio.br')

     submit_button = self.driver.find_element(By.ID, 'idSIButton9')
     submit_button.click()

     sleep(2)

     senha_input = self.driver.find_element(By.NAME, 'passwd')
     senha_input.send_keys('BateraDeus3#')

     sleep(2)

     submit_senha = self.driver.find_element(By.ID, 'idSIButton9')
     submit_senha.click()

     sleep(1)

     submit_neg = self.driver.find_element(By.ID, 'idBtn_Back')
     submit_neg.click()





    def estudante_tema(self):
     sleep(20)

     disc = self.driver.find_element(By.XPATH, '//*[@id="card-entrega-ARA0066"]').click()

     sleep(2)

     tema = self.driver.find_element(By.XPATH, '//*[@id="temas-lista-topicos"]/li[5]/a/div').click()
     sleep(1)

     pag = self.driver.find_element(By.XPATH, '//*[@id="segunda-tab"]').click()

     sleep(2)

     site = self.driver.find_element(By.XPATH, '//*[@id="acessar-conteudo-complementar-link-646160d3efeb4f0025211737"]').click()







    def  site_extrai(self):
     sleep(25)
     #find_element_by_xpath("//div[@data-rel='phone']")
     inp = self.driver.find_element(By.ID, 'input-busca')
     inp.send_keys('Processador Intel i9')
     pesquisa = self.driver.find_element(By.XPATH, '//*[@id="barraBuscaKabum"]/div/form/button').click()



     sleep(15)


     descricao = self.driver.find_elements(By.CLASS_NAME, 'sc-d99ca57-0')
     precos = self.driver.find_elements(By.CLASS_NAME, 'sc-3b515ca1-2')
     precos_ant = self.driver.find_elements(By.CLASS_NAME, 'sc-3b515ca1-1')
     horas = self.driver.find_elements(By.CLASS_NAME, 'sc-3ab99a4d-0')

# Crie listas vazias para armazenar as descrições e os preços dos produtos
     nome_produtos = []
     preco_produtos = []
     preco_ant_produtos = []
     tempo_produtos = []

# Itere sobre os elementos encontrados e extraia as descrições e os preços dos produtos
     for nome, preco, preco_ant, tempo in zip(descricao, precos, precos_ant, horas):
         nome_produtos.append(nome.text)
         preco_produtos.append(preco.text)
         preco_ant_produtos.append(preco_ant.text)
         tempo_produtos.append(tempo.text)


     produtos = pd.DataFrame({'Nome Produto' : nome_produtos, 'Preço Atual' : preco_produtos, 'Preço Anterior' : preco_ant_produtos, 'Tempo Promoção' : tempo_produtos})

     print(produtos)
     self.driver.quit()













extrai = Extrai(email, password, driver)

extrai.login()
extrai.estudante_tema()
extrai.site_extrai()


