import unittest
import pytest
import time
from or_plans.loginpage.login import Login
from or_plans.touristpage.tourist import TouristPlans


@pytest.mark.usefixtures("suiteSetup")
class PrepaidTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,suiteSetup):
        self.tp = TouristPlans(self.driver)
        self.lp = Login(self.driver)

    def test_more_info_25(self):
        result_login = self.lp.verify_page_opened()
        assert result_login == True,"Failed"
        self.tp.click_Tourist_option()
        self.tp.click_more_info_button()
        verify_button = self.tp.verify_more_info_button()
        time.sleep(2)
        assert verify_button == True, "Clicking on more info button failed"

"""
Recharge Button is not automatable as of now beacuse which ever mobile number we are entering it is not working
"""