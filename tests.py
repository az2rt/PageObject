import unittest
from page import SearchPage

class TestCases(unittest.TestCase):

    def setUp(self):
        self.page = SearchPage()

    def test_check_search(self):
        self.page.open('http://google.com')
        self.page.set_search_phrase('Qwerty')
        assert self.page.get_nav_bar()
