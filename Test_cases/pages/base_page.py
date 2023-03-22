class BasePage():
    def __init__(self, driver, url):
        self.driver = driver
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.url = url
        self.driver.get(self.url)


