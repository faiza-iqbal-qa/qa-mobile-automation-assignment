from pages.base_page import BasePage

class ActivityPage(BasePage):
    CUSTOM_TITLE = "Custom Title"

    def open_custom_title(self):
        self.click_text(self.CUSTOM_TITLE)
