import pytest
from pages.login import Login
from pages.admin import AdminPage

@pytest.mark.admin
def test_search_existing_user(page):
 
    login = Login(page)
    login.login("Admin", "admin123")
    logger.info("Logged in successfully")
    admin = AdminPage(page)
    admin.open_admin_page()

    admin.search_user(username="Admin")

    assert admin.verify_user_found(), "Existing user not found"


@pytest.mark.admin
def test_search_user_with_employee_name(page):
    login = Login(page)
    login.login("Admin", "admin123")

    admin = AdminPage(page)
    admin.open_admin_page()

    # Search by Employee Name
    admin.search_user(employee_name="Aayusha Tester")
    assert admin.verify_user_found(), "User with Employee Name not found"


@pytest.mark.admin
def test_search_user_with_status_and_role(page):
    login = Login(page)
    login.login("Admin", "admin123")

    admin = AdminPage(page)
    admin.open_admin_page()

    # Search by User Role and Status
    admin.search_user(user_role="Admin", status="Enabled")
    assert admin.verify_user_found(), "No user found with selected Role and Status"


@pytest.mark.admin
def test_search_user_invalid(page):
    login = Login(page)
    login.login("Admin", "admin123")

    admin = AdminPage(page)
    admin.open_admin_page()

    # Search with invalid username
    admin.search_user(username="invalidUser123")
    # Expect no results
    assert not admin.verify_user_found(), "Invalid user unexpectedly found"