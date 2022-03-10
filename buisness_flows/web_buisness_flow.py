import pages.login_page
import utilities.manage_pages
from utilities import common_methods


class TestProjectExample:
    @staticmethod
    def login(user_name: str, password: str) -> bool:
        example_page: pages.login_page.Login_Page = utilities.manage_pages.login_page
        common_methods.write_text(example_page.get_user_name_element(), user_name)
        common_methods.write_text(example_page.get_password_element(), password)
        common_methods.click(example_page.get_login_element())
        # common_methods.wait_and_click(example_page.get_login_element(), example_page.get_login_by())
        return example_page.get_logout_element().is_displayed()

    @staticmethod
    def choose_country(country_name: str) -> str:
        example_page: pages.login_page.Login_Page = utilities.manage_pages.login_page
        if not example_page.get_logout_element().is_displayed():
            TestProjectExample.login('abc', '12345')
        common_methods.select_drop_down_by_text(example_page.get_select_country_element(), country_name)
        common_methods.select_drop_down_by_index(example_page.get_select_country_element(), 1)
        common_methods.wait(2)
        # common_methods.select_drop_down_by_text(example_page.get_select_country_element(), country_name)
        # common_methods.wait_and_click(example_page.get_login_element(), example_page.get_login_by())
        return 'abc'

    @staticmethod
    def js_actions_test(user_name: str, password: str) -> bool:
        example_page: pages.login_page.Login_Page = utilities.manage_pages.login_page
        common_methods.write_text(example_page.get_user_name_element(), user_name)
        common_methods.scroll_down(100)
        common_methods.write_text(example_page.get_password_element(), password)
        common_methods.scroll_up(100)
        #common_methods.click(example_page.get_login_element())
        common_methods.js_scroll_to_element(example_page.get_login_element())
        common_methods.js_click(example_page.get_login_element())
        # common_methods.wait_and_click(example_page.get_login_element(), example_page.get_login_by())
        return example_page.get_logout_element().is_displayed()