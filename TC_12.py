import Global
import time
import Search_Bus_Automation.variable as search_bus_variable

def Test(session_driver, wait_driver):
    if(len(Global.FindElementsByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/layout_bus_dialog_negative_button']", "negative_button can't found", 0))>0):
        Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/layout_bus_dialog_negative_button']", "negative_button can't found", 0)
    SubTest(session_driver, wait_driver, "To Be Tested")
    Global.ReturnPreviousPage(session_driver, wait_driver)

def SubTest(session_driver, wait_driver, group_name):
    stop_name = CreateStopGroup(session_driver, wait_driver, group_name)
    VerifyCreateGroupExist(session_driver, wait_driver, group_name, stop_name)
    DeleteGroup(session_driver, wait_driver)

def CreateStopGroup(session_driver, wait_driver, group_name):
    default_route = "300"
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/button_search']", "路線搜尋 btn can't found")
    search_bus_variable.InputBusRoute(session_driver, wait_driver, default_route)
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/tv_listitem_route_v2_name']/parent::*", "路線 can't found")
    stop_name = Global.FindElementsByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/text_stopname']", "路線 can't found")[0].get_attribute('text')
    Global.FindElementsByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/text_stopname']/../../..", "路線 can't found")[0].click()
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@text='加入常用站牌']", "加入常用站牌 can't found")
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/rb_listitem_stop_add_new_group']", "add can't found")
    Global.FindElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/ed_layout_bus_input']", "input can't found").send_keys(group_name)
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='android:id/button1']", "確定 can't found")
    Global.ReturnPreviousPage(session_driver, wait_driver)
    Global.ReturnPreviousPage(session_driver, wait_driver)
    return stop_name

def VerifyCreateGroupExist(session_driver, wait_driver, group_name, stop_name):
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@text='常用站牌']/..", "常用站牌 btn can't found")
    time.sleep(1)
    session_driver.swipe(0, 679, 0, 1824, 1000)
    group_len = len(Global.FindElementsByXpath(session_driver, wait_driver, "//*[@text='{0}']".format(group_name), "group_name can't found"))
    stop_len = len(Global.FindElementsByXpath(session_driver, wait_driver, "//*[@text='{0}']".format(stop_name), "stop_name can't found"))
    assert group_len!=0, "group_len should not be 0"
    assert stop_len!=0, "stop_len should not be 0"

def DeleteGroup(session_driver, wait_driver):
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@content-desc='更多選項']", "更多選項 btn can't found")
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@text='管理群組']/../../..", "管理群組 btn can't found")
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@text='全選']", "全選 btn can't found")
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@text='刪除']", "刪除 btn can't found")
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@text='刪除']", "刪除 dialog btn can't found")
    time.sleep(1)
    session_driver.swipe(0, 679, 0, 1824, 1000)