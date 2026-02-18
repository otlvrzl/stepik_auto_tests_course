import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = r"/usr/bin/firefox"
driver = webdriver.Firefox(options=options)  
driver.get("https://stepik.org/lesson/25969/step/8")

time.sleep(4)
driver.quit()