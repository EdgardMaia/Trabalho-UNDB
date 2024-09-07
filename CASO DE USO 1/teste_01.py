# Caso de Teste 1:
# Descrição: Verificar se o campo de pesquisa está disponivel ou não.
# Passos:
#   Acessar a URL https://www.google.com
#   Verificar a presença do campo de pesquisa no Google

from selenium import webdriver # Controlar o navegador
from selenium.webdriver.common.by import By # Ajuda a encontrar elementos específicos na página.
from selenium.webdriver.support.ui import WebDriverWait # Espera que algo aconteça.
from selenium.webdriver.support import expected_conditions as EC  # Define o que estamos esperando acontecer.
from webdriver_manager.microsoft import EdgeChromiumDriverManager # Baixa e instala automaticamente o driver do navegador Microsoft Edge.
from selenium.webdriver.edge.service import Service # Ajuda a iniciar o navegador.
import time # servir como tempo de resposta para o código

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
    
    time.sleep(2)
    
    if area_pesquisa:
        print("\nCampo de pesquisa disponivel.")
    else:
        print("\nCampo de pesquisa não disponivel.")

finally:
    driver.quit()