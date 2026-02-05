from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains

class CustomAdapterPage(BasePage):
    PEOPLE_NAMES = "People Names"
    SAMPLE_MENU = "Sample menu"

    def verify_loaded(self):
        # Give it more time on slower emulators
        assert self.exists_text(self.PEOPLE_NAMES, timeout=25), "Custom Adapter screen did not load"

    def long_press_people_names(self):
        el = self.wait_for_text(self.PEOPLE_NAMES, timeout=25)
        ActionChains(self.driver).click_and_hold(el).pause(1.2).release().perform()

    def verify_sample_menu(self):
        assert self.exists_text(self.SAMPLE_MENU, timeout=15), '"Sample menu" did not appear'
