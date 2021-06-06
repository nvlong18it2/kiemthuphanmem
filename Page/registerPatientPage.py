def RegisterPatient(browser):
    browser.get(" https://demo.openmrs.org/openmrs/login.htm")

    txtUser = browser.find_element_by_id("username")
    txtUser.send_keys(username) # <---  Điền username thật của các bạn vào đây

    txtPass = browser.find_element_by_id("password")
    txtPass.send_keys(password)

    btnLocation = browser.find_element_by_id("Inpatient Ward")
    btnLocation.click()

    btnSubmit = browser.find_element_by_id("loginButton")
    btnSubmit.click()

    # txtPass.send_keys(Keys.ENTER)
    # sleep(3)

    # browser.close()