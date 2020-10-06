from selenium import webdriver
import time
import logging

logging.basicConfig(level=logging.DEBUG)

class Switchtoiframe():
    def switch_to_iframe(self):
        driver = webdriver.Chrome(executable_path="D:/drivers/chromedriver.exe")
        driver.get("https://letskodeit.teachable.com/p/practice")
        driver.maximize_window()


        #switch to iframe
        driver.switch_to.frame("courses-iframe")
        logging.debug("switched to next iframe")

        #click searchbox
        driver.find_element_by_id("search-courses").send_keys("python")
        logging.debug("found searchbox and typed python")
        time.sleep(2)


s = Switchtoiframe()
s.switch_to_iframe()