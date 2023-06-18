import Global
import time
import Search_Bus_Automation.variable as search_bus_variable

def Test(session_driver, wait_driver):
    if(len(Global.FindElementsByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/layout_bus_dialog_negative_button']", "negative_button can't found", 0))>0):
        Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/layout_bus_dialog_negative_button']", "negative_button can't found", 0)
    SubTest(session_driver, wait_driver)
    Global.ReturnPreviousPage(session_driver, wait_driver)

def SubTest(session_driver, wait_driver):
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@text='常用站牌']/..", "常用站牌 btn can't found")
    time.sleep(1)
    session_driver.swipe(0, 679, 0, 1824, 1000)
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@content-desc='更多選項']", "更多選項 btn can't found")
    time.sleep(1)
    error_msg = len(Global.FindElementsByXpath(session_driver, wait_driver, "//*[@text='至少需要建立一個以上的站牌或群組才能編輯噢']", "警告 can't found"))
    assert error_msg!=0, "警告msg is not appear"