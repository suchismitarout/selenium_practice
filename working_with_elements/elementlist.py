from selenium import webdriver
import time

class Elementlist():
    def element_list(self):
        driver=webdriver.Chrome(executable_path="D:/drivers/chromedriver.exe")
        driver.get('https://letskodeit.teachable.com/p/practice')
        driver.maximize_window()

        list_of_elements=driver.find_elements_by_xpath("//div[@id='radio-btn-example']//input")
        size = len(list_of_elements)
        print("size of list is "+ str(size))
        for element in list_of_elements:
            element.click()
            time.sleep(1)


e = Elementlist()
e.element_list()