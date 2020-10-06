from selenium import webdriver
import time
import logging

logging.basicConfig(level=logging.DEBUG)

class Switchwindow():
    def switch_to_window(self):
        driver = webdriver.Chrome(executable_path="D:/drivers/chromedriver.exe")
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.maximize_window()

        #get current handle
        current_handle = driver.current_window_handle
        logging.debug("current handle: " + current_handle)

        #click window_button
        window_button = driver.find_element_by_id("openwindow")
        window_button.click()
        time.sleep(2)

        #get all handles
        handles = driver.window_handles
        for handle in handles:
            logging.debug("handle: " + handle)
            if handle not in current_handle:
                driver.switch_to.window(handle)
                present_handle = driver.current_window_handle
                logging.debug("present handle is: " + present_handle)
                searchbox = driver.find_element_by_id("search-courses")
                searchbox.send_keys("python")
                time.sleep(2)
                driver.close()
                break

        #go back to previous window
        driver.switch_to.window(current_handle)
        handle1 = driver.current_window_handle
        logging.debug("Now the handle is: " + handle1)
        driver.find_element_by_id("displayed-text").send_keys("python")
        time.sleep(2)
s = Switchwindow()
s.switch_to_window()
