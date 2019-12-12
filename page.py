from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class BasePage(object):

    def __init__(self):
        self.driver=webdriver.Chrome('./bin/chromedriver')

    def open(self, url):
        return self.driver.get(url)

    def close(self):
        self.driver.close()


class MainPage(BasePage):

    def sign_in(self, username, password):
        login = self.driver.find_element_by_xpath('//input[contains(@class, \'search__input\')]')
        password = self.driver.find_element_by_xpath('//input[contains(@class, \'search__input\')]')
        try:
            login.send_keys(username)
            password.send_keys(password)
        except:
            print("ERROR")



class SearchPage(BasePage):

    def set_search_phrase(self, search_phrase):
        field = self.driver.find_element_by_xpath('//input[contains(@class, \'search__input\')]')
        field.send_keys(search_phrase)
        field.send_keys(Keys.RETURN)

    def get_nav_bar(self):
        return self.driver.find_element_by_xpath('//a[contains(@class, \'PageNavigator\')]')

