class HomePage: 
    def __init__(self, driver): 
        self.driver = driver 
        self.login_button = self.driver.locator('svg[data-testid="header-user-icon"]')

    def click_login_button(self):
        self.login_button.click()
        
  