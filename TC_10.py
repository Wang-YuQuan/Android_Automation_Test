import Global

def Test(session_driver, wait_driver):
    if(len(Global.FindElementsByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/layout_bus_dialog_negative_button']", "negative_button can't found", 0))>0):
        Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/layout_bus_dialog_negative_button']", "negative_button can't found", 0)
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@text='路線規劃']/..", "路線規劃 btn can't found")
    SubTest(session_driver, wait_driver, "弘光科技大學(專用道)", "市政府(專用道)", "7", "00")
    Global.ReturnPreviousPage(session_driver, wait_driver)

def SubTest(session_driver, wait_driver, res, dst, hour, minute):
    InputResource(session_driver, wait_driver, res)
    InputDestination(session_driver, wait_driver, dst)
    InputTime(session_driver, wait_driver, hour, minute)
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/ib_activity_direction_submit']", "submit btn can't found")
    header = Global.FindElementsByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/tv_listitem_direction_header']", "header not found")[0].get_attribute('text')
    timeStart = header[0:5]
    result_hour = int(timeStart.split(':')[0])
    result_minute = int(timeStart.split(':')[1])
    assert result_hour>=int(hour), "result hour not in the range."
    assert result_minute>=int(minute), "result minute not in the range."

def InputResource(session_driver, wait_driver, res):
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/fragment_activity_direction_src']", "input area can't found")
    Global.FindElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/ed_search_bar_input']", "text can't found").send_keys(res)
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/tv_listitem_place_search_name']/..", "stop can't found")

def InputDestination(session_driver, wait_driver, dst):
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/fragment_activity_direction_dst']", "input area can't found")
    Global.FindElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/ed_search_bar_input']", "text can't found").send_keys(dst)
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/tv_listitem_place_search_name']/..", "stop can't found")

def InputTime(session_driver, wait_driver, hour, minute):
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/tv_activity_direction_time']", "time btn area can't found")
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@content-desc='{0} 點']".format(hour), "hour area can't found")
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@content-desc='{0} 分']".format(minute), "minute area can't found")
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/material_timepicker_ok_button']", "submit btn can't found")