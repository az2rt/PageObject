from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class BasePage(object):

    def __init__(self):
        self.driver=webdriver.Chrome('./bin/chromedriver')

    def open(self, url):
        return self.driver.get(url)

    def close(self):
        self.driver.close()

class SearchPage(BasePage):

    def set_search_phrase(self, search_phrase):
        try:
            field = self.driver.find_element_by_xpath('//input[contains(@class, \'search__input\')]')
            field.send_keys(search_phrase)
            field.send_keys(Keys.RETURN)
        except ( NoSuchElementException, AttributeError):
            import ipdb; ipdb.set_trace()

    def get_nav_bar(self):
        return self.driver.find_element_by_xpath('//a[contains(@class, \'PageNavigator\')]')

