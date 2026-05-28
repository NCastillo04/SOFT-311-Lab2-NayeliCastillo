import sys
from pathlib import Path

# Allow running this test file directly: `python tests/login_test.py`
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

import time

def test_products():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        email_ = f"naye1@example.com"
        password_ = "naye1234"

        page.goto("https://storedemo.testdino.com/login", wait_until="domcontentloaded")

        login_page = LoginPage(page)

        login_page.fill_email(email_)
        time.sleep(1)
        
        login_page.fill_password(password_)
        time.sleep(1)
        
        login_page.click_signup_button()
        
        page.goto("https://storedemo.testdino.com/products", wait_until="domcontentloaded")

        products_page = ProductsPage(page)
        
        products_page.agregar_a_favoritos(0)
        products_page.agregar_a_favoritos(3)

        time.sleep(3)



        assert products_page.validar_cantidad_favoritos(2), f"Cantidad espera 2 pero tuvo otra cantidad"

        # FALTA EL AGREGAR PRODUCTO AL CARRITO

        # Agregar producto a favoritos <<<<<<<<<<<<<

        time.sleep(3)
        
        browser.close()


# EJECUTAR ASI: 
# .venv\Scripts\python -m pytest tests/products_test.py