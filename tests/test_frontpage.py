import pytest
from pages.frontpage import FrontPage


@pytest.mark.landing
def test_username_field_visibility(page):
    landing_page = LandingPage(page)
    assert landing_page.verify_usernameField(), "Username field is not visible."


@pytest.mark.landing
def test_password_field_visibility(page):
    landing_page = LandingPage(page)
    assert landing_page.verify_passwordField(), "Password field is not visible."


@pytest.mark.landing
def test_login_button_visibility(page):
    landing_page = LandingPage(page)
    assert landing_page.verify_loginButton(), "Login button is not visible."


@pytest.mark.landing
def test_forgot_password_link_visibility(page):
    landing_page = LandingPage(page)
    assert landing_page.verify_forgotPasswordLink(), "Forgot Password link is not visible."