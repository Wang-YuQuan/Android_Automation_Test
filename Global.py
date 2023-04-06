from selenium.webdriver.common.by import By

# 檢查元素是否存在，超過檢查時間未找到拋出異常
def WaitUntilElementAppearByXpath(session_driver, wait_driver, xpath, error_message):
    wait_driver.until(lambda lam1: session_driver.find_element(By.XPATH, xpath), error_message)

# type為0無須檢查元素是否存在
def ClickElementByXpath(session_driver, wait_driver, xpath, error_message, type=1):
    if type==1:
        WaitUntilElementAppearByXpath(session_driver, wait_driver, xpath, error_message)
    session_driver.find_element(By.XPATH, xpath).click()

# type為0無須檢查元素是否存在
def FindElementByXpath(session_driver, wait_driver, xpath, error_message, type=1):
    if type==1:
        WaitUntilElementAppearByXpath(session_driver, wait_driver, xpath, error_message)
    return session_driver.find_element(By.XPATH, xpath)

# type為0無須檢查元素是否存在
def FindElementsByXpath(session_driver, wait_driver, xpath, error_message, type=1):
    if type==1:
        WaitUntilElementAppearByXpath(session_driver, wait_driver, xpath, error_message)
    return session_driver.find_elements(By.XPATH, xpath)

def ReturnPreviousPage(session_driver, wait_driver):
    ClickElementByXpath(session_driver, wait_driver, "//*[@content-desc='向上瀏覽']", "上一頁 btn can't found")