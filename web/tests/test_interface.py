from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()


def test_button_index():
    # test for link "Главная" in header
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.LINK_TEXT, "Главная").click()
    WebDriverWait(driver, 2)
    if 'Наши работы' not in driver.page_source:
        AssertionError("Not that page")
    if 'Применяем качественную химию' not in driver.page_source:
        AssertionError("Not that page")
    if 'В нашем штате работают опытные специалисты' not in driver.page_source:
        AssertionError("Not that page")


def test_button_prices():
    # test for link "Цены" in header
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.LINK_TEXT, "Цены").click()
    WebDriverWait(driver, 2)
    if 'Трехместный диван' not in driver.page_source:
        AssertionError("Not that page")
    if 'Нестандартный диван' not in driver.page_source:
        AssertionError("Not that page")
    if 'Большая подушка' not in driver.page_source:
        AssertionError("Not that page")


def test_button_process():
    # test for link "Процесс" in header
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.LINK_TEXT, "Процесс").click()
    WebDriverWait(driver, 2)
    if 'Процесс химчистки' not in driver.page_source:
        AssertionError("Not that page")
    if 'Чистка дивана' not in driver.page_source:
        AssertionError("Not that page")
    if 'Предварительная обработка' not in driver.page_source:
        AssertionError("Not that page")
    if 'static/img/process/process-3.jpg' not in driver.page_source:
        AssertionError("Not that page")



def test_button_order():
    # test for link "Как заказать" in header
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.LINK_TEXT, "Как заказать").click()
    WebDriverWait(driver, 2)
    if 'Как заказать' not in driver.page_source:
        AssertionError("Not that page")
    if 'static/img/order/order-2.png' not in driver.page_source:
        AssertionError("Not that page")
    if 'Вы получите письмо' not in driver.page_source:
        AssertionError("Not that page")



def test_button_calendar():
    # test for link "Расписание чисток" in header
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.LINK_TEXT, "Расписание").click()
    WebDriverWait(driver, 2)
    if 'Расписание чисток' not in driver.page_source:
        AssertionError("Not that page")
    if 'https://calendar.google.com/calendar' not in driver.page_source:
        AssertionError("Not that page")
    if 'Здесь Вы можете ознакомиться' not in driver.page_source:
        AssertionError("Not that page")


def test_button_contacts():
    # test for link "Контакты" in header
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.LINK_TEXT, "Контакты").click()
    WebDriverWait(driver, 2)
    if 'Наши контакты' not in driver.page_source:
        AssertionError("Not that page")
    if 'www.instagram.com/4istolife_gomel/' not in driver.page_source:
        AssertionError("Not that page")
    if 'ru-ru.facebook.com' not in driver.page_source:
        AssertionError("Not that page")


def test_button_get_price():
    # test for link "Узнать цену" in header
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.LINK_TEXT, "Узнать цену").click()
    WebDriverWait(driver, 2)
    if 'Получить цену' not in driver.page_source:
        AssertionError("Not that page")
    if 'Ваш населенный пункт' not in driver.page_source:
        AssertionError("Not that page")
    if 'Запах/пятна мочи' not in driver.page_source:
        AssertionError("Not that page")


def test_form_get_price():
    # test form for send data to
    # telegram on page "get_price"
    driver.get("http://127.0.0.1:5000/get_price")
    driver.find_element(By.NAME, "name").send_keys('Ivan')
    driver.find_element(By.NAME, "phone").send_keys("+375291111111")
    driver.find_element(By.NAME, "city").send_keys("1")
    driver.find_element(By.NAME, "photo").send_keys(
        "/home/matvey/projects/4istoLIFE/web/tests/img_for_test.jpg"
        )
    # above string required absolute path to image for uplaod it
    driver.find_element(By.NAME, "urine").send_keys("нет")
    driver.find_element(By.NAME, "drying").send_keys("нет")
    driver.find_element(By.NAME, "pillows").send_keys("нет")
    driver.find_element(By.NAME, "send_form_button").click()
    WebDriverWait(driver, 2)
    if 'Ожидайте' not in driver.page_source:
        AssertionError("Not that page")
    if 'SMS' not in driver.page_source:
        AssertionError("Not that page")