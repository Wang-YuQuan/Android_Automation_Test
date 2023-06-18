import Global
import time

def Test(session_driver, wait_driver):
    default_number = "56"
    default_car_number = "677-FZ"
    if(len(Global.FindElementsByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/layout_bus_dialog_negative_button']", "negative_button can't found", 0))>0):
        Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/layout_bus_dialog_negative_button']", "negative_button can't found", 0)
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@text='公車追蹤']/parent::*", "公車追蹤 btn can't found")
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/menu_tracker_add']", "add btn can't found")
    Global.FindElementsByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/ed_layout_bus_input']", "text can't found")[0].send_keys(default_number)
    Global.FindElementsByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/ed_layout_bus_input']", "text can't found")[1].send_keys(default_car_number)
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@text='儲存']", "save btn can't found")
    time.sleep(2)
    ClickCancel(session_driver, wait_driver)
    SubTest(session_driver, wait_driver, default_car_number)
    Global.ReturnPreviousPage(session_driver, wait_driver)

def SubTest(session_driver, wait_driver, car_number):
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/text_busid']/parent::*", "btn can't found")
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@text='刪除追蹤公車']/parent::*", "btn can't found")
    time.sleep(1)
    result_bus_len = len(Global.FindElementsByXpath(session_driver, wait_driver, "//*[@text='{0}']".format(car_number), "text can't found", 0))
    result_stop_len = len(Global.FindElementsByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/text_alias']", "text can't found", 0))
    assert result_bus_len==0 and result_stop_len==0, "Bus should not be visible."

def ClickCancel(session_driver, wait_driver):
    if(len(Global.FindElementsByXpath(session_driver, wait_driver, "//*[@text='下次再說']", "negative_button can't found", 0))>0):
        Global.ClickElementByXpath(session_driver, wait_driver, "//*[@text='下次再說']", "negative_button can't found")