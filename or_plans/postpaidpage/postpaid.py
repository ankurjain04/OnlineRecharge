import time
import os
from base.common import CommonUI

class PostpaidLocators():
    """
    :Description:
       - This class provides all the locators which is related to Login page
    """

    IMPORTANT_BUTTON_125 = "/html/body/main/section[4]/div/div[3]/div/div[4]/div[17]/div/div[4]/div[8]/button[1]"
    IMP_FLEX_BTN_125 = "/html/body/main/section[4]/div/div[3]/div/div[4]/div[18]/div/div[4]/div[7]/button[1]"
    VERIFY_IMP_BUTTON_125 = "//div[@id='important-to-know']//div[@class='plans-landing--popup-title']"
    ORDER_BUTTON_125 = "/html/body/main/section[4]/div/div[3]/div/div[4]/div[17]/div/div[4]/div[7]/button[2]"
    ORD_FLEX_BTN_125 = "/html/body/main/section[4]/div/div[3]/div/div[4]/div[18]/div/div[4]/div[8]/button[2]"
    VERIFY_ORDER_BUTTON_125="/html/body/main/div/div/div/div/div[2]/span[2]/button"
    FLEXIBLE_OPTION = "//label[@for='national']"
    SELECT_LANGUAGE = "//a[@id='desktop-language-change_{}']"

class PostpaidPlans(CommonUI):
    """
    :Description:
       - This class provides functionalities for Create Survey related operations.
    """

    def __init__(self,driver):
        CommonUI.__init__(self, driver)
        self.driver = driver

    def click_important_button(self):
        """
        :Description:
            - The primary function of this method is to perform click on important button.

        :Parameter:
            - None

        :Example:
            - None

        :Return: None
        """
        self.element_click(PostpaidLocators.IMPORTANT_BUTTON_125, locatorType="xpath")

    def verify_imp_button(self):
        """
        :Description:
            - The primary function of this method is to verify important button for postpaid National plan.

        :Parameter:
            - None

        :Example:
            - None

        :Return: Bool : True on Pass and False on Failures
        """

        status = self.is_element_present(PostpaidLocators.VERIFY_IMP_BUTTON_125,locatorType="xpath")
        if status == True:
            self.information("Showing Important Info Successfully")
        return status

    def click_order_button(self):
        """
        :Description:
            - The primary function of this method is to perform click on Order button.

        :Parameter:
            - None

        :Example:
            - None

        :Return: None
        """
        self.element_click(PostpaidLocators.ORDER_BUTTON_125, locatorType="xpath")

    def verify_order_button(self):
        """
        :Description:
            - The primary function of this method is to verify order button for postpaid National plan.

        :Parameter:
            - None

        :Example:
            - None

        :Return: Bool : True on Pass and False on Failures
        """

        status = self.is_element_present(PostpaidLocators.VERIFY_ORDER_BUTTON_125, locatorType="xpath")
        if status == True:
            self.information("Showing Order Placed Successfully")
        return status

    def click_flexible_option(self):
        """
        :Description:
            - The primary function of this method is to perform click on flexible option.

        :Parameter:
            - None

        :Example:
            - None

        :Return: None
        """
        self.element_click(PostpaidLocators.FLEXIBLE_OPTION, locatorType="xpath")

    def click_flex_important_button(self):
        """
        :Description:
            - The primary function of this method is to perform click on important button for flexible option.

        :Parameter:
            - None

        :Example:
            - None

        :Return: None
        """
        self.element_click(PostpaidLocators.IMP_FLEX_BTN_125, locatorType="xpath")

    def click_flex_order_button(self):
        """
        :Description:
            - The primary function of this method is to perform click on order button for flexible option.

        :Parameter:
            - None

        :Example:
            - None

        :Return: None
        """
        self.element_click(PostpaidLocators.ORD_FLEX_BTN_125, locatorType="xpath")

    def select_language(self,language):

        if language.lower() == 'english':
            lang = PostpaidLocators.SELECT_LANGUAGE.format('en')
        elif language.lower() == 'arabic':
            lang = PostpaidLocators.SELECT_LANGUAGE.format('ar')
        else:
            print "Select language either english or arabic"
            return False
        print "****************"
        # element = self.driver.find_element_by_xpath(lang)
        self.driver.execute_script("scrollBy(0,-500);")
        return self.element_click(lang,locatorType="xpath")
