# class PIMPage:
#     def __init__(self, page):
#         self.page = page
#         self.pim_menu = page.locator("text=PIM")
#         self.add_employee_button = page.locator("button:has-text('Add')")
#         self.first_name_input = page.locator("input[name='firstName']")
#         self.last_name_input = page.locator("input[name='lastName']")
#         self.save_button = page.locator("button:has-text('Save')")

    
#     def open_pim_page(self):
#         self.pim_menu.click()

#     def click_add_employee(self):
#         self.add_employee_button.click()

#     def add_employee(self, first_name, last_name):
#         self.first_name_input.fill(first_name)
#         self.last_name_input.fill(last_name)
#         self.save_button.click()

#     def verify_employee_added(self):
        
#         return "addEmployee" in self.page.url
# pages/pim.py

class PIMPage:
    def __init__(self, page):
        self.page = page
        self.pim_menu = page.locator("text=PIM")
        self.add_employee_button = page.locator("button:has-text('Add')")

        # Employee fields
        self.first_name_input = page.locator("input[name='firstName']")
        self.middle_name_input = page.locator("input[name='middleName']")
        self.last_name_input = page.locator("input[name='lastName']")
        self.employee_id_input = page.locator("input[name='employeeId']")

        # Optional: Create Login Details checkbox
        self.create_login_checkbox = page.locator("input[type='checkbox']")

        # Buttons
        self.save_button = page.locator("button:has-text('Save')")
        self.cancel_button = page.locator("button:has-text('Cancel')")

    def open_pim_page(self):
        self.pim_menu.click()

    def click_add_employee(self):
        self.add_employee_button.click()

    def add_employee(self, first_name, middle_name, last_name, employee_id, create_login=False):
        self.first_name_input.fill(first_name)
        self.middle_name_input.fill(middle_name)
        self.last_name_input.fill(last_name)
        self.employee_id_input.fill(employee_id)

        if create_login:
            self.create_login_checkbox.check()

        self.save_button.click()

    def verify_employee_added(self):
        # You can also check for a success message if needed
        return "addEmployee" in self.page.url