

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()
driver.get('https://app.vwo.com/')
title = driver.title
time.sleep(3)
print(title)
assert "Login - VWO" in driver.title

email_elm= driver.find_element(By.NAME, "username")
email_elm.send_keys("shashikant.gaurav@gmail.com")
pass_elm = driver.find_element(By.NAME,"password")
#WW.until(EC.visibility_of(pass_elm))
pass_elm.send_keys("Python24")

submit_button = driver.find_element(By.CSS_SELECTOR, "#js-login-btn")
submit_button.click()
time.sleep(7)


def funct(x):
    return x+1

def test_ans():
    assert funct(3)==4
    
print("Assert Pass")    


