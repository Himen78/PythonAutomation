from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\PythonSelenium\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get("https://login.salesforce.com/?locale=in") #Get method to hit URL on browser.
driver.find_element_by_css_selector("#username").send_keys("Himen") # we can use id as #idname in cssselector.
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(4)").text)
driver.find_element_by_css_selector(".password").send_keys("Patel")
driver.find_element_by_css_selector(".password").clear()
driver.find_element_by_link_text("Forgot Your Password?").click()
driver.find_element_by_xpath("//a[text()='Cancel']").click()

# Parent-child element : //form[@name='login']/div[1]

print("Passed successfully!")
