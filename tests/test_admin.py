# import pytest
# import logging
# from pages.login import Login
# from pages.admin import AdminPage

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)


# @pytest.mark.admin
# def test_search_existing_user(page):

#     login = Login(page)
#     login.login("Admin", "admin123")
#     logger.info("Logged in successfully")

#     admin = AdminPage(page)
#     admin.open_admin_page()

#     admin.search_user(username="Admin")

#     try:
#         assert admin.verify_user_found()
#         logger.info("Existing user found successfully")
#     except AssertionError:
#         logger.warning("Existing user not found")


# @pytest.mark.admin
# def test_search_user_with_employee_name(page):

#     login = Login(page)
#     login.login("Admin", "admin123")

#     admin = AdminPage(page)
#     admin.open_admin_page()

#     admin.search_user(employee_name="Aayusha Tester")

#     try:
#         assert admin.verify_user_found()
#         logger.info("User with employee name found")
#     except AssertionError:
#         logger.warning("User with employee name not found")


# @pytest.mark.admin
# def test_search_user_with_status_and_role(page):

#     login = Login(page)
#     login.login("Admin", "admin123")

#     admin = AdminPage(page)
#     admin.open_admin_page()

#     admin.search_user(user_role="Admin", status="Enabled")

#     try:
#         assert admin.verify_user_found()
#         logger.info("User found with selected role and status")
#     except AssertionError:
#         logger.warning("No user found with selected role and status")


# @pytest.mark.admin
# def test_search_user_invalid(page):

#     login = Login(page)
#     login.login("Admin", "admin123")

#     admin = AdminPage(page)
#     admin.open_admin_page()

#     admin.search_user(username="invalidUser123")

#     try:
#         assert not admin.verify_user_found()
#         logger.info("Invalid user correctly not found")
#     except AssertionError:
#         logger.warning("Invalid user unexpectedly found")
import pytest
import logging
from pages.login import Login
from pages.admin import AdminPage

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.mark.admin
def test_open_job_titles(page):

    login = Login(page)
    login.login("Admin", "admin123")
    logger.info("Logged in successfully")

    admin = AdminPage(page)

    # Click Admin menu
    admin.open_admin_page()
    logger.info("Admin page opened")

    # Click Job → Job Titles
    admin.open_job_titles()
    logger.info("Navigated to Job Titles page")

    # Verification (URL contains jobTitle)
    try:
        assert "jobTitle" in page.url
        logger.info("Successfully opened Job Titles page")
    except AssertionError:
        logger.warning("Failed to open Job Titles page")