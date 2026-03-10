from utils.config import TIMEOUT

class FrontPage:

    def __init__(self, page):
        self.page = page
        self.username_field = page.locator("input[name='username']")
        self.password_field = page.locator("input[name='password']")
        self.login_button = page.locator("button[type='submit']")
        self.forgot_password_link = page.locator("text=Forgot your password?")

    def verify_usernameField(self):
        return self.username_field.is_visible(timeout=TIMEOUT)

    def verify_passwordField(self):
        return self.password_field.is_visible(timeout=TIMEOUT)

    def verify_loginButton(self):
        return self.login_button.is_visible(timeout=TIMEOUT)

    def verify_forgotPasswordLink(self):
        return self.forgot_password_link.is_visible(timeout=TIMEOUT)