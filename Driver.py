# Using Chrome to access web
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
# Open the website and login
driver.get('https://als.royalholloway.ac.uk/Account/login')

username_box = driver.find_element_by_id('MainContent_SSLogin_txtUserName')
username_box.send_keys('')
password_box = driver.find_element_by_name('ctl00$MainContent$SSLogin$txtPassword')
password_box.send_keys('')
login_button = driver.find_element_by_name('ctl00$MainContent$SSLogin$btnLogin')
login_button.click()

# after logged in


timetable_button = driver.find_element_by_link_text("Timetable")
timetable_button.click()

submit_button = driver.find_element_by_id('MainContent_btnSubmit')
submit_button.click()

days_ahead_button = driver.find_element_by_id('MainContent_rpDays_dayLink_2')
days_ahead_button.click()


# ## check if Sunday is day, if so then do not book.
# third_day_in_slot = driver.find_element_by_id('MainContent_rpDays_dayLink_2')

# username identifier
# MainContent_SSLogin_txtUserName
# password identifier
# Signing into website:
