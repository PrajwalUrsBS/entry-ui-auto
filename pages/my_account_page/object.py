from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from core.base_page import BaseScreen
from core.data_classes import Config
from core.exceptions import LoginFailedException
from pages.my_account_page.elements import MyAccountPageElements


class MyAccountPageObj(BaseScreen):
    def __init__(self, config: Config):
        super().__init__(config)
        self.resource_url = "my-account"
        self.elements = MyAccountPageElements()

    def open(self):
        """
        Open the My Account page.
        """
        self.log.info(f"Open the {self.url} page")
        self.driver.get(self.url)

    def login(self, username, password):
        """
        Log in to My Account using provided credentials.

        Args:
            username (str): The username to log in with.
            password (str): The password to log in with.

        Returns:
            bool: True if login is successful, False otherwise.
        """
        self.log.info("Logging in to My Account")
        self.se_helper.get_element(self.elements.username_textbox).send_keys(username)
        self.se_helper.get_element(self.elements.password_textbox).send_keys(password)
        self.se_helper.get_element(self.elements.login_button).click()

        try:
            # Wait for a success indicator element
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="page-36"]/div/div[1]/nav/ul/li[6]/a'))
            )
            self.log.info("Login successful.")
            return True
        except TimeoutException:
            # Check if the error message element is present
            try:
                error_message = self.driver.find_element(By.XPATH,
                                                         '//*[contains(text(), "Error: The password you entered")]')
                error_text = error_message.text
                self.log.error(f"Login failed. Error message: {error_text}")
                raise LoginFailedException("Login failed. Incorrect username or password.")
            except NoSuchElementException:
                self.log.error("Login failed. Error message not found.")
                raise LoginFailedException("Login failed. Error message not found.")

    def navigate_to_orders(self):
        """
        Navigate to the Orders page.

        Returns:
            bool: True if navigation is successful, False otherwise.
        """
        self.log.info("Navigating to Orders page")
        try:
            # Handle ads if present
            self.close_ads()

            # Click on My Account menu
            self.se_helper.get_element(self.elements.my_account_menu).click()
            # Wait for the orders link to be clickable
            orders_link = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH,
                                            '//*[@id="page-36"]/div/div[1]/nav/ul/li[2]/a')))
            orders_link.click()

            # Wait for the URL to change to the Orders page URL
            WebDriverWait(self.driver, 20).until(
                lambda driver: driver.current_url == 'https://practice.automationtesting.in/my-account/orders/')

            self.log.info("Successfully navigated to Orders page.")
            return True
        except TimeoutException:
            self.log.error("Timeout occurred while waiting for orders link or navigating to Orders page.")
            return False

    def close_ads(self):
        """
        Close any dynamic ads that may appear on the page.
        """
        ad_closed = False

        # Try closing the ad using the dismiss button by ID
        try:
            dismiss_button = WebDriverWait(self.driver, 1).until(
                EC.element_to_be_clickable((By.ID, 'dismiss-button'))
            )
            dismiss_button.click()
            self.log.info("Closed the ad using the dismiss button by ID.")
            ad_closed = True
        except TimeoutException:
            pass  # Dismiss button not found or not clickable

        # If ad is not closed yet, try closing it using the close button by class name
        if not ad_closed:
            try:
                close_button = WebDriverWait(self.driver, 1).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, 'btn.skip'))
                )
                close_button.click()
                self.log.info("Closed the ad using the close button by class name.")
                ad_closed = True
            except TimeoutException:
                pass  # Close button not found or not clickable

        # If ad is not closed yet, try closing it using the close button by XPATH
        if not ad_closed:
            try:
                close_button = WebDriverWait(self.driver, 1).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="dismiss-button"]'))
                )
                close_button.click()
                self.log.info("Closed the ad using the close button by XPATH.")
                ad_closed = True
            except TimeoutException:
                pass  # Close button not found or not clickable

        # If ad is not closed yet, try closing it using the body element
        if not ad_closed:
            try:
                body = WebDriverWait(self.driver, 1).until(
                    EC.element_to_be_clickable((By.TAG_NAME, 'body'))
                )
                body.click()
                self.log.info("Closed the ad using the body element.")
                ad_closed = True
            except TimeoutException:
                pass  # Body element not found or not clickable

        if not ad_closed:
            self.log.info("No dismiss, close button, or body element found to close the ad.")

        return ad_closed

