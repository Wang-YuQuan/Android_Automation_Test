import Global
import time
import Search_Bus_Automation.variable as search_bus_variable

def Test(session_driver, wait_driver):
    if(len(Global.FindElementsByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/layout_bus_dialog_negative_button']", "negative_button can't found", 0))>0):
        Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/layout_bus_dialog_negative_button']", "negative_button can't found", 0)
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/button_search']", "路線搜尋 btn can't found")
    SubTest(session_driver, wait_driver, "300", 1)
    Global.ReturnPreviousPage(session_driver, wait_driver)
    time.sleep(1)

def SubTest(session_driver, wait_driver, route, isExist):
    search_bus_variable.InputBusRoute(session_driver, wait_driver, route)
    assert isExist==len(Global.FindElementsByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/tv_listitem_route_v2_name']/parent::*", "路線 can't found", isExist)), "路線 can't found"
    search_bus_variable.ClickButtonByText(session_driver, wait_driver, "重設")