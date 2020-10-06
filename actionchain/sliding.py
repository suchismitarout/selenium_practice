from selenium import webdriver
import time
from selenium.webdriver import  ActionChains

class Sliding():
    def working_with_slider(self):
        driver = webdriver.Chrome(executable_path="D:/drivers/chromedriver.exe")
        driver.get("https://jqueryui.com/slider/")
        driver.maximize_window()

        #switch to frame
        driver.switch_to.frame(0)

        #move slider
        slider = driver.find_element_by_xpath("//div[@id='slider']/span")
        ele = ActionChains(driver)
        ele.drag_and_drop_by_offset(slider,500,0).perform()
        time.sleep(2)

s = Sliding()
s.working_with_slider()


