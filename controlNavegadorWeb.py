from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configurar el navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Navegar a Google
    driver.get("https://www.google.com")

    # Buscar el campo de texto y escribir una consulta
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium WebDriver")
    # search_box.send_keys(Keys.RETURN)

    # Esperar unos segundos para ver los resultados
    # driver.implicitly_wait(1000)
finally:
    # Cerrar el navegador
    # driver.quit()
    input("Presiona Enter para cerrar el navegador...")

    
# driver = webdriver.Chrome()

# driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# title = driver.title

# driver.implicitly_wait(1000)

# text_box = driver.find_element(by=By.NAME, value="my-text")
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# text_box.send_keys("Selenium")
# # submit_button.click()

# message = driver.find_element(by=By.ID, value="message")
# text = message.text
# input("Presiona Enter para cerrar el navegador...")

# driver.quit()