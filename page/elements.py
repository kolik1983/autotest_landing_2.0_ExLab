import time
from termcolor import colored

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver import Remote as RemoteWebDriver, ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class WebElement(object):

    _locator = ('', '')
    _web_driver = None
    _page = None
    _timeout = 10
    _wait_after_click = False  # TODO: how we can wait after click?

    def __init__(self, timeout=10, wait_after_click=False, **kwargs):
        self._timeout = timeout
        self._wait_after_click = wait_after_click

        for attr in kwargs:
            self._locator = (str(attr).replace('_', ' '), str(kwargs.get(attr)))

    def find(self, timeout=10):
        """ Find element on the page. """

        element = None

        try:
            element = WebDriverWait(self._web_driver, timeout).until(
               EC.presence_of_element_located(self._locator)
            )
        except:
            print(colored('Element not found on the page!', 'red'))

        return element

    def wait_to_be_clickable(self, timeout=10, check_visibility=True):
        """ Wait until the element will be ready for click. """

        element = None

        try:
            element = WebDriverWait(self._web_driver, timeout).until(
                EC.element_to_be_clickable(self._locator)
            )
        except:
            print(colored('Element not clickable!', 'red'))

        if check_visibility:
            self.wait_until_not_visible()

        return element

    def is_clickable(self):
        """ Check is element ready for click or not. """

        element = self.wait_to_be_clickable(timeout=0.1)
        return element is not None

    def is_presented(self):
        """ Check that element is presented on the page. """

        element = self.find(timeout=0.1)
        return element is not None

    def is_visible(self):
        """ Check is the element visible or not. """

        element = self.find(timeout=2)
        self.wait_until_not_visible(2)

        if element:
            return element.is_displayed()

        return False

    def wait_until_not_visible(self, timeout=10):

        element = None

        try:
            element = WebDriverWait(self._web_driver, timeout).until(
                EC.visibility_of_element_located(self._locator)
            )
        except:
            print(colored('Element not visible!', 'red'))

        if element:
            js = ('return (!(arguments[0].offsetParent === null) && '
                  '!(window.getComputedStyle(arguments[0]) === "none") &&'
                  'arguments[0].offsetWidth > 0 && arguments[0].offsetHeight > 0'
                  ');')
            visibility = self._web_driver.execute_script(js, element)
            iteration = 0

            while not visibility and iteration < 10:
                time.sleep(0.5)

                iteration += 1

                visibility = self._web_driver.execute_script(js, element)
                print('Element {0} visibility: {1}'.format(self._locator, visibility))

        return element

    def get_attribute(self, attr_name):
        """ Get attribute of the element. """

        element = self.find()

        if element:
            return element.get_attribute(attr_name)

    def click(self, hold_seconds=0, x_offset=1, y_offset=1):
        """ Wait and click the element. """

        element = self.wait_to_be_clickable()

        if element:
            action = ActionChains(self._web_driver)
            action.move_to_element_with_offset(element, x_offset, y_offset).\
                pause(hold_seconds).click(on_element=element).perform()
        else:
            msg = 'Element with locator {0} not found'
            raise AttributeError(msg.format(self._locator))

        if self._wait_after_click:
            self._page.wait_page_loaded()


    def scroll_to_element(self):
        """ Scroll page to the element. """

        element = self.find()

        # Scroll page to the element:
        # Option #1 to scroll to element:
        try:
            self._web_driver.execute_script("arguments[0].scrollIntoView();", element)
        except Exception as e:
            pass
        # Option #2 to scroll to element:
        # try:
        #     element.send_keys(Keys.DOWN)
        # except Exception as e:
        #     pass  # Just ignore the error if we can't send the keys to the element
    #
    # def open_spoilers(self):
    #     try:
    #
    #         count_it = len(self.find())
    #
    #         for area in range(1, count_it + 1):
    #             what_to_click = self.find(area)
    #             self._web_driver.execute_script("arguments[0].scrollIntoView();", what_to_click)
    #             what_to_click.click()
    #
    #     except NoSuchElementException:
    #         return False
    #     return True

class ManyWebElements(WebElement):

    def __getitem__(self, item):
        """ Get list of elements and try to return required element. """

        elements = self.find()
        return elements[item]

    def finds(self, timeout=15):
        """ Find elements on the page. """

        elements = []

        try:
            elements = WebDriverWait(self._web_driver, timeout).until(
               EC.presence_of_all_elements_located(self._locator)
            )
        except:
            print(colored('Elements not found on the page!', 'red'))

        return elements

    # def click(self, hold_seconds=0, x_offset=0, y_offset=0):
    #     """ Note: this action is not applicable for the list of elements. """
    #     raise NotImplemented('This action is not applicable for the list of elements')

    def count(self):
        """ Get count of elements. """

        elements = self.finds()
        return len(elements)

    def open_spoilers(self):
        try:

            count_it = len(self.finds())

            for area in range(1, count_it + 1):
                what_to_click = self.find(area)
                self._web_driver.execute_script("return arguments[0].scrollIntoView();", what_to_click)
                what_to_click.click()

        except NoSuchElementException:
            return False
        return True
