# tests/test_pim.py

import pytest
import logging
from pages.login import Login
from pages.pim import PIMPage

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.mark.pim
def test_add_employee(page):
    # Login first
    login = Login(page)
    login.login("Admin", "admin123")
    logger.info("Logged in successfully")

    # Go to PIM module
    pim = PIMPage(page)
    pim.open_pim_page()
    pim.click_add_employee()

    # Add a new employee
    pim.add_employee(
        first_name="Ram",
        middle_name="Kumar",
        last_name="Singh",
        employee_id="2345",
        create_login=False  # change to True if you want to create login details
    )

    # Verify employee added
    assert pim.verify_employee_added(), "Employee was not added successfully"