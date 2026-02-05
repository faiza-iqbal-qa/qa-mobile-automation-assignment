from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class HomePage(BasePage):
    VIEWS = "Views"
    APP = "App"

    def verify_loaded(self):
        # On the real home list, "Accessibility" and "App" should exist
        assert self.exists_text("Accessibility", timeout=25), "API Demos home list didn't load"
        assert self.exists_text("App", timeout=25), "API Demos home list didn't load (App not found)"

    def scroll_to_text(self, text: str):
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView('
            f'new UiSelector().text("{text}"));'
        )

    def open_views(self):
        self.scroll_to_text(self.VIEWS)
        self.click_text(self.VIEWS)

    def open_app(self):
        self.click_text(self.APP)
