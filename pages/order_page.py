import time

from Sprint_4.generators import generate_name
from Sprint_4.locators.locators import OrderPageLocators


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    # def enter_name(self):
    #     name_input = self.driver.find_element(*OrderPageLocators.FIRST_NAME_INPUT )
    #     name_input.send_keys(generate_name())

    #
    # def enter_surname(self, surname):
    #     surname_input = self.driver.find_element(By.XPATH, ".//input[@placeholder='* Фамилия']")
    #     surname_input.send_keys(surname)
    #
    # def enter_address(self, address):
    #     address_input = self.driver.find_element(By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    #     address_input.send_keys(address)
    #
    # def select_random_station(self):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(EC.presence_of_element_located((By.CLASS_NAME, "select-search__input")))
    #     input_elem = self.driver.find_element(By.CLASS_NAME, "select-search__input")
    #     input_elem.click()
    #     options = self.driver.find_elements(By.CLASS_NAME, "select-search__option")
    #     random_station = random.choice(options)
    #     random_station.click()
    #
    # def enter_phone_number(self, phone_number):
    #     phone_input = self.driver.find_element(By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    #     phone_input.send_keys(phone_number)
    #
    # def click_next_page_button(self):
    #     next_page_button = self.driver.find_element(By.CLASS_NAME, 'Button_Button__ra12g.Button_Middle__1CSJM')
    #     next_page_button.click()
    #     time.sleep(2)
    #
    # def select_date(self, date):
    #     date_picker = self.driver.find_element(By.CSS_SELECTOR, "div.react-datepicker__input-container > input")
    #     date_picker.send_keys(date)
    #     time.sleep(2)
    #     # click outside the date picker to close it
    #     self.driver.find_element(By.XPATH, '//body').click()
    #
    # def select_rental_period(self, rental_period):
    #     rental_period_dropdown = self.driver.find_element(By.CLASS_NAME, "Dropdown-placeholder")
    #     rental_period_dropdown.click()
    #     rental_period_option = self.driver.find_element(By.XPATH,
    #                                                     f'//div[@class="Dropdown-option" and @role="option" and @aria-selected="false" and contains(text(), "{rental_period}")]')
    #     rental_period_option.click()
    #
    # def enter_comment(self, comment):
    #     comment_input = self.driver.find_element(By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    #     comment_input.send_keys(comment)
    #
    # def click_order_button(self):
    #     order_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[3]/button[2]")
    #     order_button.click()
    #
    # def click_confirm_order_button(self):
    #     confirm_order_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[5]/div[2]/button[2]")
    #     confirm_order_button.click()
    #
    # def check_order_success(self):
    #     self.driver.find_element(By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
    #     time.sleep(2)
    def go_to_yandex(self):
        logo_link = self.driver.find_element(*OrderPageLocators.YANDEX_LOGO)
        logo_link.click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def go_to_scooter_home(self):
        logo_link = self.driver.find_element(*OrderPageLocators.SAMOKAT_LOGO)
        logo_link.click()
        assert self.driver.current_url == "https://qa-scooter.praktikum-services.ru/"