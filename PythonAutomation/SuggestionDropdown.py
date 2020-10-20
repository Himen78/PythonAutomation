import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\PythonSelenium\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.makemytrip.com/") #Get method to hit URL on browser.

driver.find_element_by_css_selector("li[data-cy='oneWayTrip']").click()
driver.find_element_by_id("fromCity").click()
driver.find_element_by_css_selector("input[placeholder='From']").send_keys("del")
time.sleep(2)
cities = driver.find_elements_by_css_selector("p[class*='blackText']")
print(len(cities))
for city in cities:
    if city.text == "Delhi, India":
        city.click()
        break
