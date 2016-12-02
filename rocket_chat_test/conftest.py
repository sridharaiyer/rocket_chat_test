import pytest
from webdriverwrapper import Chrome


# Create browser once for all tests.
@pytest.yield_fixture(scope='session')
def session_driver():
    driver = Chrome()
    yield driver
    driver.quit()


# Before every test go to homepage.
@pytest.fixture(scope='function')
def _driver(session_driver):
    """
    :type session_driver: driver object
    """
    return session_driver
