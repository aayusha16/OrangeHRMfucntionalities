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