# 從appium套件 引用 webdriver模組
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import TestCase

# 定義Desired Capabilities需求設定內容desired_caps變數，為key-value的字典資料型態
desired_caps = dict()
# 平台名，不分大小寫
desired_caps['platformName'] = 'Android'
# 版本可寫7.1.2 或 7.1
desired_caps['platformVersion'] = '9.0'
# 設備名，可寫 emulator-5554 或 IP:Port，但不能留空
desired_caps['deviceName'] = 'emulator-5554'
# 要啟動的APP的Package名
desired_caps['appPackage'] = 'nexti.android.bustaichung'
# 要啟動的APP的介面名
desired_caps['appActivity'] = 'com.oath.mobile.client.android.abu.bus.dashboard.SplashActivity'
# 自動授予所有權限
desired_caps['autoGrantPermissions'] = True
# 程式將Desired Capabilities這一包設定內容Post給Appium Server後，Server建立session與產生唯一的session id
# 建立webdriver.Remote類別的物件session_driver，session_driver就會包含session id
# print(session_driver)會印出類似"<appium.webdriver.webdriver.WebDriver (session="5cdf0a23-ea07-49ea-ad78-e3f841d05e6c")>"得內容
session_driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
wait_driver = WebDriverWait(session_driver, 5)

TestCase.TC_01.Test(session_driver, wait_driver)
TestCase.TC_02.Test(session_driver, wait_driver)
TestCase.TC_03.Test(session_driver, wait_driver)
TestCase.TC_04.Test(session_driver, wait_driver)
TestCase.TC_05.Test(session_driver, wait_driver)
TestCase.TC_06.Test(session_driver, wait_driver)
TestCase.TC_07.Test(session_driver, wait_driver)
TestCase.TC_08.Test(session_driver, wait_driver)
TestCase.TC_09.Test(session_driver, wait_driver)
TestCase.TC_10.Test(session_driver, wait_driver)
TestCase.TC_11.Test(session_driver, wait_driver)
TestCase.TC_12.Test(session_driver, wait_driver)
TestCase.TC_13.Test(session_driver, wait_driver)
TestCase.TC_14.Test(session_driver, wait_driver)
TestCase.TC_15.Test(session_driver, wait_driver)

time.sleep(1)
session_driver.quit()