from selenium.webdriver.common.by import By
import requests
import sys
sys.path.append("d:\\Android_Automation_Test")
import Global

client_id = 't108590031-7e119b3c-0826-4c72'
client_secret = 'e42def15-f424-4434-b0be-22cbfaf95a55'

class TDX():
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def get_token(self):
        token_url = 'https://tdx.transportdata.tw/auth/realms/TDXConnect/protocol/openid-connect/token'
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        data = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }
        response = requests.post(token_url, headers=headers, data=data)
        # print(response.status_code)
        # print(response.json())
        return response.json()['access_token']

    def get_response(self, url):
        headers = {'authorization': f'Bearer {self.get_token()}'}
        response = requests.get(url, headers=headers)
        return response.json()


def ReturnBusStops(routeID, direction, type):
    tdx = TDX(client_id, client_secret)
    bus_list = []

    base_url = "https://tdx.transportdata.tw/api"
    if(type==0):
        url = base_url + "/basic/v2/Bus/DisplayStopOfRoute/City/Taichung/{0}?%24filter=Direction%20eq%20%27{1}%27%20and%20RouteID%20eq%20%27{0}%27&%24top=100&%24format=JSON".format(routeID, direction)
    else:
        url = base_url + "/basic/v2/Bus/DisplayStopOfRoute/City/Taichung/{0}?%24filter=Direction%20eq%20%27{1}%27%20&%24top=100&%24format=JSON".format(routeID, direction)

    response = tdx.get_response(url)
    for stop in response[0]['Stops']:
       bus_list.append(stop['StopName']['Zh_tw'])
    return bus_list

def ClickButtonByText(session_driver, wait_driver, ch):
    for element in Global.FindElementsByXpath(session_driver, wait_driver, "//*[@resource-id='nexti.android.bustaichung:id/rsk_activity_route_search_keyboard']//*[@class='androidx.appcompat.widget.LinearLayoutCompat']", ch + " btn can't found"):
        for button in element.find_elements(By.XPATH, "//*[@class='android.widget.Button']"):
            if(button.get_attribute('name')==ch):
                button.click()

def InputBusRoute(session_driver, wait_driver, route):
    for ch in route:
        ClickButtonByText(session_driver, wait_driver, ch)