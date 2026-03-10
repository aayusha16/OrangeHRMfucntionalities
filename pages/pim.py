class PIMPage:

    def __init__(self, page):
        self.page = page
        self.pim_menu = page.locator("text=PIM")
        self.add_employee_button = page.locator("button:has-text('Add')")
        self.first_name_input = page.locator("input[name='firstName']")
        self.last_name_input = page.locator("input[name='lastName']")
        self.save_button = page.locator("button:has-text('Save')")

    # Click PIM menu
    def open_pim_page(self):
        self.pim_menu.click()

    # Click Add Employee
    def click_add_employee(self):
        self.add_employee_button.click()

    # Fill employee details
    def add_employee(self, first_name, last_name):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.save_button.click()

    # Verify employee added
    def verify_employee_added(self):
        return "addEmployee" in self.page.url
