from inicializar import GoogleChrome

browser = GoogleChrome()
driver, wait = browser.get_driver(), browser.get_wait()