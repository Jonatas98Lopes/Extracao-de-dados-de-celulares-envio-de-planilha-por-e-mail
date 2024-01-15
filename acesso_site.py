from inicializar import GoogleChrome
from selenium.webdriver.common.by import By
from time import sleep


# Site os dados serão extráidos
SITE = 'https://telefonesimportados.netlify.app/'

browser = GoogleChrome()
driver, wait = browser.get_driver(), browser.get_wait()


driver.get(SITE)
sleep(5)

driver.execute_script("window.scrollBy(0, 2500);")








