# class AdminPage:
#     def __init__(self, page):
#         self.page = page
#         self.admin_menu = page.locator("text=Admin")
#         self.username_field = page.locator("input[placeholder='Username']")
#         self.user_role_dropdown = page.locator("div[role='listbox']")  
#         self.employee_name_field = page.locator("input[placeholder='Type for hints...']")
#         self.status_dropdown = page.locator("div[role='listbox']")  
#         self.search_button = page.locator("button:has-text('Search')")
#         self.reset_button = page.locator("button:has-text('Reset')")
#         self.result_rows = page.locator(".oxd-table-row") 

#     def open_admin_page(self):
#         self.admin_menu.click()

   
#     def search_user(self, username="", user_role="", employee_name="", status=""):
#         if username:
#             self.username_field.fill(username)
#         if employee_name:
#             self.employee_name_field.fill(employee_name)
        
#         if user_role:
#             self.user_role_dropdown.click()
#             self.page.locator(f"text={user_role}").click()
#         if status:
#             self.status_dropdown.click()
#             self.page.locator(f"text={status}").click()
#         self.search_button.click()

#     # Verify at least one result is shown
#     def verify_user_found(self):
#         return self.result_rows.first.is_visible()
# pages/admin.py

class AdminPage:
    def __init__(self, page):
        self.page = page

        # Main menu
        self.admin_menu = page.locator("text=Admin")

        # Job menu
        self.job_menu = page.locator("text=Job")
        self.job_titles = page.locator("text=Job Titles")

    # Navigate to Admin page
    def open_admin_page(self):
        self.admin_menu.click()
        self.page.wait_for_timeout(500)  # wait for page to load

    # Navigate to Job → Job Titles
    def open_job_titles(self):
        self.job_menu.click()
        self.page.wait_for_timeout(300)  # wait for dropdown animation
        self.job_titles.click()
        self.page.wait_for_timeout(500)  # wait for Job Titles page to load