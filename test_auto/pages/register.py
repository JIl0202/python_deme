from selenium.webdriver.common.by import By


class register_pages:
    url = 'http://localhost/dbshop/'

    def __init__(self, driver):
        self.driver = driver

    def register(self, username, password, reg_email):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, '注册').click()
        self.driver.find_element(By.ID, "user_name").send_keys(username)
        self.driver.find_element(By.ID, "user_password").send_keys(password)
        self.driver.find_element(By.ID, "user_com_passwd").send_keys(password)
        self.driver.find_element(By.ID, 'user_email').send_keys(reg_email)
        self.driver.find_element(By.ID, 'agreement').click()
        self.driver.find_element(By.XPATH, '//button').click()
        return self

    def load_pages(self):
        self.driver.get(self.url)
        return self

    def register_assert(self, username):
        e1 = True
        try:
            self.driver.find_element(By.PARTIAL_LINK_TEXT, username).text
        except:
            e1 = False
        return e1
