from selenium.webdriver.common.by import By


def test_add_to_basket_button_existence(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    browser.implicitly_wait(5)
    browser.get(link)
    button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert button, "No button"
