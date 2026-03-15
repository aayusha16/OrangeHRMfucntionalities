# from pages.login import Login


# def test_valid_login(page):
#     login = Login(page)
    
#     login.login("Admin", "admin123")
#     assert "dashboard" in page.url #un and pw  as a parameter to test pass and fail


# def test_invalid_password(page):
#     login = Login(page)
#     logger.info("Testing invalid password")
#     login.login("Admin", "admin1234")
#     assert "dashboard" not in page.url


# def test_invalid_username(page):
#     login = Login(page)
#     logger.info("Testing invalid username")
#     login.login("Admin1", "admin123")
#     assert "dashboard" not in page.url


# def test_invalid_credentials(page):
#     login = Login(page)
#     login.login("ADMIN", "ADMIN123")
#     assert "dashboard" not in page.url


# def test_blank_login(page):
#     login = Login(page)
#     login.login("", "")
#     assert "dashboard" not in page.url


# def test_blank_password(page):
#     login = Login(page)
#     login.login("Admin", "")
#     assert "dashboard" not in page.url


# def test_blank_username(page):
#     login = Login(page)
#     login.login("", "admin123")
#     assert "dashboard" not in page.url
import pytest
from pages.login import Login

@pytest.mark.login
def test_valid_login(page):
    login = Login(page)

    login.login("Admin", "admin123")

    # Verify successful login
    assert "dashboard" in page.url