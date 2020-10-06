from selenium import webdriver
import time

class Browserinteraction():
    def testelements(self):
        driver = webdriver.Chrome(executable_path="D:/drivers/chromedriver.exe")
        url = "https://letskodeit.teachable.com/p/practice"
        driver.get(url)
        #Maximize the window
        driver.maximize_window()
        #Minimize the window
        driver.minimize_window()
        #print web-page title
        print("web page title is: ", driver.title)
        #print current page url
        print("current page is: ", driver.current_url)
        #Refresh the page
        driver.refresh()
        #Open another url
        driver.get("https://dhtmlx.com/docs/products/dhtmlxGrid/")
        #Go to previous page
        driver.back()
        # Go to next page
        driver.forward()
        #Close current page
        driver.close()

b = Browserinteraction()
b.testelements()