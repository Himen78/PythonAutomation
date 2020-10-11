from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\PythonSelenium\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/angularpractice/") #Get method to hit URL on browser.

# driver.find_element_by_name("name").send_keys("Himen Patel")
driver.find_element_by_css_selector("input[name='name']").send_keys("Himen Patel")
driver.find_element_by_name("email").send_keys("himen@gmail.com")
driver.find_element_by_id("exampleInputPassword1").send_keys("Himen@123")
driver.find_element_by_id("exampleCheck1").click()

dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

driver.find_element_by_xpath("//input[@type='submit']").click()
print(driver.find_element_by_class_name("alert-success").text)
# //*[contains(@class,'alert-success')]


message = driver.find_element_by_class_name("alert-success").text

# How to use assertion in Python as below :
print(message)
assert "success" in message

driver.find_element_by_class_name("close").click()
driver.close()