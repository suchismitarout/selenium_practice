from selenium import webdriver
import time
def google_browser():
    driver=webdriver.Chrome(executable_path="D:/drivers/chromedriver.exe")
    driver.get("https://www.google.com/")
    driver.maximize_window()
    time.sleep(2)
    driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").send_keys("bangalore")
    time.sleep(2)
g=google_browser()