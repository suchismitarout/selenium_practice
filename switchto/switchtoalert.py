from selenium import webdriver
import time
import logging

logging.basicConfig(level=logging.DEBUG)

class Switchtoalert():
    def switch_to_alert(self):
        driver = webdriver.Chrome(executable_path="D:/drivers/chromedriver.exe")
        driver.get("https://letskodeit.teachable.com/p/practice")
        driver.maximize_window()
        time.sleep(2)

        #find searchbox for alert
        driver.find_element_by_id("name").send_keys("suchi")
        driver.find_element_by_id("alertbtn").click()
        logging.debug("searchbox found for alert")
        time.sleep(2)

        #switch to alert popup
        alert_button = driver.switch_to.alert
        alert_button.accept()
        time.sleep(2)
        logging.debug("alert popup closed")

        #find searchbox for confirm
        driver.find_element_by_id("name").send_keys("dpk")
        driver.find_element_by_id("confirmbtn").click()
        logging.debug("searchbox found for confirm")
        time.sleep(2)

        #switch to confirm popup
        confirm_button = driver.switch_to.alert
        confirm_button.dismiss()
        time.sleep(2)
        logging.debug("cancelled the confirm popup")


s = Switchtoalert()
s.switch_to_alert()