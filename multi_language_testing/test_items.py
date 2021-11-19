from selenium.webdriver.common.by import By


def test_add_to_basket_button_existence(browser):
    browser.implicitly_wait(5)
    button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert button, "No button"
