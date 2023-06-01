from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-notifications")  # Desabilitar notificações
options.add_experimental_option('excludeSwitches', ['enable-logging'])

url_login = 'https://estudante.estacio.br/login'

print('É importante esse arquivo tenha o seguinte caminho: C:\Projeto_Alta\projeto-2\projeto-2')
email = input('digite o email do usuario: ')
password = input("digite a sua senha: ")

driver = webdriver.Chrome(options=options)

class KabumProdutos:
    def __init__(self, email, password, driver):
        self.email = email
        self.password = password
        self.driver = driver

    def login(self):

     sleep(10)
     self.driver.get(url_login)

     sleep(8)
     button_estacio = self.driver.find_element(By.XPATH, '//*[@id="section-login"]/div/div/div/section/div[1]/button')
     button_estacio.click()

     sleep(25)

     email_input = self.driver.find_element(By.NAME, 'loginfmt')
     email_input.send_keys(email)

     submit_button = self.driver.find_element(By.ID, 'idSIButton9')
     submit_button.click()

     sleep(2)

     senha_input = self.driver.find_element(By.NAME, 'passwd')
     senha_input.send_keys(password)

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
     sleep(2)
     self.driver.switch_to.window(driver.window_handles[-1])


    def  site_extrai(self):
     sleep(25)

     inp = self.driver.find_element(By.XPATH, "//input[@id='input-busca' and @class='id_search_input']")
     inp.send_keys('Processador Intel i9')
     print(inp)

     pesquisa = self.driver.find_element(By.XPATH, '//*[@id="barraBuscaKabum"]/div/form/button').click()

     sleep(20)

     conteudo = driver.find_elements(By.CLASS_NAME, 'sc-ff8a9791-7')

     nome_produtos = []
     preco_produtos = []
     preco_ant_produtos = []
     tempo_produtos = []

     for conteudo_card in conteudo:
          descricao = conteudo_card.find_elements(By.CLASS_NAME, 'sc-d99ca57-0')
          preco = conteudo_card.find_elements(By.CLASS_NAME, 'sc-3b515ca1-2')
          preco_ant = conteudo_card.find_elements(By.CLASS_NAME, 'sc-3b515ca1-1')
          hora = conteudo_card.find_elements(By.CLASS_NAME, 'sc-3ab99a4d-0')

          for descricao, preco, preco_ant, hora in zip(descricao, preco, preco_ant, hora):
             nome_produtos.append(descricao.text)
             preco_produtos.append(preco.text)
             preco_ant_produtos.append(preco_ant.text)
             tempo_produtos.append(hora.text)


     while True:
        try:
         proxima_pagina = driver.find_element(By.XPATH,'//a[@rel="next"]')

         if "disabled" in  proxima_pagina.get_attribute("class"):
            break

         proxima_pagina.click()

         for conteudo_card in conteudo:
          descricao = conteudo_card.find_elements(By.CLASS_NAME, 'sc-d99ca57-0')
          preco = conteudo_card.find_elements(By.CLASS_NAME, 'sc-3b515ca1-2')
          preco_ant = conteudo_card.find_elements(By.CLASS_NAME, 'sc-3b515ca1-1')
          hora = conteudo_card.find_elements(By.CLASS_NAME, 'sc-3ab99a4d-0')

          for descricao, preco, preco_ant, hora in zip(descricao, preco, preco_ant, hora):
             nome_produtos.append(descricao.text)
             preco_produtos.append(preco.text)
             preco_ant_produtos.append(preco_ant.text)
             tempo_produtos.append(hora.text)



        except Exception as e:
         print("Ocorreu um erro:", str(e))
         break


     produtos = pd.DataFrame({'Nome Produto' : nome_produtos, 'Preço Atual' : preco_produtos, 'Preço Anterior' : preco_ant_produtos, 'Tempo Promoção' : tempo_produtos})

     produtos.to_excel('C:\\Projeto_Alta\\projeto-2\\projeto-2\\Kabum_Produtos.xlsx', index=False)


     self.driver.quit()



kabum = KabumProdutos(email, password, driver)

kabum.login()
kabum.estudante_tema()
kabum.site_extrai()


