from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    firstname.send_keys('firstname')

    lastname = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    lastname.send_keys('lastname')

    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email.send_keys('email')

    current_dir = os.path.abspath(os.path.dirname(__file__)) 
    file_path = os.path.join(current_dir, 'file.txt')  

    file_element = browser.find_element(By.ID, "file")
    file_element.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()