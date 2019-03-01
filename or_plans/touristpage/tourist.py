import time
import os
from base.common import CommonUI

class TouristLocators():
    """
    :Description:
       - This class provides all the locators which is related to Login page
    """

    Tourist_OPTION = "Tourist"
    MORE_INFO_25 = "/html/body/main/section[4]/div/div[2]/div/div[2]/div[1]/div/div[4]/div[4]/button[1]"
    VERIFY_MORE_INFO_BUTTON_25 = "//div[@id='tourist-plan-reveal-info']//div[contains(text(),'This is important to know')]"

class TouristPlans(CommonUI):
    """
    :Description:
       - This class provides functionalities for Create Survey related operations.
    """

    def __init__(self,driver):
        CommonUI.__init__(self, driver)
        self.driver = driver

    def click_Tourist_option(self):
        """
        :Description:
            - The primary function of this method is to perform click on tourist option.

        :Parameter:
            - None

        :Example:
            - None

        :Return: None
        """
        self.element_click(TouristLocators.Tourist_OPTION, locatorType="linktext")

    def click_more_info_button(self):
        """
        :Description:
            - The primary function of this method is to perform click on more info button.

        :Parameter:
            - None

        :Example:
            - None

        :Return: None
        """
        self.element_click(TouristLocators.MORE_INFO_25, locatorType="xpath")

    def verify_more_info_button(self):
        """
        :Description:
            - The primary function of this method is to verify more info button for Tourist plan.

        :Parameter:
            - None

        :Example:
            - None

        :Return: Bool : True on Pass and False on Failures
        """

        status = self.is_element_present(TouristLocators.VERIFY_MORE_INFO_BUTTON_25,locatorType="xpath")
        if status == True:
            self.information("Showing More Info Successfully")
        return status