import pytest
import logging
from playwright.sync_api import sync_playwright
from config import BASE_URL

# Configure logging
logging.basicConfig(
    filename="test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()


@pytest.fixture
def page():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        context = browser.new_context()
        page = context.new_page()

        logger.info("Opening OrangeHRM login page")

        page.goto(BASE_URL)
        page.wait_for_selector("input[name='username']")

        yield page

        logger.info("Closing browser")

        context.close()
        browser.close()