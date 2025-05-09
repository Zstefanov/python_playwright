import time

from playwright.sync_api import Page, expect


def test_UIChecks(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

def test_AlertBox(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    #anon functions are created via lambda keyword, listening for the popup
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Confirm").click()
    time.sleep(5)

def test_iFrames(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    iFrame = page.frame_locator("#courses-iframe")
    iFrame.get_by_role("link", name="All Access plan").click()
    expect(iFrame.locator("body")).to_contain_text("Happy Subscibers")

def test_webTables(page: Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    #tagname all 3 table headers

    for index in range(page.locator("th").count()):
       if page.locator("th").nth(index).filter(has_text="Price").count()>0:
           colValue = index
           print(f"Price column value is {colValue}")
           break

    riceRow = page.locator("tr").filter(has_text="Rice")
    expect(riceRow.locator('td').nth(colValue)).to_have_text("37")

def test_mouseHover(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top").click()