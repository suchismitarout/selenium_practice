from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class Radiocheck():
    def radio_and_check_button(self):
        driver = webdriver.Chrome(executable_path="D:/drivers/chromedriver.exe")
        driver.get("https://letskodeit.teachable.com/p/practice")
        driver.maximize_window()
        benz_button = driver.find_element(By.ID,"benzradio")
        benz_button.click()

        bmw_button = driver.find_element(By.ID,"bmwradio")
        bmw_button.click()

        bmw_chekcbox = driver.find_element(By.ID,"bmwcheck")
        bmw_chekcbox.click()

        benz_checkbox = driver.find_element(By.ID,"benzcheck")
        benz_checkbox.click()

        honda_checkbox = driver.find_element(By.ID,"hondacheck")
        honda_checkbox.click()

        print("benz checkbox selected ?" + str(benz_checkbox.is_selected()))
        print("bmw checkbox selected?" + str(bmw_chekcbox.is_selected()))
        print("bmw button clicked ?" + str(bmw_button.is_selected()))
        print("honda checkbox selected ?" + str(honda_checkbox.is_selected()))
        time.sleep(2)

r = Radiocheck()
r.radio_and_check_button()