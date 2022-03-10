import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import utilities.files_reader
import utilities.manage_pages
import utilities.base_driver
#from utilities import base_driver
from utilities.files_reader import get_data


@pytest.fixture(scope='class')
def init_web(request):
    platform: str = utilities.files_reader.get_data("BrowserType")
    if platform.lower() == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif platform.lower() == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif platform.lower() == 'ie':
        driver = webdriver.Ie(IEDriverManager().install())
    elif platform.lower() == 'edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    else:
        raise Exception("Wrong Browser")
    driver.maximize_window()
    driver.get(utilities.files_reader.get_data("webUrl"))
    driver.implicitly_wait(10)
    utilities.base_driver.driver = driver
    # request.cls.driver = driver
    utilities.manage_pages.InitPages.init_all_web_pages(driver)
    yield
    driver.quit()


# @pytest.fixture(scope='class')
# def init_mobile(request):
#     dc = {}
#     dc['reportDirectory'] = get_data('reportDirectory')
#     dc['reportFormat'] = get_data('reportFormat')
#     dc['testName'] = get_data('testName')
#     dc['udid'] = get_data('udid')
#     dc['appPackage'] = get_data('appPackage')
#     dc['appActivity'] = get_data('appActivity')
#     dc['platformName'] = get_data('platformName')
#     driver = webdriver.Remote(get_data('server'), dc)
#     utilities.base_driver.driver = driver
#     utilities.manage_pages.InitPages.init_mobile_pages(driver)
#     yield
#     driver.quit()
#
#
# pytest.fixture(scope='class')
# def init_desktop(request):
#     desired_caps = {}
#     desired_caps["app"] = get_data("dc_app")
#     desired_caps["platformName"] = get_data("dc_platformName")
#     desired_caps["deviceName"] = get_data("deviceName")
#     driver = webdriver.Remote(get_data("dc_server"), desired_caps)
#     utilities.base_driver.driver = driver
#     request.cls.driver = driver
#     utilities.manage_pages.InitPages.init_desktop_pages(driver)
#     yield
#     driver.quit()
