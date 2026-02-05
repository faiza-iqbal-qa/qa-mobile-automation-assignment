from pages.base_page import BasePage

class ExpandableListsPage(BasePage):
    CUSTOM_ADAPTER = "1. Custom Adapter"

    def verify_loaded(self):
        # This screen should show the menu options
        assert self.exists_text(self.CUSTOM_ADAPTER, timeout=15), "Expandable Lists menu did not load"

    def open_custom_adapter(self):
        self.verify_loaded()
        self.click_text(self.CUSTOM_ADAPTER, timeout=20)
