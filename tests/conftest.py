import pytest
from playwright.sync_api import sync_playwright
from pages.amazon import Amazon

@pytest.fixture(scope="function")
def amazon_home():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Launch browser
        context = browser.new_context()  # Create new browser context
        page = context.new_page()  # Create new page
        amazon_home = Amazon(page)  # Create AmazonPage object
        yield amazon_home  # Provide amazon_page object to the test function
        browser.close()  # Close the browser after test is finished
