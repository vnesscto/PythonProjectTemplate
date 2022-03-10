from pages.login_page import Login_Page

# declare variables for all your web pages
# and initialize them in init_all_web_pages method
# example init of example test project login page
login_page = None


class InitPages:

    @staticmethod
    def init_all_web_pages(driver):
        globals()['login_page'] = Login_Page(driver)

    @staticmethod
    def init_desktop_pages(driver):
        pass

    @staticmethod
    def init_mobile_pages(driver):
        pass
