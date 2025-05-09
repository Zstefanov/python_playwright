from playwright.sync_api import Playwright, expect
from utils.apiBase import APIUtils



# THIS WHOLE TEST IS REFACTORED IN TEST_FRAMEWORK_WEB_API
def test_e2e_web_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #create order -> orderId
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright)
    #login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("asddsa@asd.com")
    page.get_by_placeholder("enter your passsword").fill("Pa55word")
    page.get_by_role("button", name="Login").click()

    page.get_by_role("button", name="ORDERS").click()

    #orders History page-> order is present.
    row = page.locator("tr").filter(has_text=orderId)
    row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()

