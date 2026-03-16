import pytest
import logging
from pages.login import Login
from data.login_data import get_login_data

logger = logging.getLogger(__name__)


@pytest.mark.parametrize("username,password,expected", get_login_data())
def test_login(page, username, password, expected):

    logger.info(f"Testing login with {username}")

    login = Login(page)
    login.login(username, password)

    if expected:
        assert "dashboard" in page.url
    else:
        assert "dashboard" not in page.url