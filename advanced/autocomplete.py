from selenium import webdriver
import time
import logging

logging.basicConfig(level=logging.DEBUG)


class Autocomplete():
    def auto_complete(self):
        driver = webdriver.Chrome(executable_path="D:/drivers/chromedriver.exe")
        driver.get("https://www.makemytrip.com/")
        driver.maximize_window()

        # choose city from which you want to depart
        fromcity = driver.find_element_by_id("fromCity")
        fromcity.send_keys("mumbai")
        time.sleep(5)
        logging.debug("city input box selected")

        # choose the desired city

        city = driver.find_element_by_id('react-autowhatever-1-section-0-item-0')
        driver.execute_script("arguments[0].click();", city)
        logging.debug("found the city from dropdown and clicked")


auto = Autocomplete()
auto.auto_complete()
