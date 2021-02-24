
# Selenium is a Python web automation tool. It allows us to script behaviors on a web browser. Say on google chrome,
# we can script it to simulate drags, click and etc.

# To setup selenium, we need to do the following:
#   -   Installing selenium package through pip
#   -   Having the corresponding web driver of the browser you prefer. Eg: Chrome webdriver

from selenium import webdriver

PATH = r"C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://www.google.com')    # Open a tab with URL given
print(driver.title)                     # Get the page's title by .title property
driver.close()                          # Closes the current tab only
driver.quit()                           # Closes the browser window