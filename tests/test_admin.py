import pytest
from pages.login import Login
from pages.admin import AdminPage


@pytest.mark.admin
def test_open_admin_page(Login):
    # Login first
    login = Login(page)
    login.login("Admin", "admin123")

    # Open Admin section
    admin = AdminPage(page)
    admin.open_admin_page()

    # Simple assertion: URL contains /admin
    assert "/admin" in page.url, "Admin page did not open successfully."