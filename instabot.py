from selenium import webdriver
import os
import time

"""
    To perform this action you need to install selenium and web driver of your browser:
    1: pip install selenium
    2: Web driver  (Chrome / Firefox / Safari, etc...)
"""


class InstagramBot():
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'
        self.driver = webdriver.Chrome('./chromedriver.exe')
        # call login function
        self.login()
        
    def login(self):
        self.driver.get('{}/accounts/login/'.format(self.base_url))
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[3]/button/div').click()
        # self.driver.find_element_by_xpath("//div[contains(text(), 'Log In')]")[0].click()
        time.sleep(5)
        # disable notification
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        time.sleep(2)
        # disable notification
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        time.sleep(1)
        
    
    def nav_user(self, user):
        self.driver.get('{}/{}/'.format(self.base_url, user))
    
    def follow(self, user):
        self.nav_user(user)
        time.sleep(5)
        # follow user
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button').click()
        # open user latest post
        # self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[2]/div/div[1]/div[2]/div/div/div/ul/li[2]/div/div/div/div[2]').click()
        # # like user latest post
        # self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span/svg').click()
        # # make a comment
        # self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys('Halloween')
        # # click on post btn
        # self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
        self.unfollow()
    
    def unfollow(self):
        time.sleep(5)
        unfollow_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button/div/span').click()
        unfoll_btn = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]').click()
        self.driver.quit()


if __name__ == '__main__':
    ig_bot = InstagramBot('username', 'password')
    # print(ig_bot.username, ig_bot.password)
    ig_bot.follow('coders.eduyear')