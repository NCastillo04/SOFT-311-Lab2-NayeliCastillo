import sys
from pathlib import Path

# Allow running this test file directly: `python tests/login_test.py`
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
import time


def run() -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        login = LoginPage(page)
        
        page.goto("https://www.automationexercise.com/login", wait_until="domcontentloaded")
        
        login.fill_signup_name("Felipe")
        time.sleep(5)
        
        login.fill_email("felipe123123@example.com")
        time.sleep(5)
        
        login.click_signup_button()
        time.sleep(5)
        
        ## validar url
        assert page.url == "https://www.automationexercise.com/signup", f"Expected URL to be 'https://www.automationexercise.com/signup' but got '{page.url}'"
        time.sleep(10)
        browser.close()


if __name__ == "__main__":
    run()