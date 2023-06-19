import Global
import time

def Test(session_driver, wait_driver):
    if(len(Global.FindElementsByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/layout_bus_dialog_negative_button']", "negative_button can't found", 0))>0):
        Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/layout_bus_dialog_negative_button']", "negative_button can't found", 0)
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@text='路線規劃']/..", "路線規劃 btn can't found")
    SubTest(session_driver, wait_driver, "弘光科技大學(專用道)", "市政府(專用道)", 1)
    SubTest(session_driver, wait_driver, "弘光科技大學(專用道)", "臺中高工(高工路)", 2)
    SubTest(session_driver, wait_driver, "弘光科技大學(專用道)", "台灣高鐵(雲林站)", 3)
    Global.ReturnPreviousPage(session_driver, wait_driver)

def SubTest(session_driver, wait_driver, res, dst, turns):
    InputResource(session_driver, wait_driver, res)
    InputDestination(session_driver, wait_driver, dst)
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/ib_activity_direction_submit']", "submit btn can't found")
    result_turns = len(Global.FindElementsByXpath(session_driver, wait_driver, "//*[contains(@text, '搭乘')]", "text can't found"))
    assert result_turns==turns, "turns is not same."

def InputResource(session_driver, wait_driver, res):
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/fragment_activity_direction_src']", "input area can't found")
    Global.FindElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/ed_search_bar_input']", "text can't found").send_keys(res)
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/tv_listitem_place_search_name']/..", "stop can't found")

def InputDestination(session_driver, wait_driver, dst):
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/fragment_activity_direction_dst']", "input area can't found")
    Global.FindElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/ed_search_bar_input']", "text can't found").send_keys(dst)
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/tv_listitem_place_search_name']/..", "stop can't found")