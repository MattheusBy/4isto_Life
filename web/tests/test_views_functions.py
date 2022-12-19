"""
Module contains tools for testing view-functions
"""

import requests
from main_app import create_app


def test_config():
    # create Flask-application instance for test
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_index(client):
    # sends request to index-page and checks response
    response = client.get('/')
    assert response.status_code==200
    assert b'get_price' in response.data
    assert b'src="static/img/works/item-6.jpg"' in response.data
    assert b'All rights reserved' in response.data
    assert bytes('Более 5 лет в сфере оказания услуг', encoding='utf-8') in response.data
    assert bytes('Как заказать', encoding='utf-8') in response.data
    assert bytes('Наши работы', encoding='utf-8') in response.data


def test_calendar(client):
    # sends request to calendar-page and checks response
    response = client.get('/calendar')
    assert response.status_code==200
    assert bytes('Расписание чисток', encoding = 'utf-8') in response.data
    assert b'<iframe src="https://calendar.google.com/calendar/' in response.data


def test_contacts(client):
    # sends request to contacts-page and checks response
    response = client.get('/contacts')
    assert response.status_code == 200
    assert bytes('Наши контакты', encoding='utf-8') in response.data
    assert b'https://www.instagram.com/4istolife_gomel/' in response.data
    assert b'https://ru-ru.facebook.com/' in response.data
def test_prices(client):
    # sends request to prices-page and checks response
    response = client.get('/prices')
    assert response.status_code==200
    assert b'src="static/img/sofas/divan-1.png"' in response.data
    assert b'35 BYN' in response.data
    assert bytes('Удаление запаха', encoding='utf-8') in response.data
    assert bytes('Внимание!', encoding='utf-8') in response.data


def test_process(client):
    # sends request to process-page and checks response
    response = client.get('/process')
    assert response.status_code==200
    assert b'src="static/img/process/process-0.jpg"' in response.data
    assert b'src="static/img/process/process-2.jpg"' in response.data
    assert bytes('Нейтрализация', encoding = 'utf-8') in response.data


def test_order(client):
    # sends request to order-page and checks response
    response = client.get('/order')
    assert response.status_code==200
    assert b'src="static/img/order/order-1.png"' in response.data
    assert b'src="static/img/order/order-2.png"' in response.data
    assert bytes('Как заказать', encoding = 'utf-8') in response.data
    assert bytes('Для осуществления заказа', encoding = 'utf-8') in response.data
    assert bytes('Сделайте фото Вашего изделия в хорошем качестве', encoding = 'utf-8') in response.data

def test_get_price(client):
    # sends request to get_price-page and checks response
    response = client.get('/get_price')
    assert response.status_code==200
    # send POST-request to localhost
    url = "http://127.0.0.1:5038/get_price"
    # dict with test data in POST-request
    payload_1 = {'name': 'Alex',
               'phone': '+375291111111',
               'city': 'Gomel',
               'item': 'Трехместный диван',
               'count': '1',
               'urine': 'нет',
               'drying': 'нет',
               'pillows': 'да'}
    # add image in POST-request
    files = [
        ('photo', ('img_for_test.jpg', open('tests/img_for_test.jpg', 'rb'), 'image/jpeg'))
    ]
    response = requests.request("POST", url, data=payload_1, files=files)
    assert response.status_code==200
    # dict with test data in POST-request
    payload_2 = {'name': 'Jim',
               'phone': '+3752912345678',
               'city': 'Gomel',
               'item': 'Кресло',
               'count': '4',
               'urine': 'нет',
               'drying': 'нет',
               'pillows': 'нет'}
    # add image in POST-request
    files = [
        ('photo', ('img_for_test.jpg', open('tests/img_for_test.jpg', 'rb'), 'image/jpeg'))
    ]
    response = requests.request("POST", url, data=payload_2, files=files)
    assert response.status_code == 200
    assert bytes('Ожидайте SMS', encoding='utf-8') in response.content
    assert bytes('15 минут', encoding='utf-8') in response.content

def test_request_send(client):
    # sends request to request_send_page and checks response. Direct request response is error 404
    response = client.get('/request_send')
    assert response.status_code==200
    assert b"url('static/img/errors_images/404_back.png')" in response.data


def test_error_handler_404(client):
    response = client.get('/some_text')
    assert response.status_code==200
    assert b"url('static/img/errors_images/404_back.png')" in response.data

