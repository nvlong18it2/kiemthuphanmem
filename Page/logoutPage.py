def LogOut(browser):
    
    btnNavbar = browser.find_element_by_xpath("/html/body/header/nav/div[2]/ul/li[3]/a")
    btnNavbar.click()
