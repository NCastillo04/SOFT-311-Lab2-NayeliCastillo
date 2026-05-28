class LoginPage: 
    def __init__(self, driver): 
        self.driver = driver 
        self.email_input = self.driver.locator('input[data-testid="login-email-input"]') 
        self.password_input = self.driver.locator('input[data-testid="login-password-input"]')
        self.signup_button = self.driver.locator('button[data-testid="login-submit-button"]')
        self.signup_link = self.driver.locator('span[data-testid="login-signup-link"]')

    def fill_email(self, email):
        self.email_input.fill(email)

    def fill_password(self, name):
        self.password_input.fill(name) 
        
    def click_signup_button(self):
        self.signup_button.click()

    def click_signup_link(self):
        self.signup_link.click()