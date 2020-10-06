from selenium import webdriver
import time

class Working_with_hidden_element():
    def letskodeit(self):
        driver = webdriver.Chrome(executable_path='D:/drivers/chromedriver.exe')
        driver.get('https://letskodeit.teachable.com/p/practice')
        driver.maximize_window()
        #state of element
        element = driver.find_element_by_id('displayed-text')
        state_of_element = element.is_displayed()
        print("element visible ??" + str(state_of_element))

        #click hide button
        driver.find_element_by_id('hide-textbox').click()
        #state of element
        state_of_element = element.is_displayed()
        print("element visible ??" + str(state_of_element))

        #click show button
        driver.find_element_by_id('show-textbox').click()
        #state of element
        state_of_element = element.is_displayed()
        print("element visible ??" + str(state_of_element))

w = Working_with_hidden_element()
w.letskodeit()