import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_cart_button_is_displayed(browser):
    browser.get(link)
    button_is_visible = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket").is_displayed()
    assert button_is_visible is True

