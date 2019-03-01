import pytest
import os
from selenium import webdriver
from or_plans.loginpage.login import Login

@pytest.yield_fixture(scope="function")
def suiteSetup(request,browser):
    """
    :Description:
        - The primary function of this method is to one time setup before and after running any suite.

    :Parameter:
        - browser - accepts type of browser Chrome or Firefox

    :Example:
        - py.test -s -v or_tests/loginpage/login_test.py --browser chrome

    :Return: object : return driver instance
    """

    print "\n Running Test on ", browser.lower()
    if browser.lower() == "chrome":
        driver_path = '/home/ankur/Downloads/lib/chromedriver'
        os.environ['webdriver.chrome.driver'] = driver_path
        driver = webdriver.Chrome(driver_path)
        driver.maximize_window()
        driver.implicitly_wait(20)

    else:
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(20)
        pass

    if os.path.exists(os.getcwd() + "/test.log"):
        os.remove(os.getcwd() + "/test.log")

    if request.cls is not None:
        request.cls.driver = driver

    lp = Login(driver)
    lp.open_page()

    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", help="Type of browser Chrome or Firefox")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")