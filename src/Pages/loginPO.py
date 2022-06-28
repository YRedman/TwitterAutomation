# -------------------------------------  PAGE OBJECTS -------------------------------------- #
# Here you can find the Page Objects to be used in the Login section of the twitter page.
#

class LoginPO():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox = "session[username_or_email]"
        self.password_textbox = "session[password]"
        self.login_button_id = "//div[@data-testid='LoginForm_Login_Button']"

    # Types the username
    def enter_username(self, username):
        self.driver.find_element_by_name(self.username_textbox).send_keys(username)

    # Types the password
    def enter_password(self, password):
        self.driver.find_element_by_name(self.password_textbox).send_keys(password)

    # Click on the login button
    def login_button_click(self):
        self.driver.find_element_by_xpath(self.login_button_id).click()
