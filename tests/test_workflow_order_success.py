import pytest
from pages import HomePage
from selenium import webdriver


@pytest.fixture(scope="class")
def chrome_driver_init(request):
    chrome_driver = webdriver.Chrome()
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()


@pytest.fixture(scope="class")
def firefox_driver_init(request):
    firefox_driver = webdriver.Firefox()
    request.cls.driver = firefox_driver
    yield
    firefox_driver.close()


@pytest.mark.usefixtures("chrome_driver_init")
class TestOrderPageChrome:

    def test_order_scooter(self):
        home_page = HomePage(self.driver)
        home_page.go_to_home_page()
        home_page.accept_cookies()
        order_page = home_page.click_order_button()
        order_page.enter_name("John")
        order_page.enter_email("john@example.com")
        order_page.select_scooter("Classic")
        order_page.click_submit_button()
        assert order_page.get_success_message() == "Thank you, John! Your order for Classic scooter is confirmed!"

    def test_order_scooter_no_name(self):
        home_page = HomePage(self.driver)
        home_page.go_to_home_page()
        home_page.accept_cookies()
        order_page = home_page.click_order_button()
        order_page.enter_email("john@example.com")
        order_page.select_scooter("Classic")
        order_page.click_submit_button()
        assert order_page.get_error_message() == "Please enter your name."
