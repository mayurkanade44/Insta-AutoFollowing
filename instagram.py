from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from time import sleep

username = 'YOUR_INSTAGRAM_USERNAME'
password = 'YOUR_INSTAGRAM_PASSWORD'
account =  'DESIRABLE_ACCOUNT_WHOS_FOLLOWERS_YOU_WANT_TO_FOLLOW' "example of url" = 'https://www.instagram.com/natgeoyourshot/'

chrome_driver = 'LOCAL_PATH_OF_CHROME_DRIVER'

class InstaFollower:

        def __init__(self, driver):
            self.driver = webdriver.Chrome(driver)

        def login(self):
            self.driver.get('https://www.instagram.com/')

            sleep(4)
            user = self.driver.find_element_by_name('username')
            user.send_keys(username)
            user.send_keys(Keys.TAB + password + Keys.ENTER)

            sleep(4)
            self.driver.find_element_by_css_selector('.cmbtv button').click()

            sleep(4)
            self.driver.find_element_by_xpath("//*[text() = 'Not Now']").click()

        def find_account(self):
            sleep(2)
            self.driver.get(account)

            sleep(4)
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()

            sleep(5)
            follow = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
            for i in range(4):
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follow)
                sleep(1)

        def follow(self):
            all_followers = self.driver.find_elements_by_css_selector('li button')
            for follow in all_followers:
                try:
                    follow.click()
                    sleep(2)
                except ElementClickInterceptedException:
                    cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                    cancel_button.click()



insta = InstaFollower(chrome_driver)
insta.login()
insta.find_account()
insta.follow()