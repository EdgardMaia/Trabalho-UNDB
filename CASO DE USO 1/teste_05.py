# Caso de Teste 5:
# Descrição: Verificar se os resultados da pesquisa estão relacionados ao termo de busca.
# Passos:
#   Acessar a URL https://www.google.com
#   Inserir um termo de busca válido no campo de pesquisa.
#   Clicar no botão de pesquisa.
#   Verificar se os títulos dos primeiros resultados contêm o termo de busca.

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
    pesquisa = "GitHub"
    area_pesquisa.send_keys(pesquisa) 
    area_pesquisa.send_keys(Keys.RETURN)
    time.sleep(2)
    
    # Esperar até que os resultados da pesquisa estejam visíveis
    resultados = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'h3')))
    time.sleep(2)
    
    # Verificar os títulos dos primeiros resultados
    resultado_encontrados = False
    for i, resultados in enumerate(resultados[:5]):  # Verificar os primeiros 5 resultados
        titulo = resultados.text
        print(f"Resultado {i+1}: {titulo}")
        if pesquisa.lower() in titulo.lower():
            resultado_encontrados = True
    
    # Exibir se os resultados estão relacionados ou não
    if resultado_encontrados:
        print("\nOs resultados da pesquisa estão relacionados ao termo de busca.")
    else:
        print("\nOs resultados da pesquisa NÃO estão relacionados ao termo de busca.")
finally:
    # Fechar o navegador
    driver.quit()