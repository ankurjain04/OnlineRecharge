import sm_utilities.custom_logger as cl
import logging
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class CommonUI():
    """
    :Description:
       - This class provides common functionalities for all selenium driver related operations.
    """

    def __init__(self, driver):
        self.driver = driver
        self.log = cl.customLogger(logging.DEBUG)

    def get_by_type(self, locatorType):
        """
        :Description:
            - The primary function of this method is to return locator type as per its type

        :Parameter:
            - locatorType - Accepts type of locator

        :Example:
            - ``get_by_type("id")``
            - ``get_by_type("xpath")``

        :Return: String : return type of locator.
        """
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType + " not correct/supported")
        return False

    def get_element(self, locator, locatorType="id"):
        """
        :Description:
            - The primary function of this method is to get and return locator of element on the page.

        :Parameter:
            - locatorType - Accepts type of locator and by default it accepts id as an locator

        :Example:
            - ``get_element("username","id")``
            - ``get_element("//*[@id=username]","xpath")``

        :Return: String : return locator of element.
        """
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.get_by_type(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator + " and locatorType: " + locatorType)
        return element

    def get_elements(self, locator, locatorType="id"):
        """
        :Description:
            - The primary function of this method is to get and return locator of elements on page.

        :Parameter:
            - locatorType - Accepts type of locator and by default it accepts id as an locator

        :Example:
            - ``get_elements("username","id")``
            - ``get_elements("//*[@id=username]","xpath")``

        :Return: String : return locator of elements.
        """
        elements = None
        try:
            locatorType = locatorType.lower()
            byType = self.get_by_type(locatorType)
            elements = self.driver.find_elements(byType, locator)
            self.log.info("Elements found with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.log.info("Elements not found with locator: " + locator + " and locatorType: " + locatorType)
        return elements

    def element_click(self, locator, locatorType="id"):
        """
        :Description:
            - The primary function of this method is to perform click operation on element present on page.

        :Parameter:
            - locatorType - Accepts type of locator and by default it accepts id as an locator

        :Example:
            - ``element_click("username","id")``
            - ``element_click("//*[@id=username]","xpath")``

        :Return: Bool : True on Pass and False on Failures
        """
        try:
            element = self.get_element(locator, locatorType)
            element.click()
            return True
        except:
            # print_stack()
            return False

    def element_send_data(self, data,locator, locatorType="id"):
        """
        :Description:
            - The primary function of this method is to sent data to element present on page.

        :Parameter:
            - locatorType - Accepts type of locator and by default it accepts id as an locator

        :Example:
            - ``element_send_data("abc@gmail.com","username","id")``
            - ``element_send_data("abc@gmail.com","//*[@id=username]","xpath")``

        :Return: Bool : True on Pass and False on Failures
        """
        try:
            element = self.get_element(locator, locatorType)
            element.send_keys(data)
            return True
        except:
            print_stack()
            return False

    def is_element_present(self, locator, locatorType="id"):
        """
        :Description:
            - The primary function of this method is to check element present on page.

        :Parameter:
            - locatorType - Accepts type of locator and by default it accepts id as an locator

        :Example:
            - ``is_element_present("username","id")``
            - ``is_element_present("//*[@id=username]","xpath")``

        :Return: Bool : True on Pass and False on Failures
        """
        try:
            element = self.get_element(locator, locatorType)
            if element is not None:
                return True
            else:
                return False
        except:
            self.log.info("Element not found")
            return False

    def elements_presence_check(self, locator, locatorType="id"):
        """
        :Description:
            - The primary function of this method is to check elements present on page.

        :Parameter:
            - locatorType - Accepts type of locator and by default it accepts id as an locator

        :Example:
            - ``elements_presence_check("username","id")``
            - ``elements_presence_check("//*[@id=username]","xpath")``

        :Return: Bool : True on Pass and False on Failures
        """
        try:
            elementList = self.get_elements(locator, locatorType)
            if len(elementList) > 0:
                return True
            else:
                return False
        except:
            return False

    def wait_for_element(self, locator, locatorType="id",
                               timeout=10, pollFrequency=0.5):
        """
        :Description:
            - The primary function of this method is to wait for certain duration until that element present
            on that page.

        :Parameter:
            - locator - Accepts element locator
            - locatorType - Accepts type of locator and by default it accepts id as an locator
            - timeout - Accepts timeout till whicch it wait for that duration by defaults value is 10 seconds
            - pollFrequency - It accept time duration on which it will check again for that element.

        :Example:
            - ``wait_for_element("username","id",timeout=30,pollFrequency=10)``

        :Return: String : It will return element if it is present
        """
        element = None
        try:
            byType = self.get_by_type(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType,
                                                             locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def information(self,message):
        """
        :Description:
            - The primary function of this method is to print information.

        :Parameter:
            - message - It accepts message which to be print or logged as an info for end user.

        :Example:
            - ``information("You have Log in successfully")``

        :Return: None
        """
        self.log.info(message)
