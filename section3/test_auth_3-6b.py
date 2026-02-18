from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import math
import pytest

def calc():
  return str(math.log(int(time.time())))

stepikUserName = os.environ.get('stepikUserName')
stepikUserPassword = os.environ.get('stepikUserPassword')

@pytest.mark.parametrize('link', ["236895/step/1", "236896/step/1"])
def test_auth(browser, link):
    link = f"https://stepik.org/lesson/{link}"
    browser.get(link)
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "ember499"))
     )
    button.click()

    print("-10-")

    id_login_email = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.ID, "id_login_email"))
        )
    id_login_email.send_keys(stepikUserName)

    id_login_password = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.ID, "id_login_password"))
        )
    id_login_password.send_keys(stepikUserPassword)

    sign_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.sign-form__btn"))
     )
    sign_button.click()

    print("-20-")

    answer = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.ember-text-area"))
        )
    answer.clear()
    answer.send_keys(calc())

    print("-25-")

    submit_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
     )
    submit_button.click()

    print("-30-")

    result_text = WebDriverWait(browser, 10,ignored_exceptions=ignored_exceptions).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "p.smart-hints__hint"),"Correct!")
        )
    


