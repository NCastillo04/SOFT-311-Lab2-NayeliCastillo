class LoginPage: 
    def __init__(self, driver): 
        self.driver = driver 
        self.signup_name_input = self.driver.locator('input[data-qa="signup-name"]') 
        self.email_input = self.driver.locator('input[data-qa="signup-email"]') 
        self.signup_button = self.driver.locator('button[data-qa="signup-button"]')

    def fill_signup_name(self, name):
        self.signup_name_input.fill(name) 
        
    def fill_email(self, email):
        self.email_input.fill(email)

    def click_signup_button(self):
        self.signup_button.click()