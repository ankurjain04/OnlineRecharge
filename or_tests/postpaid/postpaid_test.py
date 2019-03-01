import unittest
import pytest
import time
from or_plans.loginpage.login import Login
from or_plans.postpaidpage.postpaid import PostpaidPlans


@pytest.mark.usefixtures("suiteSetup")
class PostpaidTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,suiteSetup):
        self.po = PostpaidPlans(self.driver)
        self.lp = Login(self.driver)

    def test_national_important_button_125(self):
        result_login = self.lp.verify_page_opened()
        assert result_login == True,"Failed"
        self.po.click_important_button()
        verify_button = self.po.verify_imp_button()
        time.sleep(2)
        assert verify_button == True, "Clicking on important button failed"


    def test_national_order_button_125(self):
        result_login = self.lp.verify_page_opened()
        assert result_login == True, "Failed"
        self.po.click_order_button()
        time.sleep(5)
        verify_button = self.po.verify_order_button()
        assert verify_button == True, "Clicking on order button failed"

    def test_flexible_important_button_125(self):
        result_login = self.lp.verify_page_opened()
        assert result_login == True, "Failed"
        self.po.click_flexible_option()
        time.sleep(2)
        self.po.click_flex_important_button()
        verify_button = self.po.verify_imp_button()
        time.sleep(2)
        assert verify_button == True, "Clicking on important button failed"

    def test_flexible_order_button_125(self):
        result_login = self.lp.verify_page_opened()
        assert result_login == True, "Failed"
        self.po.click_flexible_option()
        time.sleep(2)
        self.po.click_flex_order_button()
        time.sleep(5)
        verify_button = self.po.verify_order_button()
        assert verify_button == True, "Clicking on order button failed"