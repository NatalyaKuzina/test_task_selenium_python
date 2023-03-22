from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    def push_elemets_button(self):
        button_elements = self.driver.find_element(By.XPATH, "//h5[text()='Elements']")
        self.driver.execute_script("arguments[0].scrollIntoView();", button_elements)
        # i prefer use ActionChains(self.driver).move_to_element(button_elements).click().perform()
        # but this site work normally whis simple click
        button_elements.click()

    def open_checkbox_page(self):
        button_check_box = self.driver.find_element(By.XPATH, "//span[text()='Check Box']")
        button_check_box.click()

    def push_toggle_home(self):
        toggle_home = self.driver.find_element(By.CSS_SELECTOR, "[class='rct-icon rct-icon-expand-close']")
        toggle_home.click()

    def push_toggle_downloads(self):
        toggle_downloads = self.driver.find_elements(By.CSS_SELECTOR, "[class='rct-collapse rct-collapse-btn']")[3]
        toggle_downloads.click()

    def choose_checkbox_wordfile(self):
        checkbox_wordFile = self.driver.find_element(By.CSS_SELECTOR, "[for='tree-node-wordFile']")
        # or checkbox_wordFile = self.driver.find_elements(By.CSS_SELECTOR, "[class='rct-checkbox']")[4]
        checkbox_wordFile.click()
        text_element_first = self.driver.find_element(By.XPATH, "//span[text()='You have selected :']")
        assert text_element_first.text == 'You have selected :', "Real: " + str(text_element_first.text)
        text_element_second = self.driver.find_element(By.CSS_SELECTOR, "[class='text-success']")
        assert text_element_second.text == 'wordFile', "Real: " + str(text_element_second.text)
