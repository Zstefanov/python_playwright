import time
from playwright.sync_api import expect, Page


def test_UIValidationDynamicScript(page: Page):
    #iphone X, Nokia Edge -> verify that are added/showing in cart.
    page.goto("https:/rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    # css locator for checkbox by id
    page.locator("#terms").check()
    # page.get_by_role("link", name = "terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()

    #adding the 2 phones required to the cart and checkout
    iPhone = (page.locator("app-card").filter(has_text="iphone X").
              get_by_role("button").click())
    nokiaEdge = (page.locator("app-card").filter(has_text="Nokia Edge").
                 get_by_role("button").click())
    page.get_by_text("Checkout").click()
    #check the count of products added in the cart
    expect(page.locator(".media-body")).to_have_count(2)

    time.sleep(10)

def test_childWindowHandle(page: Page):
    page.goto("https:/rahulshettyacademy.com/loginpagePractise")
    with page.expect_popup() as newPage:
        page.locator(".blinkingText").click()  # new page
        childPage = newPage.value
        text = childPage.locator(".red").text_content()
        print(text)
        words = text.split("at ")
        email = words[1].split(" ")[0]
        assert email == "mentor@rahulshettyacademy.com"

