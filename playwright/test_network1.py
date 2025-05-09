import pytest
from playwright.sync_api import Page

fakePayloadResponse = {"data": [], "message": "No Orders"}
#-> api call from browser -> api call contact server returns response ->
#browser uses response to generate HTML, mocking 0 orders on the order page

def intercept_response(route):
    route.fulfill(
        json=fakePayloadResponse
    )


#mock empty orders page via intecepting response with json
def test_Network1(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*",
               intercept_response)
    page.get_by_placeholder("email@example.com").fill("asddsa@asd.com")
    page.get_by_placeholder("enter your passsword").fill("Pa55word")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click() #routed on this step
    order_text = page.locator(".mt-4").text_content()
    print(order_text)