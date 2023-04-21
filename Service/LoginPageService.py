from selenium.webdriver.common.by import By

class LoginPageService:
    def __init__(self,chrome_service):
        self.chrome_service=chrome_service
    """Login the default user:
    """
    def login_user(self):
        self.chrome_service.move_to_url("https://irony.cs.bgu.ac.il/#/login")
        # sets username field
        username = self.chrome_service.driver.find_element(By.XPATH, "/html/body/div/div/div/form/div[1]/div/input")
        username.send_keys("chana")
        # sets password field
        password = self.chrome_service.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/form/div[2]/div/input")
        password.send_keys("banana")
        # clicks on submit button
        login_button = self.chrome_service.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/form/button")
        login_button.click()
