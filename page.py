#Todos los localizadores y métodos
from typing import Any

from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import data
from selenium.webdriver.common.by import By



class UrbanRoutesPage:
    #Localizadores
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    button_pedir_taxi = (By.CSS_SELECTOR, 'button.round')
    comfort_rate = (By.XPATH, "//div[text()='Comfort' and @class='tcard-title']")
    phone_field = (By.CSS_SELECTOR, '.np-text')
    phone_window = (By.XPATH, "//div[text()= 'Introduce tu número de teléfono']")
    number_phone_field = (By.XPATH, "//label[@for='phone']")
    write_phone_field = (By.XPATH, "//input[@id='phone']")
    metodo_pago_field = (By.XPATH, "//div[text()='Método de pago' and @class='pp-text']")
    next_button = (By.XPATH, "//button[text()='Siguiente']")
    code_input = (By.ID, "code")
    confirm_button = (By.XPATH, "//button[text()='Confirmar']")
    add_card_trigger = (By.XPATH, "//div[contains(@class,'pp-plus-container')]")
    card_number_input = (By.XPATH, "//div[.//div[text()='Agregar tarjeta']]//input[@id='number']")
    card_cvv_input = (By.XPATH, "//div[contains(@class,'card-code-input')]//input[@id='code']"
    )
    add_card_button = (
        By.XPATH,
        "//div[.//div[text()='Agregar tarjeta']]//button[text()='Agregar']"
    )
    close_payment_modal_button = (
        By.XPATH,
        "//div[contains(@class,'pp-button')]//ancestor::div[contains(@class,'modal')]//button[contains(@class,'section-close')]"
    )
    add_card_section_active = (
        By.XPATH,
        "//div[contains(@class,'section') and contains(@class,'active')]//div[text()='Agregar tarjeta']"
    )
    message_input = (By.ID, "comment")
    blanket_switch = (By.XPATH, "//div[.//div[text()='Manta y pañuelos']]//span[@class='slider round']")
    ice_plus = (By.XPATH, "//div[.//div[text()='Helado']]//div[contains(@class,'counter-plus')]")
    smart_button = (By.XPATH, "//button[contains(@class,'smart-button')]")
    switch_blanket_assert = (By.CLASS_NAME, 'switch-input')
    ice_assert = (By.CLASS_NAME, 'counter-value')
    order_popup = (By.CLASS_NAME, 'order-body')
    DRIVER_ARRIVAL_TITLE = (By.XPATH, "//div[contains(@class, 'order-header-title') and contains(text(), 'conductor')]")

    #Constructor
    def __init__(self, driver):
        self.driver = driver

    #Metodos
    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def click_button_pedir_taxi(self):
        boton_pedir_taxi = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.button_pedir_taxi)).click()

    def click_comfort_rate(self):
        opcion_comfort = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.comfort_rate)).click()

    def extraer_texto_confort_rate(self):
        opcion_comfort = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.comfort_rate))
        return opcion_comfort.text

    def click_phone_number(self):
        phone_number = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.phone_field)).click()

    def extraer_texto_phone_window(self):
        ventana_phone = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.phone_window))
        return ventana_phone.text

    def click_phone_number_field(self):
        phone_number_field = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.number_phone_field)).click()

    def write_phone_number(self, phone_number):
        escribir_phone = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.write_phone_field)).send_keys(phone_number)

    def click_metodo_pago(self):
        pago_metodo = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.metodo_pago_field)).click()

    def click_next_button(self):
        boton_siguiente = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.next_button)).click()

    def set_code(self, code):
            WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.code_input))
            self.driver.find_element(*self.code_input).send_keys(code)

    def confirm_code(self):
            self.driver.find_element(*self.confirm_button).click()

    def click_add_card(self):
        element = WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.add_card_trigger)).click()

    def wait_for_add_card_section(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.add_card_section_active)
        )

    def add_card(self, number, cvv):
        # 1. Esperar a que la sección esté activa
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[contains(@class,'section') and contains(@class,'active')]//div[text()='Agregar tarjeta']")))
        # 2. Input de Número de tarjeta
        card_number_element = WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.card_number_input))
        card_number_element.click()  # activar input
        card_number_element.send_keys(number)
        card_number_element.send_keys(Keys.TAB)
        # 3. Input de CVV
        cvv_element = WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.card_cvv_input)
        )
        cvv_element.click()  # activar input
        cvv_element.send_keys(cvv)
        # 4. Perder foco (activar botón)
        cvv_element.send_keys(Keys.TAB)
        # 5. Esperar botón habilitado
        add_button = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.add_card_button)
        )
        # 6. Click en Agregar
        add_button.click()

    def close_payment_modal(self):
            close_button = WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable(self.close_payment_modal_button)
            )
            close_button.click()

    def set_message_to_driver(self, message):
        message_field = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.message_input)
        )
        message_field.send_keys(message)

    def set_blanket(self):
        self.driver.find_element(*self.blanket_switch).click()

    def add_ice(self, times=2):
        for _ in range(times):
            self.driver.find_element(*self.ice_plus).click()

    def click_smart_button(self):
        WebDriverWait(self.driver, 10).until(

            expected_conditions.element_to_be_clickable(self.smart_button)

        ).click()

    def get_phone(self):
        return self.driver.find_element(*self.write_phone_field).get_property('value')

    def get_card(self):
        return self.driver.find_element(*self.card_number_input).get_property('value')

    def get_cvv(self):
        return self.driver.find_element(*self.card_cvv_input).get_property('value')

    def get_text(self):
        return self.driver.find_element(*self.message_input).get_property('value')

    def get_checked_unchecket(self):
        switches = self.driver.find_elements(*self.switch_blanket_assert)
        return switches[0].get_property('checked')

    def get_dos_nieves(self):
        return int(self.driver.find_elements(*self.ice_assert)[0].text)

    def wait_order_taxi_popup(self):
        WebDriverWait(self.driver, 3).until(

            expected_conditions.visibility_of_element_located(self.order_popup))

    def wait_for_driver_assignment(self):
        return WebDriverWait(self.driver, 60).until(
            expected_conditions.visibility_of_element_located(self.DRIVER_ARRIVAL_TITLE)
        )

    def get_driver_info_text(self):
        element = self.wait_for_driver_assignment()
        return element.text

