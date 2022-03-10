class Base_Page:
    def __init__(self, driver):
        self.driver = driver

    def go_to_url(self, url_str):
        self.driver.get(url_str)