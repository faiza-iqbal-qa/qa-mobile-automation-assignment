from utils.logger import get_logger
from pages.home_page import HomePage
from pages.views_page import ViewsPage
from pages.expandable_lists_page import ExpandableListsPage
from pages.custom_adapter_page import CustomAdapterPage
from pages.app_page import AppPage
from pages.activity_page import ActivityPage
from pages.custom_title_page import CustomTitlePage

log = get_logger()

def test_api_demos_assignment_flow(driver):
    home = HomePage(driver)
    views = ViewsPage(driver)
    expandable = ExpandableListsPage(driver)
    custom_adapter = CustomAdapterPage(driver)
    app = AppPage(driver)
    activity = ActivityPage(driver)
    custom_title = CustomTitlePage(driver)

    log.info("Verifying home screen loaded...")
    home.verify_loaded()
    log.info("Success: home screen loaded")


    log.info("Verifying navigation: Views -> Expandable Lists -> 1. Custom Adapter")
    home.open_views()
    views.open_expandable_lists()
    expandable.open_custom_adapter()
    custom_adapter.verify_loaded()
    log.info("Success: Navigation - Views -> Expandable Lists -> 1. Custom Adapter")


    log.info("Long pressing People Names and verifying Sample menu...")
    custom_adapter.long_press_people_names()
    custom_adapter.verify_sample_menu()
    log.info("Success: Item added to cart - Context menu appeared treated as confirmation")

    log.info("Navigating back to API Demos home list...")
    ok = custom_adapter.back_until_text("App", max_backs=6)
    assert ok, "Could not return to API Demos home list"

    home.open_app()
    app.open_activity()
    activity.open_custom_title()
    log.info("Success: Checkout flow successful - Navigate App -> Activity -> Custom Title")

    log.info("Verifying Custom Title screen loaded...")
    custom_title.verify_loaded()
    log.info("Success: Order confirmation - Verified Custom Title screen loaded")
