import pytest
from pytest_bdd import given, when, then, parsers, scenarios
from conftest import user_credentials
from pageObjects.login import LoginPage
from utils.apiBaseFramework import APIUtils

#point to the correct feature file
scenarios('features/orderTransaction.feature')

#initialize an empty dictionary for variables that we need to reuse within methods below
@pytest.fixture
def shared_data():
    return {}

#{} used for feeding the username and pass from the gherkin scenario outline
#using bdd parsers so that given can know about the variables injected
@given(parsers.parse('place the item order with {username} and {password}'))
def place_item_order(playwright, username, password, shared_data):
    #create a dictionary and fill it with username and password bec item order requries it
    #in the way it is currently implemented(to receive from JSON file)
    user_credentials = {}
    user_credentials["userEmail"] = username
    user_credentials["userPassword"] = password
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright, user_credentials)
    #loading the fixture dictionary with order id
    shared_data['order_id'] = orderId

@given('user is on landing page')
def user_on_landing_page(browserInstance, shared_data):#browserInstane is coming from confTest as usual
    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    #loading the fixture dictionary with login page
    shared_data['login_page'] = loginPage

#using bdd parsers so that given can know about the variables injected
@when(parsers.parse('I login to portal with {username} and {password}'))
def login_to_portal(username, password, shared_data):
    loginPage = shared_data['login_page']
    dashboardPage = loginPage.login(username, password)
    #loading the fixture dictionary with dashboard page
    shared_data['dashboard_page'] = dashboardPage

@when('navigate to orders page')
def navigate_to_orders_page(shared_data):
    dashboardPage = shared_data['dashboard_page']
    orderHistoryPage = dashboardPage.selectOrdersNavLink()
    shared_data['orderHistory_page'] = orderHistoryPage

@when('select the orderId')
def select_order_id(shared_data):
    orderHistoryPage = shared_data['orderHistory_page']
    orderId = shared_data['order_id']
    orderDetailsPage = orderHistoryPage.selectOrder(orderId)
    shared_data['orderDetails_page'] = orderDetailsPage

@then('order message is successfully displayed')
def order_message_successfully_displayed(shared_data):
    orderDetailsPage = shared_data['orderDetails_page']
    orderDetailsPage.verifyOrderMessage()