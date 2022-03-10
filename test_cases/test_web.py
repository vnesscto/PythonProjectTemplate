import allure
import pytest

from buisness_flows.web_buisness_flow import TestProjectExample

# an example tests class for the example test project login page


@pytest.mark.usefixtures('init_web')
class Test_Web:

    @allure.title("Login to test project example")
    @allure.description("This test verify successful login to test project example website")
    def test_login(self):
        actual_res = TestProjectExample.login('abc', '12345')
        expected_res = True
        assert actual_res == expected_res

    @allure.title(" js Login to test project example")
    @allure.description("This test verify successful login with js actions")
    def test_js_login(self):
        actual_res = TestProjectExample.js_actions_test('abc', '12345')
        expected_res = True
        assert actual_res == expected_res

    def test_choose_country(self):
        country = 'Israel'
        actual_res = TestProjectExample.choose_country(country)
        expected_res = 'abc'
        assert actual_res == expected_res
