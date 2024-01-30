from pytest import mark
from core.data_classes import Config
from pages.shop_page.object import ShopPageObj

# Scenario:
# 1. Go to “http://practice.automationtesting.in/shop”
# 2. Verify the shop page title
# 3. Click the Android product link in the product category


@mark.demo
def test_demo(config: Config):
    config.log.info("Test the product categories")
    shop_page = ShopPageObj(config)
    shop_page.open()
    shop_page.verify_page_title()
    shop_page.select_android()
