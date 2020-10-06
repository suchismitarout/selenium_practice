from selenium import webdriver
import time

class Calenderwork():
    def working_with_calender1(self):
        driver=webdriver.Chrome(executable_path="D:/drivers/chromedriver.exe")
        driver.get("https://www.expedia.com/")
        driver.maximize_window()

        #click flight tab
        driver.find_element_by_id("tab-flight-tab-hp").click()
        time.sleep(2)

        #click on Departing tab
        driver.find_element_by_id("flight-departing-hp-flight").click()

        #choose date
        date = driver.find_element_by_xpath("//div[@class='datepicker-cal-month'][position()=1]//tbody//button[@data-day='30']")
        date.click()
        time.sleep(2)

    def working_with_calender2(self):
        driver = webdriver.Chrome(executable_path="D:/drivers/chromedriver.exe")
        driver.get("https://www.goibibo.com/")
        driver.maximize_window()


        # click on Departing tab
        driver.find_element_by_id("departureCalendar").click()
        time.sleep(2)


        date_list = driver.find_elements_by_xpath("//div[@class='DayPicker-Body']//div[@aria-disabled='false']")
        time.sleep(2)

        for date in date_list:
            if date.text == "30":
                date.click()
                time.sleep(2)
                break


c= Calenderwork()
c.working_with_calender2()
