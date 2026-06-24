import playwright
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,  # Set to True for headless mode
            slow_mo=1000  # Slow down actions for better visibility
        )
        page = browser.new_page()
        yield page
        browser.close()