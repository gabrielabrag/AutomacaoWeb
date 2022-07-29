from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

#pesquisar cotacao dolar;
navegador = webdriver.Chrome()
navegador.get("https://www.google.com.br/")
navegador.find_element('xpath',
                       '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
                       ).send_keys('cotação dolar')
navegador.find_element('xpath',
                       '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
                       ).send_keys(Keys.ENTER)

#pegar cotacao dolar
cotacao_dolar = navegador.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'
                                       ).get_attribute('data-value')

#pesquisar/pegar cotacao euro
navegador = webdriver.Chrome()
navegador.get("https://www.google.com.br/")
navegador.find_element('xpath',
                       '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
                       ).send_keys('cotação euro')
navegador.find_element('xpath',
                       '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
                       ).send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'
                                       ).get_attribute('data-value')

#pesquisar/pegar cotacao ouro
navegador = webdriver.Chrome()
navegador.get("https://www.melhorcambio.com/ouro-hoje")
#send_keys(Keys.ENTER)
cotacao_ouro = navegador.find_element('xpath','//*[@id="comercial"]'
                                       ).get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(",", ".")

#recalcular base de dados
tabela = pd.read_excel(R'C:\Users\gabir\Downloads\Produtos.xlsx')

#atualizar as cotacoes
tabela.loc[tabela["Moeda"]=="Dolar","Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)

#preço compra= preco original * cotacao
tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]
# preco venda = preco de compra * margem
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]

#exportar base de dados p/excel
tabela.to_excel("Produtos Novos.xlsx",index=False)








