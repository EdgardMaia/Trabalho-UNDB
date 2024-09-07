# Caso de Teste 2:
# Descrição: Verificar se é possível inserir um termo de busca no campo de pesquisa.
# Passos:
#   Acessar a URL https://www.google.com
#   Inserir um termo de busca válido no campo de pesquisa

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
    pesquisa = ("tecnologia")
    area_pesquisa.send_keys(pesquisa) 
    area_pesquisa.send_keys(Keys.RETURN)
    time.sleep(4)

    # Imprime uma mensagem de confirmação
    if area_pesquisa:
        print(f"\nTermo de busca '{pesquisa}' inserido com sucesso.")
    else:
        print(f"\nTermo de busca '{pesquisa}' mal sucessidida.")

finally:   
    # Fecha o navegador
    driver.quit()