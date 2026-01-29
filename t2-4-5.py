from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 

    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"),"$100") 
        )

    book = browser.find_element(By.ID, "book")
    book.click()

    x = browser.find_element(By.ID, "input_value").text
    print(x)
    y = calc(x)
    print(y)

    #time.sleep(200)

    in_element = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.ID, "answer"))
        )
    in_element.send_keys(y)

    solve = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.ID, "solve"))
        )
    solve.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

