from selenium import webdriver
import time

class Clicksend():
    def click_and_send(self):
        apt = webdriver.ChromeOptions()
        apt.add_argument("user-data-dir=C:/Users/Suchismita/AppData/Local/Google/Chrome/User Data/Profile 1")
        driver = webdriver.Chrome(executable_path="D:/drivers/chromedriver.exe",options=apt)
        driver.get("https://letskodeit.teachable.com")
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//a[@class='navbar-link fedora-navbar-link']").click()
        driver.find_element_by_id('user_email').send_keys("test")
        driver.find_element_by_id('user_password').send_keys("test")
        time.sleep(2)
        driver.find_element_by_id('user_email').clear()
        driver.find_element_by_id('user_password').clear()

c = Clicksend()
c.click_and_send()
