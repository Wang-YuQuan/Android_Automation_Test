import Global
import time

def Test(session_driver, wait_driver):
    default_number = "56"
    default_car_number = "761-U8"
    if(len(Global.FindElementsByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/layout_bus_dialog_negative_button']", "negative_button can't found", 0))>0):
        Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/layout_bus_dialog_negative_button']", "negative_button can't found", 0)
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@text='公車追蹤']/parent::*", "公車追蹤 btn can't found")
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/menu_tracker_add']", "add btn can't found")
    Global.FindElementsByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/ed_layout_bus_input']", "text can't found")[0].send_keys(default_number)
    Global.FindElementsByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/ed_layout_bus_input']", "text can't found")[1].send_keys(default_car_number)
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@text='儲存']", "save btn can't found")
    time.sleep(2)
    ClickCancel(session_driver, wait_driver)
    bus_number = '761-U8'
    SubTest(session_driver, wait_driver, "", "", '公車離線')
    SubTest(session_driver, wait_driver, "", bus_number, '公車離線')
    SubTest(session_driver, wait_driver, "", "88888", '公車離線')
    SubTest(session_driver, wait_driver, "1", "", '公車離線')
    SubTest(session_driver, wait_driver, "1", bus_number, '行駛中')
    SubTest(session_driver, wait_driver, "1", "88888", '公車離線')
    SubTest(session_driver, wait_driver, "56", "", '公車離線')
    SubTest(session_driver, wait_driver, "56", bus_number, '行駛中')
    SubTest(session_driver, wait_driver, "56", "88888", '公車離線')
    SubTest(session_driver, wait_driver, "1"*35, "", '公車離線')
    SubTest(session_driver, wait_driver, "1"*35, bus_number, '行駛中')
    SubTest(session_driver, wait_driver, "1"*35, "88888", '公車離線')
    SubTest(session_driver, wait_driver, "1"*36, "", '公車離線')
    SubTest(session_driver, wait_driver, "1"*36, bus_number, '公車離線')
    SubTest(session_driver, wait_driver, "1"*36, "88888", '公車離線')
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/text_busid']/parent::*", "btn can't found")
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@text='刪除追蹤公車']/parent::*", "btn can't found")
    Global.ReturnPreviousPage(session_driver, wait_driver)

def SubTest(session_driver, wait_driver, stop_number, car_number, compare=""):
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/text_busid']/parent::*", "btn can't found")
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@text='修改追蹤公車']/parent::*", "btn can't found")
    Global.FindElementsByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/ed_layout_bus_input']", "text can't found")[0].send_keys(stop_number)
    Global.FindElementsByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/ed_layout_bus_input']", "text can't found")[1].send_keys(car_number)

    if(stop_number=="" or car_number=="" or len(stop_number)>35):
        status = Global.FindElementByXpath(session_driver, wait_driver, "//*[@text='儲存']", "save btn can't found").get_attribute('enabled')
        assert status=="false", "status suhold be disabled."
        Global.ClickElementByXpath(session_driver, wait_driver, "//*[@text='取消']", "caancel btn can't found")
    else:
        Global.ClickElementByXpath(session_driver, wait_driver, "//*[@text='儲存']", "save btn can't found")
        time.sleep(2)
        ClickCancel(session_driver, wait_driver)
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

def ClickCancel(session_driver, wait_driver):
    if(len(Global.FindElementsByXpath(session_driver, wait_driver, "//*[@text='下次再說']", "negative_button can't found", 0))>0):
            Global.ClickElementByXpath(session_driver, wait_driver, "//*[@text='下次再說']", "negative_button can't found")