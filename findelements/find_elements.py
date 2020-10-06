from selenium import webdriver

def setup():
    driver = webdriver.Chrome(executable_path="D:/drivers/chromedriver.exe")

    return driver

driver = setup()
base_url = "https://letskodeit.teachable.com/p/practice"
class Find_elements():
    def find_element_by_id(self):
        driver.get(base_url)
        element_by_id = driver.find_element_by_id("name")
        if element_by_id is not None:
            print("element found by id")
        else:
            print("element not found")
    def find_element_by_name(self):
        driver.get(base_url)
        element_by_name = driver.find_element_by_name("show-hide")
        if element_by_name is not None:
            print("element found by name")
        else:
            print("element not found")
    def find_element_by_link_text(self):
        driver.get(base_url)
        element_by_link_text = driver.find_element_by_link_text("Login")
        if element_by_link_text is not None:
            print("element found by link-text")
        else:
            print("element not found")
    def find_element_by_partial_link_text(self):
        driver.get(base_url)
        element_by_partial_link_text = driver.find_element_by_partial_link_text("Log")
        if element_by_partial_link_text is not None:
            print("element found by partial_link_text")
        else:
            print("element not found")
    def find_element_by_xpath(self):
        driver.get(base_url)
        element_by_xpath = driver.find_element_by_xpath("//input[@id='displayed-text']")
        if element_by_xpath is not None:
            print("element found by xpath")
        else:
            print("element not found")

    def find_element_by_css_selector(self):
        driver.get(base_url)
        element_by_css_selector = driver.find_element_by_css_selector("#alertbtn")
        if element_by_css_selector is not None:
            print("element found by css-selector")
        else:
            print("element not found")

    def find_element_by_tag(self):
        driver.get(base_url)
        element_by_tag = driver.find_element_by_tag_name("h1")
        if element_by_tag is not None:
            print("element found by tag is : ", element_by_tag.text)

    def find_elements_by_tag(self):
        driver.get(base_url)
        elementlist_by_tag = driver.find_elements_by_tag_name("td")
        print("length of list is", len(elementlist_by_tag))

    def find_element_by_classname(self):
        driver.get(base_url)
        element_by_classname = driver.find_element_by_class_name("displayed-class")
        element_by_classname.send_keys("testing")

    def find_elements_by_classname(self):
        driver.get(base_url)
        elements_by_classname = driver.find_elements_by_class_name("inputs")
        print("length of list is ", len(elements_by_classname))

f = Find_elements()
f.find_elements_by_tag()


