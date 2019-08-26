import unittest
from page import SearchPage


class TestCases(unittest.TestCase):

    def setUp(self):
        self.page = SearchPage()

    def tearDown(self):
        self.page.close()

    def test_check_search(self):
        self.page.open('http://mail.ru')
        self.page.set_search_phrase('Qwerty')
        assert self.page.get_nav_bar()


if __name__ == '__main__':
    unittest.main()
