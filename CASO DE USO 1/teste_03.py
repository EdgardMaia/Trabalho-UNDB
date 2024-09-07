# Caso de Teste 3:
# Descrição: Verificar se o botão de pesquisa está habilitado após inserir um termo de busca e pesquisa-lo.
# Passos:
#   Acessar a URL https://www.google.com
#   Encontra o campo de pesquisa pelo nome
#   Inserir um termo de busca válido no campo de pesquisa.
#   Verificar se o botão de pesquisa está habilitado.
#   Simula o pressionamento da tecla 'Enter' para realizar a pesquisa
#   Verificar se a página de resultados contém o elemento que indica resultados

from selenium import webdriver # Controlar o navegador
from selenium.webdriver.common.by import By # Ajuda a encontrar elementos específicos na página.
from selenium.webdriver.common.keys import Keys # Simular ações do teclado.
from selenium.webdriver.support.ui import WebDriverWait # Espera que algo aconteça.
from selenium.webdriver.support import expected_conditions as EC  # Define o que estamos esperando acontecer.
from webdriver_manager.microsoft import EdgeChromiumDriverManager # Baixa e instala automaticamente o driver do navegador Microsoft Edge.
from selenium.webdriver.edge.service  import Service # Ajuda a iniciar o navegador.
import time #servir como tempo de resposta para o código


# Configura o driver automaticamente
service = Service(EdgeChromiumDriverManager().install())
# Inicializa o navegador Edge
driver = webdriver.Edge(service=service)

try:
    # Acessar a URL do Google
    driver.get("https://www.google.com")

    # Encontrar o campo de pesquisa pelo XPath
    area_pesquisa = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='APjFqb']")))

    # Insere um termo de busca
    pesquisa = ("I.A")
    area_pesquisa.send_keys(pesquisa) 
    time.sleep(2)
    
    # Verificar se o botão de pesquisa está habilitado
    verificar_botao = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[1]")))
    
    if verificar_botao.is_enabled():
        print("\nO botão de pesquisa está habilitado.")
    else:
        print("\nO botão de pesquisa NÃO está habilitado.")
         
    #Simula o pressionamento da tecla 'Enter' para realizar a pesquisa
    area_pesquisa.send_keys(Keys.RETURN)
    
    time.sleep(4)  # Aguardar um breve momento para o carregamento da página de resultados
        
    # Verificar se a página de resultados contém o elemento que indica resultados
    if "https://www.google.com/search" in driver.current_url:
        print("\nA página de resultados foi carregada com sucesso.")
    else:
        print("\nA página de resultados NÃO foi carregada corretamente.")
    
    time.sleep(2)    
        
finally:
    # Fechar o navegador
    driver.quit()