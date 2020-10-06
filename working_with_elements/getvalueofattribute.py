from selenium import  webdriver
import time

class GetattributeValue():
    def get_value_of_attribute(self):
        driver = webdriver.Chrome(executable_path='D:/drivers/chromedriver.exe')
        driver.get('https://letskodeit.teachable.com/p/practice')
        driver.maximize_window()

        element = driver.find_element_by_id('name')
        print(element.get_attribute('type'))

        button_ele = driver.find_element_by_id('bmwradio')
        print(button_ele.get_attribute('value'))

g = GetattributeValue()
g.get_value_of_attribute()