import sys
from pathlib import Path

from tests.helpers.assertions import assert_with_screenshot

# Allow running this test file directly: `python tests/login_test.py`
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.home_page import HomePage
from pages.products_page import ProductsPage

import time

def test_login():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        email_last_int = int(time.time())

        email_ = f"naye{email_last_int}@example.com"
        password_ = "naye1234"

        # >>>>>>>>>>>>>> Validar carga del Home
        page.goto("https://storedemo.testdino.com", wait_until="domcontentloaded")

        assert page.url == "https://storedemo.testdino.com/", f"Expected URL to be 'https://storedemo.testdino.com' but got '{page.url}'"
        
        home_page = HomePage(page)

        home_page.click_login_button()
        time.sleep(3)

        assert page.url == "https://storedemo.testdino.com/login", f"Expected URL to be 'https://storedemo.testdino.com/login' but got '{page.url}'"

        login_page = LoginPage(page)

        login_page.click_signup_link()

        page.wait_for_url("**/signup", timeout=15000)

        assert_with_screenshot(
            page,
            condition=page.url == "https://storedemo.testdino.com/signup",
            message=(
                "Espected URL to be 'https://storedemo.testdino.com/signup'"
                f"bus got '{page.url}'"
            ),
            name="signup_url_assert"
        )


        assert page.url == "https://storedemo.testdino.com/signup", f"Expected URL to be 'https://storedemo.testdino.com/signup' but got '{page.url}'"

        # >>>>>>>>>>>>> Registro de usuario

        signup_page = SignupPage(page)

        signup_page.fill_first_name("Nayeli")
        signup_page.fill_last_name("Castillo")
        signup_page.fill_email_address(email_)
        signup_page.fill_password(password_)

        signup_page.click_signup_button()

        # time.sleep(10) 

        # AL crear el user con los credenciales se dirigue automaticamente, por eso se valida contra la url
        # assert page.url == "https://storedemo.testdino.com/login", f"Expected URL to be 'https://storedemo.testdino.com/login' but got '{page.url}'"
        
        # Registro de usuario <<<<<<<<<<<<

        time.sleep(5)

        # >>>>>>>>>>>>>> Login válido

        login_page.fill_email(email_)
        time.sleep(1)
        
        login_page.fill_password(password_)
        time.sleep(1)
        
        login_page.click_signup_button()
        
        page.wait_for_url("https://storedemo.testdino.com/")

        # Se valida que se haya logeado bien y haya ido al home
        assert page.url == "https://storedemo.testdino.com/", f"Expected URL to be 'https://storedemo.testdino.com' but got '{page.url}'"

        time.sleep(3)

        home_page.click_login_button()
   
        page.wait_for_url("https://storedemo.testdino.com/account")

        assert page.url == "https://storedemo.testdino.com/account", f"Expected URL to be 'https://storedemo.testdino.com/account' but got '{page.url}'"
        # Login válido <<<<<<<<<<<<

        time.sleep(3)


        page.goto("https://storedemo.testdino.com/products", wait_until="domcontentloaded")

        products_page = ProductsPage(page)
        
        products_page.agregar_a_favoritos(0)
        time.sleep(2)

        products_page.agregar_a_favoritos(3)

        time.sleep(3)

        cantidad_favoritos = products_page.get_cantidad_favoritos()

        assert cantidad_favoritos == "2", f"Cantidad espera 2 pero tuvo {cantidad_favoritos}"


        products_page.agregar_al_carrito(0)     
        time.sleep(2)

        products_page.agregar_al_carrito(3)      
        time.sleep(2)

        products_page.agregar_al_carrito(4)
        time.sleep(2)
    
        cantidad_carrito = products_page.get_cantidad_carrito()

        assert cantidad_carrito == "3", f"Cantidad espera 3 pero tuvo {cantidad_carrito}"


        # Agregar producto a favoritos <<<<<<<<<<<<<

        time.sleep(10)
        
        browser.close()


# if __name__ == "__main__":
#    run()



# .venv\Scripts\python -m pip install pytest-html

# .venv\Scripts\python -m pytest --html=report.html --self-contained-html

# cart.add_product(productos.nth(0))


# EJECUTAR ASI: .venv\Scripts\python -m pytest -v