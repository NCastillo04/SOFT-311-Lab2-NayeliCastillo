import sys
from pathlib import Path

# Allow running this test file directly: `python tests/login_test.py`
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.home_page import HomePage

import time

ts = 1

def run() -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        login = LoginPage(page)

        # ------------------------------- en clase -------------------------------
        
        page.goto("https://www.automationexercise.com/login", wait_until="domcontentloaded")
        
        login.fill_signup_name("Naye")
        time.sleep(ts)
        
        email_last_int = int(time.time())

        login.fill_email(f"naye{email_last_int}@example.com")
        time.sleep(ts)
        
        login.click_signup_button()
        time.sleep(ts)
        
        ## validar url signup
        assert page.url == "https://www.automationexercise.com/signup", f"Expected URL to be 'https://www.automationexercise.com/signup' but got '{page.url}'"
        
        
        # ------------------------------- Laboratorio 2 -------------------------------

        signup_page = SignupPage(page)

        signup_page.check_genero1()

        signup_page.fill_name("Naye")
        # signup_page.fill_email(f"naye{email_last_int}@example.com")
        signup_page.fill_password("hola")

        signup_page.select_date("4")
        signup_page.select_month("6")
        signup_page.select_year("2002")

        # valida la fecha completa selccionada
        assert signup_page.get_full_date_of_birth() == "4/6/2002"

        signup_page.toggle_newsletter(True)

        signup_page.fill_first_name("Nayeli")
        signup_page.fill_last_name("Castillo")
        signup_page.fill_company("Hola S.A.")
        signup_page.fill_address("Cartago")
        signup_page.fill_address2("Paraiso")
        signup_page.select_country("Canada")
        signup_page.fill_state("San Jose")
        signup_page.fill_city("San Jose")
        signup_page.fill_zipcode("3032")
        signup_page.fill_mobile_number("64779630")
        signup_page.click_create_account_button()

        time.sleep(5)

        # Registro de usuario - listo
        assert page.url == "https://www.automationexercise.com/account_created", f"Expected URL to be 'https://www.automationexercise.com/account_created' but got '{page.url}'"


        page.goto("https://www.automationexercise.com", wait_until="domcontentloaded")

        time.sleep(5)

        # Validar carga del Home - listo
        assert page.url == "https://www.automationexercise.com/", f"Expected URL to be 'https://www.automationexercise.com/' but got '{page.url}'"

        home_page = HomePage(page)

        # Validacion de login existo despues del registro
        assert home_page.is_visible_logout()

        time.sleep(6)
        browser.close()


if __name__ == "__main__":
    run()