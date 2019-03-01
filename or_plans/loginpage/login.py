import os
import time
from base.common import CommonUI

class LoginLocators():
    """
    :Description:
       - This class provides all the locators which is related to Login page
    """

    VERIFY_PAGE = "Prepaid"

class Login(CommonUI):
    """
    :Description:
       - This class provides functionalities for Login related operations.
    """

    def __init__(self,driver):
        #Calling constructor of the parent class
        CommonUI.__init__(self,driver)
        self.driver = driver
        self.current_path = os.getcwd()
        # Absolute path for Login detail
        self.login_config = self.current_path + "/or_configfiles/loginDetails.txt"
        try:
            with open(self.login_config, 'r') as fp:
                self.url = fp.readlines()[0].strip().split('url:')

        except IOError as ex:
            raise IOError("IO Error raised : \n %s" % (ex))

    def open_page(self):
        """
        :Description:
            - The primary function of this method is to open page as per URL given in LoginDetails.txt file

        :Parameter:
            - None

        :Example:
            - None

        :Return: None
        """
        self.driver.get(self.url[1])
        time.sleep(3)
        self.driver.get(self.url[1])
        time.sleep(10)

    def verify_page_opened(self):
        """
        :Description:
            - The primary function of this method is to verify login on Login page

        :Parameter:
            - None

        :Example:
            - None

        :Return: Bool : True on Pass and False on Failures
        """

        status = self.is_element_present(LoginLocators.VERIFY_PAGE,locatorType="linktext")
        if status == True:
            self.information("Page Open Successfully")
        return status

    def close_page(self):
        """
        :Description:
            - The primary function of this method is to close current page

        :Parameter:
            - None

        :Example:
            - None

        :Return: None
        """
        self.driver.close()
