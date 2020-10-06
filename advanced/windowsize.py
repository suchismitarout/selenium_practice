from selenium import webdriver
import time

class Windowsize():
    def find_window_size(self):
        driver=webdriver.Chrome(executable_path="D:/drivers/chromedriver.exe")
        driver.get("https://letskodeit.teachable.com/p/practice")
        driver.maximize_window()
        time.sleep(1)

        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth")
        print("Height is: " + str(height))
        print("Width is: " + str(width))

w = Windowsize()
w.find_window_size()