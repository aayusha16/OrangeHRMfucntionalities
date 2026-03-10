# # import pytest
# # from playwright.sync_api import sync_playwright
# # from config import BASE_URL
# # @pytest.fixture

# # def page():
# #     with sync_playwright() as p:
# #         browser = p.chromium.launch(headless=False)
# #         page = browser.new_page()
# #         page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# #         yield page
# #         browser.close()
        
# # @pytest.fixture
# # def Login(page):
# #     login = Login(page)
# #     login.Login("Admin", "admin123")
# #     return Login
# # # import pytest
# # # from playwright.sync_api import sync_playwright
# # # from config import BASE_URL

# # # @pytest.fixture
# # # def page():
# # #     with sync_playwright() as p:
# # #         browser = p.chromium.launch(headless=False)
# # #         page = browser.new_page()
# # #         page.goto(BASE_URL)
# # #         yield page
# # #         browser.close()
# import pytest
# from playwright.sync_api import sync_playwright
# from config import BASE_URL

# @pytest.fixture
# def page():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()
#         page.goto(BASE_URL)

#         # wait until username field appears
#         page.wait_for_selector("input[name='username']")

#         yield page
#         browser.close()
import pytest
from playwright.sync_api import sync_playwright
from config import BASE_URL


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        context = browser.new_context()
        page = context.new_page()

        page.goto(BASE_URL)
        page.wait_for_selector("input[name='username']")

        yield page

        context.close()
        browser.close()