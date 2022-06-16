from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By


LOGIN_URL = 'https://www.facebook.com/login.php'


class FacebookLogin():
    def __init__(self, email, password, browser='Chrome'):
        self.email = email
        self.password = password
        if browser == 'Chrome':
            # Para chrome
            self.driver = webdriver.Chrome(
                executable_path=ChromeDriverManager().install())
        elif browser == 'Firefox':
            # Para Firefox
            self.driver = webdriver.Firefox(
                executable_path=GeckoDriverManager().install())
        self.driver.get(LOGIN_URL)
        time.sleep(1)  # Esperamos un segundo

    def login(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-notifications")
        email_element = self.driver.find_element(By.ID,'email')
        email_element.send_keys(self.email)  
        time.sleep(4)
        password_element = self.driver.find_element(By.ID,'pass')
        password_element.send_keys(self.password)  
        time.sleep(3)
        login_button = self.driver.find_element(By.ID,'loginbutton')
        login_button.click()  
        
        time.sleep(2)  
        self.driver.get('https://www.facebook.com/101620122201575/photos/a.134418305588423/171360495227537/')
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//div[normalize-space()="Partager"]/div').click()
        self.driver.find_element(By.XPATH, '').send_keys('uwu')


if __name__ == '__main__':
    fb_login = FacebookLogin(email='edalpha01@gmail.com',
                             password='ALFA6119', browser='Chrome')
    fb_login.login()
