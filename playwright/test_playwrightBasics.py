import time

from playwright.sync_api import Page, Playwright, expect


def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False) #headless false so you can visually see the execution in the browser
    # an alternate is to add a runtime config as --headed (this can be used in both terminal & IDE)
    # here chromium is for chrome, and firefox for mozilla firefox
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")


def test_playwrightShortCut(page: Page):
    page.goto("https://rahulshettyacademy.com")


#-- #terms  .text-info  tagName
def test_coreLocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learnifdfd")
    page.get_by_role("combobox").select_option("teach")
    time.sleep(5)
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()


def test_firefoxBrowser(playwright: Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learnifdfd")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()



















