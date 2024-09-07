#Caso de teste 8:
#Descrição:  Verificar se a pesquisa por vídeos funciona corretamente
#Passos:
#   Acessar a URL: https://www.google.com
#   Inserir um termo de busca
#   Aguardar o carregamento da página de resultados
#   Clicar na aba "Vídeos"
#   Verificar se os vídeos foram carregadas


from selenium import webdriver # Controlar o navegador
from selenium.webdriver.common.by import By # Ajuda a encontrar elementos específicos na página.
from selenium.webdriver.common.keys import Keys # Simular ações do teclado.
from selenium.webdriver.support.ui import WebDriverWait # Espera que algo aconteça.
from selenium.webdriver.support import expected_conditions as EC  # Define o que estamos esperando acontecer.
from webdriver_manager.microsoft import EdgeChromiumDriverManager # Baixa e instala automaticamente o driver do navegador Microsoft Edge.
from selenium.webdriver.edge.service  import Service # Ajuda a iniciar o navegador.
import time #servir como tempo de resposta para o códigoe


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
    pesquisa = "python"
    area_pesquisa.send_keys(pesquisa) 
    area_pesquisa.send_keys(Keys.RETURN)
    time.sleep(2)
    
    # Aguardar o carregamento da página de resultados
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Vídeos")))
    
    # Clicar no link de vídeos
    video_link = driver.find_element(By.LINK_TEXT, "Vídeos")
    video_link.click()
    time.sleep(2)
    
    # Carregar o primeiro vídeo
    yt_link = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/div[1]/div/div/span/a/div')
    yt_link.click()
    time.sleep(2)
    
    # Verificar se os vídeos foram carregadas
    if "https://www.youtube.com/watch" in driver.current_url:
        print(f'''\nA pesquisa por vídeos "{pesquisa}", funcionou corretamente e os vídeos foram carregadas."''')
    else:
        print("\nA pesquisa por vídeos NÃO funcionou.")

finally:
    driver.quit()