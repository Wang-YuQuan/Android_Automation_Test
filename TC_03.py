import Global
import time
import Search_Bus_Automation.variable as search_bus_variable

def Test(session_driver, wait_driver):
    if(len(Global.FindElementsByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/layout_bus_dialog_negative_button']", "negative_button can't found", 0))>0):
        Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/layout_bus_dialog_negative_button']", "negative_button can't found", 0)
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/button_search']", "路線搜尋 btn can't found")
    SubTest(session_driver, wait_driver, "300", 0)
    Global.ReturnPreviousPage(session_driver, wait_driver)
    time.sleep(1)

def SubTest(session_driver, wait_driver, route, _type):
    search_bus_variable.InputBusRoute(session_driver, wait_driver, route)
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/tv_listitem_route_v2_name']/parent::*", "路線 can't found")
    bus_list = search_bus_variable.ReturnBusStops(route, 0, _type)
    scroll_times = (len(bus_list)//7)+1
    while(scroll_times>0):
        elements = Global.FindElementsByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/text_stopname']", "stop name can't found")
        for element in elements:
            assert element.get_attribute('name') in bus_list, "busStop not in a correct stop"
        element = Global.FindElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/rv_fragment_stops']", "scroll view can't found")
        session_driver.swipe(0, 1548, 0, 372, 1000)
        scroll_times -= 1
        time.sleep(1)
    Global.ReturnPreviousPage(session_driver, wait_driver)
    search_bus_variable.ClickButtonByText(session_driver, wait_driver, "重設")