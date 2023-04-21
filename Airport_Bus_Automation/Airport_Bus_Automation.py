import Global

def Test(session_driver, wait_driver):
    if(len(Global.FindElementsByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/layout_bus_dialog_negative_button']", "negative_button can't found", 0))>0):
        Global.ClickElementByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/layout_bus_dialog_negative_button']", "negative_button can't found", 0)
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@text='機場客運']/parent::*", "機場客運 btn can't found")
    Global.ClickElementByXpath(session_driver, wait_driver, "//*[@text='臺中國際機場']/parent::*/parent::*", "臺中國際機場 btn can't found")
    '''for element in session_driver.find_elements(By.XPATH, "//*[@resource-id='nexti.android.bustaichung:id/recycler_view']//android.widget.LinearLayout"):
        
    '''
    Global.ReturnPreviousPage(session_driver, wait_driver)