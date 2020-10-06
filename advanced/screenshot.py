from selenium import webdriver
import time

class Screenshot():
    def take_screenshot(self):
        apt = webdriver.ChromeOptions()
        apt.add_argument("user-data-dir=C:/Users/Suchismita/AppData/Local/Google/Chrome/User Data/Profile 1")
        driver = webdriver.Chrome(executable_path="D:/drivers/chromedriver.exe", options=apt)
        driver.get("https://letskodeit.teachable.com")
        driver.maximize_window()

        login_button = driver.find_element_by_xpath("//a[@href='/sign_in']")
        login_button.click()
        time.sleep(2)

        user_mail = driver.find_element_by_id("user_email")
        user_mail.send_keys("test@gmail.com")

        passwd = driver.find_element_by_id("user_password")
        passwd.send_keys("test")

        submit_button = driver.find_element_by_name("commit")
        submit_button.click()

        dest_loc = "D:/screen.png"
        try:
            driver.save_screenshot(dest_loc)
            print("screenshot saved in location: " + dest_loc)
        except NotADirectoryError:
            print("Not a directory issue")

s = Screenshot()
s.take_screenshot()