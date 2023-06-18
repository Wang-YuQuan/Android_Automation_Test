import Global
import time

def Test(session_driver, wait_driver):
    if(len(Global.FindElementsByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/layout_bus_dialog_negative_button']", "negative_button can't found", 0))>0):
        Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/layout_bus_dialog_negative_button']", "negative_button can't found", 0)
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@text='公車追蹤']/parent::*", "公車追蹤 btn can't found")
    SubTest(session_driver, wait_driver, "56", "342-FZ", '公車離線')
    Global.ReturnPreviousPage(session_driver, wait_driver)

def SubTest(session_driver, wait_driver, stop_number, car_number, compare=""):
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/menu_tracker_add']", "add btn can't found")
    Global.FindElementByXpath(session_driver, wait_driver, "//*[@text='名稱']", "text can't found").send_keys(stop_number)
    Global.FindElementByXpath(session_driver, wait_driver, "//*[@text='車牌號碼']", "text can't found").send_keys(car_number)
    if(stop_number=="" or car_number==""):
        status = Global.FindElementByXpath(session_driver, wait_driver, "//*[@text='儲存']", "save btn can't found").get_attribute('enabled')
        assert status=="false", "status suhold be disabled."
        Global.ClickElementByXpath(session_driver, wait_driver, "//*[@text='取消']", "caancel btn can't found")
    else:
        Global.ClickElementByXpath(session_driver, wait_driver, "//*[@text='儲存']", "save btn can't found")
        time.sleep(2)
        if(len(Global.FindElementsByXpath(session_driver, wait_driver, "//*[@text='下次再說']", "negative_button can't found", 0))>0):
            Global.ClickElementByXpath(session_driver, wait_driver, "//*[@text='下次再說']", "negative_button can't found")
        expect_bus = car_number
        expect_stop = stop_number
        expect_status = '公車離線'
        result_bus = Global.FindElementByXpath(session_driver, wait_driver, "//*[@text='{0}']".format(car_number), "text can't found").get_attribute('text')
        result_stop = Global.FindElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/text_alias']", "text can't found").get_attribute('text')
        result_status = Global.FindElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/text_route']", "text can't found").get_attribute('text')
        assert expect_bus==result_bus, ""
        assert expect_stop==result_stop.replace(' ', ''), ""
        if(compare=='公車離線'):
            assert expect_status==result_status, ""
        else:
            assert expect_status!=result_status, ""
        Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/text_busid']/parent::*", "btn can't found")
        Global.ClickElementByXpath(session_driver, wait_driver, "//*[@text='刪除追蹤公車']/parent::*", "btn can't found")