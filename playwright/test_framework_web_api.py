import json
import pytest

from playwright.sync_api import Playwright, expect
from pageObjects.login import LoginPage
from pageObjects.dashboard import DashboardPage
from utils.apiBaseFramework import APIUtils

#pytest --browser_name chrome -m smoke -n 3 --tracing on --html=report.html
#pytest --tracing on/off/retain-on-failure
#JENKINS -> c
            #pytest --browser_name chrome --tracing on --html=report.html

# JSON file
with open('data/credentials.json') as f:
    test_data = json.load(f)
    print(test_data)  # dictionary
    user_credentials_list = test_data['user_credentials']  # list with 2 items

#parametrize with different data sets coming from credentials.JSON
@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_e2e_web_api(playwright: Playwright, browserInstance, user_credentials):
    username = user_credentials["userEmail"]
    password = user_credentials["userPassword"]

    #create order -> orderId
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright, user_credentials)
    #login
    loginPage = LoginPage(browserInstance) #object for LoginPage class
    loginPage.navigate()
    #below dashboard page we catch as we are directed to it upon login
    dashboardPage = loginPage.login(username, password)

    #dashboard page
    orderHistoryPage = dashboardPage.selectOrdersNavLink()
    orderDetailsPage = orderHistoryPage.selectOrder(orderId)
    orderDetailsPage.verifyOrderMessage()

