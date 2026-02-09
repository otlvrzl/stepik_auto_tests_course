from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

link = "https://stepik.org/lesson/236895/step/1"

stepikUserName = os.environ.get('stepikUserName')
stepikUserPassword = os.environ.get('stepikUserPassword')

def test_auth(browser):
    browser.get(link)
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "ember499"))
     )
    button.click()

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

