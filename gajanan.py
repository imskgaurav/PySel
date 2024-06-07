import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


@pytest.fixture()
def driver_setUp():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield
    driver.quit()


def test_flipkart_demo(driver_setUp):
   
    driver.get("https://www.flipkart.com/")
    driver.implicitly_wait(5)
    driver.maximize_window()
    search_input = driver.find_element(By.NAME, 'q')
    search_input.send_keys("AC")
    search_element = driver.find_element(By.XPATH,
                                         "//*[local-name()='svg']/*[local-name()='g' and @fill-rule='evenodd']")
    actions = ActionChains(driver)
    actions.move_to_element(search_element).click().perform()
 
def test_svg_map(driver_setUp):
    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    states_list = driver.find_elements(By.XPATH,
                                       "//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name() = 'path']")
    for state in states_list:
        aria_label = state.get_attribute("aria-label")
        print(aria_label)

        if aria_label == "Tripura ":
            actions.move_to_element(state).click().perform()
        break
    if __name__ == "__main__":
        pytest.main(["-v"])
