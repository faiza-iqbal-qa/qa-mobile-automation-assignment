from pages.base_page import BasePage

class ViewsPage(BasePage):
    EXPANDABLE_LISTS = "Expandable Lists"

    def open_expandable_lists(self):
        self.click_text(self.EXPANDABLE_LISTS)
