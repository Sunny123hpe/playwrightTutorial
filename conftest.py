import pytest
from playwright.sync_api import Playwright

@pytest.fixture(scope="function")
def set_up(page):
    # page.locator("body").click()
    page.goto("https://omayo.blogspot.com/")
    page.set_default_timeout(15000)

    yield page