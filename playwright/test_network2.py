import pytest
from playwright.sync_api import Playwright, expect
from playwright.sync_api import Page

from utils.apiBase import APIUtils

fakePayloadResponse = {"data": [], "message": "No Orders"}

#intercepting a request with an invalid order to ensure no access
def interceptRequest(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-order-details-details?id=6711e249ae2afd4c0b9f6fb0")

@pytest.mark.smoke
def test_Network1(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*",
               interceptRequest)
    page.get_by_placeholder("email@example.com").fill("asddsa@asd.com")
    page.get_by_placeholder("enter your passsword").fill("Pa55word")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button",name="View").first.click() #routed to an unauthorized page
    errMessage = page.locator(".blink_me").text_content()
    print(errMessage)
    assert errMessage.__contains__("You are not authorize to view this order")

#avoiding login by providing token directly into localStorage
def test_session_storage(playwright: Playwright):
    api_utils = APIUtils()
    token = api_utils.getToken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #script to inject token into local sessions storage
    page.add_init_script(f"""localStorage.setItem('token', '{token}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()
