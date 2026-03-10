import pytest
from pages.login import Login
from pages.pim import PIMPage

@pytest.mark.pim
def test_add_employee(Login):
    
    login = Login(page)
    login.login("Admin", "admin123")

    # Go to PIM
    pim = PIMPage(Login)
    pim.open_pim_page()

    # Add new employee
    pim.click_add_employee()
    pim.add_employee("Aayusha", "Tester")

    # Assertion
    assert pim.verify_employee_added(), "Employee was not added successfully"