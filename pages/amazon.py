from playwright.sync_api import Page

class Amazon:
    def __init__(self, page: Page):
        self.page = page
        self.dropdown = 'select#searchDropdownBox'
        self.search_box = 'input#twotabsearchtextbox'
        self.search_button = 'input#nav-search-submit-button'

    def amazon_go(self):
        self.page.goto("https://www.amazon.com/")

    def software_selection(self):
        self.page.select_option(self.dropdown, label="Software")

    def search_text_insertion(self, text: str):
        self.page.select_option(self.dropdown, label="Software")
        self.page.fill(self.search_box, text)
        self.page.click(self.search_button)

    def close_browser(self):
        self.page.context.close()
