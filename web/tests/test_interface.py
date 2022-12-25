from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()


def test_button_index():
    # test for link "Главная" in header
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.LINK_TEXT, "Главная").click()
    WebDriverWait(driver, 2)
    assert 'Наши работы' in driver.page_source
    assert 'Применяем качественную химию со знаком качества' in driver.page_source
    assert 'В нашем штате работают опытные специалисты' in driver.page_source


def test_button_prices():
    # test for link "Цены" in header
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.LINK_TEXT, "Цены").click()
    WebDriverWait(driver, 2)
    assert 'Трехместный диван' in driver.page_source
    assert 'Нестандартный диван' in driver.page_source
    assert 'Большая подушка' in driver.page_source


def test_button_process():
    # test for link "Процесс" in header
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.LINK_TEXT, "Процесс").click()
    WebDriverWait(driver, 2)
    assert 'Процесс химчистки' in driver.page_source
    assert 'Чистка дивана - процесс многоступенчатый' in driver.page_source
    assert 'Предварительная обработка' in driver.page_source
    assert "static/img/process/process-3.jpg" in driver.page_source


def test_button_order():
    # test for link "Как заказать" in header
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.LINK_TEXT, "Как заказать").click()
    WebDriverWait(driver, 2)
    assert 'Как заказать' in driver.page_source
    assert 'static/img/order/order-2.png' in driver.page_source
    assert 'Вы получите письмо' in driver.page_source


def test_button_calendar():
    # test for link "Расписание чисток" in header
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.LINK_TEXT, "Расписание").click()
    WebDriverWait(driver, 2)
    assert 'Расписание чисток' in driver.page_source
    assert 'https://calendar.google.com/calendar' in driver.page_source
    assert 'Здесь Вы можете ознакомиться с расписанием чисток' in driver.page_source


def test_button_contacts():
    # test for link "Контакты" in header
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.LINK_TEXT, "Контакты").click()
    WebDriverWait(driver, 2)
    assert 'Наши контакты' in driver.page_source
    assert 'www.instagram.com/4istolife_gomel/' in driver.page_source
    assert 'ru-ru.facebook.com' in driver.page_source


def test_button_get_price():
    # test for link "Узнать цену" in header
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.LINK_TEXT, "Узнать цену").click()
    WebDriverWait(driver, 2)
    assert 'Получить цену' in driver.page_source
    assert 'Ваш населенный пункт' in driver.page_source
    assert 'Запах/пятна мочи' in driver.page_source


def test_form_get_price():
    # test form for send data to telegram on
    #page "get_price"
    driver.get("http://127.0.0.1:5000/get_price")
    driver.find_element(By.NAME, "name").send_keys('Ivan')
    driver.find_element(By.NAME, "phone").send_keys("+375291111111")
    driver.find_element(By.NAME, "city").send_keys("1")
    driver.find_element(By.NAME, "photo").send_keys("/home/matvey/projects/4istoLIFE/web/tests/img_for_test.jpg")
    # above string required absolute path to image for uplaod it
    driver.find_element(By.NAME, "urine").send_keys("нет")
    driver.find_element(By.NAME, "drying").send_keys("нет")
    driver.find_element(By.NAME, "pillows").send_keys("нет")
    driver.find_element(By.NAME, "send_form_button").click()
    WebDriverWait(driver, 2)
    assert 'Ожидайте' in driver.page_source
    assert 'Ожидайте SMS' in driver.page_source

