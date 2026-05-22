class HomePage: 
    def __init__(self, driver): 
        self.driver = driver 
        self.logged_a = self.driver.locator('a[href="/logout"]')

    def is_visible_logout(self):
        self.logged_a.is_visible()
        
  