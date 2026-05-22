class SignupPage: 
    def __init__(self, driver): 
        self.driver = driver 
        self.genero1 = self.driver.locator('#id_gender1')

        self.name_input = self.driver.locator('input[data-qa="name"]')
        self.email_input = self.driver.locator('input[data-qa="email"]')
        self.password_input = self.driver.locator('input[data-qa="password"]')

        self.date_select = self.driver.locator('select[data-qa="days"]')
        self.month_select = self.driver.locator('select[data-qa="months"]')
        self.year_select = self.driver.locator('select[data-qa="years"]')

        self.newsletter_checkbox = self.driver.locator('#newsletter')

        self.first_name_input = self.driver.locator('input[data-qa="first_name"]')
        self.last_name_input = self.driver.locator('input[data-qa="last_name"]')
        self.company_input = self.driver.locator('input[data-qa="company"]')
        self.address_input = self.driver.locator('input[data-qa="address"]')
        self.address2_input = self.driver.locator('input[data-qa="address2"]')
        self.country_select = self.driver.locator('select[data-qa="country"]')
        self.state_input = self.driver.locator('input[data-qa="state"]')
        self.city_input = self.driver.locator('input[data-qa="city"]')
        self.zipcode_input = self.driver.locator('input[data-qa="zipcode"]')
        self.mobile_number_input = self.driver.locator('input[data-qa="mobile_number"]')

        self.create_account_button = self.driver.locator('button[data-qa="create-account"]')


    def check_genero1(self):
        self.genero1.check()

    def fill_name(self, text):
        self.name_input.fill(text)

    def fill_email(self, text):
        self.email_input.fill(text)

    def fill_password(self, text):
        self.password_input.fill(text)

    def select_date(self, value:str):
        self.date_select.select_option(value)
        
    def select_month(self, value:str):
        self.month_select.select_option(value)    
        
    def select_year(self, value:str):
        self.year_select.select_option(value)
    
    def get_full_date_of_birth(self):
        day =  self.date_select.input_value()
        month =  self.month_select.input_value()
        year =  self.year_select.input_value()

        full_date = f"{day}/{month}/{year}"
        return full_date

    def toggle_newsletter(self, value:bool):
        self.newsletter_checkbox.set_checked(value)


    def fill_first_name(self, text):
        self.first_name_input.fill(text)
  
    def fill_last_name(self, text):
        self.last_name_input.fill(text)

    def fill_company(self, text):
        self.company_input.fill(text)
  
    def fill_address(self, text):
        self.address_input.fill(text)

    def fill_address2(self, text):
        self.address2_input.fill(text)
  
    def select_country(self, value):
        self.country_select.select_option(value) 

    def fill_state(self, text):
        self.state_input.fill(text)
  
    def fill_city(self, text):
        self.city_input.fill(text)

    def fill_zipcode(self, text):
        self.zipcode_input.fill(text)
  
    def fill_mobile_number(self, text):
        self.mobile_number_input.fill(text)

    def click_create_account_button(self):
        self.create_account_button.click()