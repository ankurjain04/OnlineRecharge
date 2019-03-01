import time
import os
from base.common import CommonUI

class PrepaidLocators():
    """
    :Description:
       - This class provides all the locators which is related to Login page
    """

    PREPAID_OPTION = "Prepaid"
    MORE_INFO_125 = "/html/body/main/section[4]/div/div[3]/div/div[3]/div[17]/div/div[4]/div[7]/button[1]"
    VERIFY_MORE_INFO_BUTTON_125 = "//div[@id='plan-reveal-info']//div[contains(text(),'This is important to know')]"
    VERIFY_SUBSCRIBE_125 = "//div[@id='reveal-prepaid-plan-VoiceData']//div[contains(text(),'Subscribe to a new')]"
    DATA_INFO_525 = "/html/body/main/section[4]/div/div[3]/div/div[3]/div[5]/div/div[4]/div[5]/button[1]"
    DATA_SUBSCRIBE_525 = "/html/body/main/section[4]/div/div[3]/div/div[3]/div[5]/div/div[4]/div[5]/button[2]"
    VERIFY_DATA_SUBSCRIBE_525 = "//div[@id='reveal-prepaid-plan']//div[contains(text(),'Subscribe to a new')]"

class PrepaidPlans(CommonUI):
    """
    :Description:
       - This class provides functionalities for Create Survey related operations.
    """

    def __init__(self,driver):
        CommonUI.__init__(self, driver)
        self.driver = driver

    def click_prepaid_option(self):
        """
        :Description:
            - The primary function of this method is to perform click on prepaid option.

        :Parameter:
            - None

        :Example:
            - None

        :Return: None
        """
        self.element_click(PrepaidLocators.PREPAID_OPTION, locatorType="linktext")

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
        self.element_click(PrepaidLocators.MORE_INFO_125, locatorType="xpath")

    def verify_more_info_button(self):
        """
        :Description:
            - The primary function of this method is to verify more info button for Prepaid National plan.

        :Parameter:
            - None

        :Example:
            - None

        :Return: Bool : True on Pass and False on Failures
        """

        status = self.is_element_present(PrepaidLocators.VERIFY_MORE_INFO_BUTTON_125,locatorType="xpath")
        if status == True:
            self.information("Showing More Info Successfully")
        return status

    def click_subscribe_btn(self):
        """
        :Description:
            - The primary function of this method is to perform click on subscribe button.

        :Parameter:
            - None

        :Example:
            - None

        :Return: None
        """
        self.element_click(PrepaidLocators.MORE_INFO_125, locatorType="xpath")

    def verify_subscribe_btn(self):
        """
        :Description:
            - The primary function of this method is to verify subscribe button for Prepaid National plan.

        :Parameter:
            - None

        :Example:
            - None

        :Return: Bool : True on Pass and False on Failures
        """

        status = self.is_element_present(PrepaidLocators.VERIFY_SUBSCRIBE_125,locatorType="xpath")
        if status == True:
            self.information("Showing Subscribe Successfully")
        return status

    def click_data_only_info_button_525(self):
        """
        :Description:
            - The primary function of this method is to perform click on more info button for data only option.

        :Parameter:
            - None

        :Example:
            - None

        :Return: None
        """
        self.element_click(PrepaidLocators.DATA_INFO_525, locatorType="xpath")

    def click_data_only_subscribe_button_525(self):
        """
        :Description:
            - The primary function of this method is to perform click on subscribe button for data only option.

        :Parameter:
            - None

        :Example:
            - None

        :Return: None
        """
        self.element_click(PrepaidLocators.DATA_SUBSCRIBE_525, locatorType="xpath")

    def verify_data_only_subscribe_btn_525(self):
        """
        :Description:
            - The primary function of this method is to verify subscribe button for data only option.

        :Parameter:
            - None

        :Example:
            - None

        :Return: Bool : True on Pass and False on Failures
        """

        status = self.is_element_present(PrepaidLocators.VERIFY_DATA_SUBSCRIBE_525,locatorType="xpath")
        if status == True:
            self.information("Showing Subscribe Successfully")
        return status