class Login:

    def __init__(self, page):
        self.page = page
        self.username_field = page.locator("input[name='username']")
        self.password_field = page.locator("input[name='password']")
        self.login_button = page.locator("button[type='submit']")
        self.error_message = page.locator(".oxd-alert-content-text")

    def login(self, username, password):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()

    def get_error_message(self):
        return self.error_message.text_content()