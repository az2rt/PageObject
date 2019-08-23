from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class BasePage(object):

    def __init__(self):
        self.driver=webdriver.chrome('./bin/chromedriver')

    def open(self, url):
        return self.driver.get(url)


class SearchPage(BasePage):

    def set_search_phrase(self, search_phrase):
        field = self.driver.find_element_by_class_name('vdLsw gsfi')
        field.input(search_phrase)
        field.send_keys(Keys.RETURN)

    def get_nav_bar(self):
        return self.driver.find_element_by_class_name('navcnt')

