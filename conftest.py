import pytest
import logging
import os
from playwright.sync_api import sync_playwright
from config import BASE_URL

# Configure logging
logging.basicConfig(
    filename="test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger()

# Create screenshots folder if not exists
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

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


# Hook for screenshot on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # get the page fixture from the test
        page = item.funcargs.get("page")
        if page:
            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)
            logger.info(f"Screenshot taken: {screenshot_path}")