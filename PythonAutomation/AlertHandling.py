from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\PythonSelenium\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/") #Get method to hit URL on browser.

validateText = "Himen"

driver.find_element_by_css_selector("#name").send_keys(validateText)
driver.find_element_by_id("alertbtn").click()
alertBox = driver.switch_to.alert
alertText = alertBox.text
assert validateText in alertText
alertBox.accept()


