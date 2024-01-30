from core.data_classes import Config
from pages.my_account_page.object import MyAccountPageObj, LoginFailedException


def test_user_orders(config: Config):
    """
    Test function to navigate to the Orders page after logging into My Account.

    Args:
        config (Config): Configuration object containing logging and driver information.
    """
    config.log.info("Testing user orders")

    # Step 1: Initialize MyAccountPageObj
    account_page = MyAccountPageObj(config)

    # Step 2: Open the browser and navigate to the URL
    account_page.open()

    # Step 3: Login with valid credentials
    try:
        account_page.login("testuser@xyz.com", "test_pwd123")
    except LoginFailedException as e:
        config.log.error(f"Login failed: {e}")
        raise AssertionError("Login failed.")

    # Step 4: Handle ads (if any)
    account_page.close_ads()

    # Step 5: Navigate to Orders page
    if not account_page.navigate_to_orders():
        raise AssertionError("Failed to navigate to Orders page.")

    # Print log if all tests pass
    config.log.info("All tests passed successfully.")
