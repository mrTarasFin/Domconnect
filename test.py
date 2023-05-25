import pytest
from pages.page_form import FormPage
from locators.locator_form import PageLocators as Locators


@pytest.mark.search_site
def test_one_part(browser):
    site = FormPage(browser)
    site.open_site()
    site.find_bth_login()
    site.enter_email("demo-tt1@inet-yar.ru")
    site.enter_password("rNCV14la")
    site.login_in()
    site.find_ip()
