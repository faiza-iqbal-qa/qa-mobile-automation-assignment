from pages.base_page import BasePage

class CustomTitlePage(BasePage):
    LEFT = "Left is best"
    RIGHT = "Right is always right"

    def verify_loaded(self):
        assert self.exists_text(self.LEFT, timeout=15), "Left title text not found"
        assert self.exists_text(self.RIGHT, timeout=15), "Right title text not found"
