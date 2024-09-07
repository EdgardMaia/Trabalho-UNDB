#Caso de teste 10:
#Descrição:  Verificar se a pesquisa por um termo específico retorna um número mínimo de resultados
#Passos:
#   Acessar a URL: https://www.google.com
#   Inserir um termo de busca
#   Aguardar o carregamento da página de resultados
#   Verificar se há pelo menos a quantidade definida de resultados


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
    pesquisa = "Selenium WebDriver"
    area_pesquisa.send_keys(pesquisa)
    area_pesquisa.send_keys(Keys.RETURN)
    time.sleep(3)
    
    # Verificar se há pelo menos 10 resultados ou da sua escolha.
    resultados = driver.find_elements(By.CSS_SELECTOR, 'div.g')
    resultados_min = 10  # Número mínimo de resultados esperados
    
    if len(resultados) >= resultados_min:
        print(f"\nA pesquisa retornou {len(resultados)} resultados, que é maior ou igual ao mínimo de {resultados_min}.")
    else:
        print(f"\nA pesquisa retornou apenas {len(resultados)} resultados, que é menor do que o mínimo de {resultados_min}.")

finally:
    driver.quit()