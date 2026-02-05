from pages.base_page import BasePage

class AppPage(BasePage):
    ACTIVITY = "Activity"

    def open_activity(self):
        self.click_text(self.ACTIVITY)
