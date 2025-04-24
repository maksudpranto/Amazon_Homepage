from playwright.sync_api import Page,expect
from pages.amazon import Amazon
import pytest


def test_01(amazon_home):
    amazon_home.amazon_go()
    amazon_home.software_selection()
    amazon_home.page.wait_for_timeout(2000)

def test_02(amazon_home):
    amazon_home.amazon_go()
    amazon_home.search_text_insertion("Games")
    amazon_home.page.wait_for_timeout(2000)

def test_03(amazon_home):
    amazon_home.close_browser()

