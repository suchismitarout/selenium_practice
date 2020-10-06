from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

class Dropdown():
    def drop_down_element(self):
        driver=webdriver.Chrome(executable_path='D:/drivers/chromedriver.exe')
        driver.get('https://letskodeit.teachable.com/p/practice')
        driver.maximize_window()
        dropdown_ele = driver.find_element_by_id('carselect')

        sel = Select(dropdown_ele)
        sel.select_by_value('benz')
        time.sleep(2)
        print("select by value")

        sel.select_by_index(2)
        time.sleep(2)
        print("select by index")

        sel.select_by_visible_text('BMW')
        time.sleep(2)
        print("select by visible text")

d = Dropdown()
d.drop_down_element()