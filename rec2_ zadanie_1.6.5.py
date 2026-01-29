from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration2.html")
    
    first_name = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control first']")
    first_name.send_keys("Ivan")
    
    last_name = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control second']")
    last_name.send_keys("Petrov")
    
    email = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control third']")
    email.send_keys("test@example.com")
    
    phone = browser.find_element(By.XPATH, "//div[@class='second_block']//input[@class='form-control first']")
    phone.send_keys("+1234567890")
    
    address = browser.find_element(By.XPATH, "//div[@class='second_block']//input[@class='form-control second']")
    address.send_keys("123 Main St")

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
