# from config import TIMEOUT

# class FrontPage:

#     def __init__(self, page):
#         self.page = page
#         self.username_field = page.locator("input[name='username']")
#         self.password_field = page.locator("input[name='password']")
#         self.login_button = page.locator("button[type='submit']")
#         self.forgot_password_link = page.locator("text=Forgot your password?")

#     def verify_usernameField(self):
#         self.username_field.wait_for(timeout=TIMEOUT)
#         return self.username_field.is_visible()

#     def verify_passwordField(self):
#         self.password_field.wait_for(timeout=TIMEOUT)
#         return self.password_field.is_visible()

#     def verify_loginButton(self):
#         self.login_button.wait_for(timeout=TIMEOUT)
#         return self.login_button.is_visible()

#     def verify_forgotPasswordLink(self):
#         self.forgot_password_link.wait_for(timeout=TIMEOUT)
#         return self.forgot_password_link.is_visible()
from utils.config import TIMEOUT  # Make sure TIMEOUT is defined in config.py, e.g., TIMEOUT = 5000

class FrontPage:

    def __init__(self, page):
        self.page = page
        self.username_field = page.locator("input[name='username']")
        self.password_field = page.locator("input[name='password']")
        self.login_button = page.locator("button[type='submit']")
        self.forgot_password_link = page.locator("text=Forgot your password?")

    def verify_usernameField(self):
        self.username_field.wait_for(timeout=TIMEOUT)
        return self.username_field.is_visible()

    def verify_passwordField(self):
        self.password_field.wait_for(timeout=TIMEOUT)
        return self.password_field.is_visible()

    def verify_loginButton(self):
        self.login_button.wait_for(timeout=TIMEOUT)
        return self.login_button.is_visible()

    def verify_forgotPasswordLink(self):
        self.forgot_password_link.wait_for(timeout=TIMEOUT)
        return self.forgot_password_link.is_visible()