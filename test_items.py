import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def is_element_present(browser):
    try:
        browser.implicitly_wait(10)
        browser.find_element_by_css_selector("#add_to_basket_form > button")
        return True
    except:
        return False

def test_add_to_basket_button(browser):
    browser.get(link)
    # time.sleep(30)
    assert is_element_present(browser) == True, "кнопка не найдена"