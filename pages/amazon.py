from playwright.sync_api import Page

class Amazon:
    def __init__(self, page:Page):
        self.page = page
        self.dropdown = page.locator('select#searchDropdownBox')
        self.search_box = page.locator('input#twotabsearchtextbox')
        self.search_button = page.locator ('input#nav-search-submit-button')

    def amazon_go(self):
        self.page.goto("https://www.amazon.com/")

    def software_selection(self):
        self.dropdown.select_option(label="Software")

    def search_text_insertion(self, text: str):

        self.search_box.fill(text)
        self.search_button.click()

    def close_browser(self):
        self.page.context.close()
