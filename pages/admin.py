class AdminPage:
    def __init__(self, page):
        self.page = page
        self.admin_menu = page.locator("text=Admin")
        self.username_field = page.locator("input[placeholder='Username']")
        self.user_role_dropdown = page.locator("div[role='listbox']")  # typical OHRM dropdown
        self.employee_name_field = page.locator("input[placeholder='Type for hints...']")
        self.status_dropdown = page.locator("div[role='listbox']")  # Enabled/Disabled
        self.search_button = page.locator("button:has-text('Search')")
        self.reset_button = page.locator("button:has-text('Reset')")
        self.result_rows = page.locator(".oxd-table-row")  # table rows

    # Navigate to Admin section
    def open_admin_page(self):
        self.admin_menu.click()

    # Enter search criteria
    def search_user(self, username="", user_role="", employee_name="", status=""):
        if username:
            self.username_field.fill(username)
        if employee_name:
            self.employee_name_field.fill(employee_name)
        # For dropdowns, you can click and select
        if user_role:
            self.user_role_dropdown.click()
            self.page.locator(f"text={user_role}").click()
        if status:
            self.status_dropdown.click()
            self.page.locator(f"text={status}").click()
        self.search_button.click()

    # Verify at least one result is shown
    def verify_user_found(self):
        return self.result_rows.first.is_visible()