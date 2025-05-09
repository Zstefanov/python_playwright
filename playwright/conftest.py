from email.policy import default

import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Browser to run tests with"
    )

#runs once before whole execution
@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param

@pytest.fixture
def browserInstance(playwright, request):
    browser_name = request.config.getoption("browser_name")
    if browser_name=="chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name=="firefox":
        browser = playwright.firefox.launch(headless=False)
    elif browser_name=="webkit":
        browser = playwright.webkit.launch(headless=False)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()