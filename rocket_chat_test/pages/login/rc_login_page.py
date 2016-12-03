from webium import BasePage
from pages.homepage.rc_homepage import RCHomePage

class RCLoginPage(BasePage):
    def __init__(self, driver, url='http://ec2-52-54-114-100.compute-1.amazonaws.com'):
        super(RCLoginPage, self).__init__(driver=driver, url=url)
        self.driver = driver

    def login(self):
        self.open()
        self.driver.wait_for_element(css_selector='a.logo img')
        self.driver.wait_for_element(id_='emailOrUsername')
        self.driver.get_elm('login-card').fill_out_and_submit({
            'emailOrUsername': 'iyer.a.sri@gmail.com',
            'pass': 'Srifree_2020'
        })
        return RCHomePage(self.driver, 'sridhar.iyer')
