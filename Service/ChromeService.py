from selenium import webdriver
from selenium.webdriver.common.by import By
class ChromeService:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.accept_insecure_certs = True  # open website even if it is unsafe
        self.driver = webdriver.Chrome(options=chrome_options)

    def move_to_url(self, new_url):
        self.driver.get(new_url)
        self.driver.refresh()
