from selenium import webdriver
import time

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

browser.execute_script("document.title='Script executing';alert('Robots at work');")

time.sleep(5)

