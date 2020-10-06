from selenium import webdriver
from selenium.webdriver import ActionChains
import  time

import logging
logging.basicConfig(level=logging.DEBUG)

class Mousehover():
    def mouse_hover(self):
        driver = webdriver.Chrome(executable_path="D:/drivers/chromedriver.exe")
        driver.get("https://letskodeit.teachable.com/p/practice")
        driver.maximize_window()
        driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(2)

        #mousehover to Top
        ele = driver.find_element_by_id("mousehover")
        action = ActionChains(driver)
        action.move_to_element(ele).perform()
        driver.find_element_by_xpath("//div[@class='mouse-hover-content']//a[text()='Top']").click()
        time.sleep(2)
        logging.debug("mousehover to Top done")

        #mousehover to Reload
        driver.execute_script("window.scrollBy(0,1000);")
        ele1 = driver.find_element_by_id("mousehover")
        action = ActionChains(driver)
        action.move_to_element(ele1).perform()
        driver.find_element_by_xpath("//div[@class='mouse-hover-content']//a[text()='Reload']").click()
        time.sleep(2)
        logging.debug("mousehover to Reload done")

m = Mousehover()
m.mouse_hover()