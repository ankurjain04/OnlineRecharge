import unittest
import pytest
import time
from or_plans.loginpage.login import Login
from or_plans.prepaidpage.prepaid import PrepaidPlans


@pytest.mark.usefixtures("suiteSetup")
class PrepaidTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,suiteSetup):
        self.pp = PrepaidPlans(self.driver)
        self.lp = Login(self.driver)

    def test_voice_data_info_150(self):
        result_login = self.lp.verify_page_opened()
        assert result_login == True,"Failed"

        self.pp.click_prepaid_option()
        self.pp.click_more_info_button()
        verify_button = self.pp.verify_more_info_button()
        time.sleep(2)
        assert verify_button == True, "Clicking on more info button failed"

    def test_voive_data_subscribe_150(self):
        result_login = self.lp.verify_page_opened()
        assert result_login == True, "Failed"
        self.pp.click_prepaid_option()
        self.pp.click_subscribe_btn()
        verify_button = self.pp.verify_subscribe_btn()
        time.sleep(2)
        assert verify_button == True, "Clicking on subscribe button failed"


    def test_data_only_info_525(self):
        result_login = self.lp.verify_page_opened()
        assert result_login == True,"Failed"

        self.pp.click_prepaid_option()
        self.pp.click_data_only_info_button_525()
        verify_button = self.pp.verify_more_info_button()
        time.sleep(2)
        assert verify_button == True, "Clicking on more info button failed"

    def test_data_only_subscribe_525(self):
        result_login = self.lp.verify_page_opened()
        assert result_login == True, "Failed"
        self.pp.click_prepaid_option()
        self.pp.click_data_only_subscribe_button_525()
        verify_button = self.pp.verify_data_only_subscribe_btn_525()
        time.sleep(2)
        assert verify_button == True, "Clicking on subscribe button failed"
