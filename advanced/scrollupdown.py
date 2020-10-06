from selenium import webdriver
import time

class Scrollupdown():
    def scroll_up_down(self):
        driver = webdriver.Chrome(executable_path="D:/drivers/chromedriver.exe")
        driver.get("https://letskodeit.teachable.com/p/practice")
        driver.maximize_window()

        driver.execute_script("window.scrollBy(0, 3000);")
        time.sleep(2)

        driver.execute_script("window.scrollBy(0, -3000);")
        time.sleep(2)

        ele = driver.find_element_by_id("mousehover")
        driver.execute_script("arguments[0].scrollIntoView(true);",ele)
        time.sleep(2)
        

s = Scrollupdown()
s.scroll_up_down()