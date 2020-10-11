from selenium import webdriver

# Browser exposes an executable file.
# Through selenium test we need to invoke executable file which will then invoke actual browser.

driver = webdriver.Chrome(executable_path="C:\\PythonSelenium\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.google.com/") #Get method to hit URL on browser.

print(driver.title)  #fetch the title from page.
print(driver.current_url) #Fetch the current url from page.

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.back()
driver.refresh()
driver.close()