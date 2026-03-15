import pytest
import logging
from pages.login import Login
from pages.pim import PIMPage

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.mark.pim
def test_add_employee(page):

    login = Login(page)
    login.login("Admin", "admin123")
    logger.info("Logged in successfully")

    pim = PIMPage(page)

    pim.open_pim_page()
    pim.click_add_employee()

    pim.add_employee("Ram", "Kumar", "Singh", "2345")

    assert pim.verify_employee_added(), "Employee was not added successfully"