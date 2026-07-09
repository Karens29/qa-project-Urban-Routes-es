import data
from page import UrbanRoutesPage
from helpers import retrieve_phone_code
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    #1. Configurar la dirección
    def test_set_route(self):
        #funcion get para abrir la pagina
        self.driver.get(data.urban_routes_url)
        #crear un objeto para inicializar la clase
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        #funcion para escribir en el campo desde y hasta
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    #2. Seleccionar la tarifa confort
    def test_choose_rate(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_button_pedir_taxi()
        routes_page.click_comfort_rate()
        assert routes_page.extraer_texto_confort_rate() == "Comfort"

    #3. Rellenar el numero de telefono
    def test_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_phone_number()
        phone_number = data.phone_number
        routes_page.click_phone_number_field()
        routes_page.write_phone_number(phone_number)
        assert routes_page.get_phone() == phone_number

    #4. Agregar una tarjeta de crédito
    def test_add_credit_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_next_button()
        code = retrieve_phone_code(self.driver)
        routes_page.set_code(code)
        routes_page.confirm_code()
        routes_page.click_metodo_pago()
        routes_page.click_add_card()
        routes_page.wait_for_add_card_section()
        routes_page.add_card(data.card_number, data.card_code)
        routes_page.close_payment_modal()
        assert routes_page.get_card() == data.card_number
        assert routes_page.get_cvv() == data.card_code

    #5.  Escribir un mensaje para el conductor
    def test_driver_message(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_message_to_driver(data.message_for_driver)
        assert routes_page.get_text() == data.message_for_driver

    #6. Pedir una manta y pañuelos
    def test_blanket_tissues(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_blanket()
        assert routes_page.get_checked_unchecket()



    #7. Pedir 2 helados
    def test_two_icecreams(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_ice(2)
        assert routes_page.get_dos_nieves() == 2


    #8. Aparece el modal para buscar un taxi
    def test_taxi_modal(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_smart_button()
        routes_page.wait_order_taxi_popup()#esta función VALIDA que aparece el popup



    #9.Esperar a que aparezca la información del conductor en el modal
    def test_wait_for_modal(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.wait_for_driver_assignment()
        final_text = routes_page.get_driver_info_text()
        assert "conductor" in final_text.lower()



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
