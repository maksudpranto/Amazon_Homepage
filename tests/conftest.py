import pytest
import os
from datetime import datetime
from playwright.sync_api import sync_playwright
from pages.amazon import Amazon

@pytest.fixture(scope="function")
def amazon_home():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        amazon_home = Amazon(page)
        yield amazon_home
        browser.close()