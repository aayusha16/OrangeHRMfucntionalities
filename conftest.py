import pytest
from playwright.sync_api import sync_playwright
# from pages.login import Login
@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        yield page
        browser.close()
@pytest.fixture
def test_valid_login(page):
    login = Login(page)
    login.Login("Admin", "admin123")
    