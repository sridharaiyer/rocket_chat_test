from webium import BasePage
from hamcrest import *


class RCHomePage(BasePage):
    def __init__(self, driver, username):
        super(RCHomePage, self).__init__(driver=driver)
        self.driver = driver
        driver.wait_for_element(css_selector='.data>h4')
        assert_that(driver.get_elm(css_selector='.data>h4').text, contains_string(username))
