import pytest
from playwright.sync_api import Playwright


@pytest.fixture()
def preSetupWork():
    print("I am setting up browser instance")
    return "pass"

