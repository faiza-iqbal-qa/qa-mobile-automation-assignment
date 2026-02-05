from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _locator_text(self, text: str):
        return (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{text}")')

    def wait_for_text(self, text: str, timeout: int = 20):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(self._locator_text(text))
        )

    def wait_clickable_text(self, text: str, timeout: int = 20):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self._locator_text(text))
        )

    def click_text(self, text: str, timeout: int = 20):
        el = self.wait_clickable_text(text, timeout)
        el.click()
        return el

    def exists_text(self, text: str, timeout: int = 6) -> bool:
        try:
            self.wait_for_text(text, timeout)
            return True
        except Exception:
            return False

    def back(self, times: int = 1):
        for _ in range(times):
            self.driver.back()

    def back_until_text(self, text: str, max_backs: int = 6):
        """
        Go back until a given text appears, or until max_backs reached.
        Prevents overshooting out of the app.
        """
        for _ in range(max_backs):
            if self.exists_text(text, timeout=2):
                return True
            self.driver.back()
        return self.exists_text(text, timeout=2)
