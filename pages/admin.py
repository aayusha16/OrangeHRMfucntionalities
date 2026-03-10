class AdminPage:

    def __init__(self, page):
        self.page = page
        self.admin_menu = page.locator("text=Admin")

    def open_admin_page(self):
        self.admin_menu.click()