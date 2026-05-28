class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.productos_ref = self.driver.locator('a.relative.block.group')
        self.productos_cart_button_ref = self.driver.locator('[data-testid="all-products-cart-button"]')
        self.productos_wishlist_button_ref = self.driver.locator('[data-testid="all-products-wishlist-button"]')
        self.wishlist_count_ref = self.driver.locator('[data-testid="header-wishlist-count"]')


    def agregar_al_carrito(self, index=0):
        producto = self.productos_ref.nth(index)
        producto.hover()

        self.productos_cart_button_ref.nth(index).click()

    def agregar_a_favoritos(self, index=0):
        producto = self.productos_ref.nth(index)
        producto.hover()

        self.productos_wishlist_button_ref.nth(index).click()

    def validar_cantidad_favoritos(self, cantidad_esperada):
        cantidad_actual = self.wishlist_count_ref.text_content()

        return cantidad_actual == str(cantidad_esperada)
        