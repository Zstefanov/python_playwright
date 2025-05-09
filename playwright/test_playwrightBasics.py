import time

from playwright.sync_api import Page, Playwright, expect, sync_playwright


def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https:/rahulshettyacademy.com")

#chroium, headless only, 1 context -> otherwise we need to customize
def test_playwrightShortcut(page: Page):
    page.goto("https:/rahulshettyacademy.com")

#css locator for id => #terms (# for id)
#css locator for class_name -> .text-info (dot for class name)
#css locator with tag_name
def test_coreLocators(page: Page):
    page.goto("https:/rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("wrongPassword")
    page.get_by_role("combobox").select_option("teach")
    #css locator for checkbox by id
    page.locator("#terms").check()
    #page.get_by_role("link", name = "terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    #Incorrect username/password. - assert if we receive the error
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

def test_firefoxBrowser(playwright: Playwright):
    browser = playwright.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https:/rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("wrongPassword")
    page.get_by_role("combobox").select_option("teach")
    # css locator for checkbox by id
    page.locator("#terms").check()
    # page.get_by_role("link", name = "terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    # Incorrect username/password. - assert if we receive the error
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()


