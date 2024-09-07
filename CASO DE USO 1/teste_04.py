# Caso de Teste 4:
# Descrição: Verificar o comportamento ao tentar realizar uma pesquisa com o campo de busca vazio.
# Passos:
#   Acessar a URL https://www.google.com
#   Deixar o campo de pesquisa vazio.
#   Tentar clicar no botão de pesquisa.
#   Verificar se o botão de pesquisa realiza alguma ação ou se exibe algum comportamento esperado (como impedir a pesquisa). Quero um código para este

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
    pesquisa = ()
    area_pesquisa.send_keys(pesquisa) 
    area_pesquisa.send_keys(Keys.RETURN)
    time.sleep(2)
    
     # Verificar se o botão de pesquisa está habilitado
    verificar_botao = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[1]")))
    
    # Verificar se o botão de pesquisa está desabilitado para um campo de pesquisa vazio
    if not verificar_botao.is_enabled():
        print("\nO botão de pesquisa está desabilitado quando o campo está vazio.")
    else:
        print("\nO botão de pesquisa está habilitado quando o campo está vazio.")
    
finally:
    # Fechar o navegador
    driver.quit()
