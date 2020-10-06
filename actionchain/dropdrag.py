from selenium import webdriver
import time
from selenium.webdriver import  ActionChains
import logging
logging.basicConfig(level=logging.DEBUG)

class Dropdrag():
    def drop_and_drag(self):
        driver = webdriver.Chrome(executable_path="D:/drivers/chromedriver.exe")
        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()
        time.sleep(2)

        #switch to dragdrop frame
        driver.switch_to.frame(0)
        source_ele = driver.find_element_by_id("draggable")
        dest_ele = driver.find_element_by_id("droppable")

        #drag and drop element
        action = ActionChains(driver)
        action.drag_and_drop(source_ele,dest_ele).perform()
        time.sleep(2)

d = Dropdrag()
d.drop_and_drag()