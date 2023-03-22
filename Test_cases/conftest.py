import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.main_page import MainPage
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

#variables
link = "https://demoqa.com/"

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")

def driver(request):
    browser_name = request.config.getoption("browser_name")
    driver = None
    if browser_name == "chrome":
        chrome_options = ChromeOptions()
        # chrome_options.add_argument("--window-size=1920,1080")
        # chrome_options.add_argument("--disable-extensions")
        # chrome_options.add_argument("--proxy-server='direct://'")
        # chrome_options.add_argument("--proxy-bypass-list=*")
        # chrome_options.add_argument("--start-maximized")
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument('--disable-dev-shm-usage')
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--ignore-certificate-errors')
        # chrome_options.add_argument('disable-infobars')
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    elif browser_name == "firefox":
        firefox_options = FirefoxOptions()
        # firefox_options.add_argument("--window-size=1920,1080")
        # firefox_options.add_argument("--disable-extensions")
        # firefox_options.add_argument("--proxy-server='direct://'")
        # firefox_options.add_argument("--proxy-bypass-list=*")
        # firefox_options.add_argument("--start-maximized")
        # firefox_options.add_argument('--headless')
        # firefox_options.add_argument('--disable-gpu')
        # firefox_options.add_argument('--disable-dev-shm-usage')
        # firefox_options.add_argument('--no-sandbox')
        # firefox_options.add_argument('--ignore-certificate-errors')
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=firefox_options)

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    return driver

@pytest.fixture(scope="function")
def page(request):
    page = MainPage(driver(request), link)
    yield page
    page.driver.quit()
