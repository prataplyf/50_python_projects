from selenium import webdriver
import os
import time

class InstagramBot():

    def __init__(self, username, password):
        self.username = username
        self.password = password

        # for interacting with web we need a webdriver that we will get from selenium
        self.driver = webdriver.Firefox('./geckodriver')


if __name__ == '__main__':
    ig_bot = InstagramBot('prataplyf', 'ilovemyindian')
    print(ig_bot.username)
    print(ig_bot.password)