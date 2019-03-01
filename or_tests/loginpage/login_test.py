import unittest
import pytest
from or_plans.loginpage.login import Login

@pytest.mark.usefixtures("suiteSetup")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,suiteSetup):
        self.lp = Login(self.driver)

    def __del__(self):
        self.lp = None

    def test_loginPage(self):

        result = self.lp.verify_page_opened()
        assert result == True,"Failed to open page"