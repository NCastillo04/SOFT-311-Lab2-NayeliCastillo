class SignupPage: 
    def __init__(self, driver): 
        self.driver = driver 

        self.first_name_input = self.driver.locator('input[data-testid="signup-firstname-input"]')
        self.last_name_input = self.driver.locator('input[data-testid="signup-lastname-input"]')
        self.email_address_input = self.driver.locator('input[data-testid="signup-email-input"]')
        self.password_input = self.driver.locator('input[data-testid="signup-password-input"]')

        self.signup_button = self.driver.locator('button[data-testid="signup-submit-button"]')

    def fill_first_name(self, text):
        self.first_name_input.fill(text)
        
    def fill_last_name(self, text):
        self.last_name_input.fill(text)

    def fill_email_address(self, text):
        self.email_address_input.fill(text)

    def fill_password(self, text):
        self.password_input.fill(text)

    def click_signup_button(self):
        self.signup_button.click()