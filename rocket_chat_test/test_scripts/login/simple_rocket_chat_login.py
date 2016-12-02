from pages.login.rc_login_page import RCLoginPage


def test_login_to_rc(session_driver):
    RCLoginPage(driver=session_driver).login()
