"""
   Module retrieves data from url-page "get_price".
   After then, it sends data from user to telegram-bot
   Owner of app can get this information
   in his telegram-account associated with telegram-bot and can
   send back actual price to user use SMS.
"""
import requests
from flask import request


def send_to_telegram():
    # extract data from user's request. Images saves locally
    data = request.form.to_dict()
    request.files["photo"].save("main_app/uploaded_image/imageToSave.jpeg")
    # CHAT_ID and TOKEN provides permissions to send data to owner's app
    CHAT_ID = '-1001599179085'
    TOKEN = "5661560876:AAERwxrmUbxPBmvD54-Ootboe_cbclyva1s"
    # Create message-body
    message = "От:{0}\n Телефон {1}. \n " \
              "Населенный пункт: {2}. \n " \
              "Изделие: {3} в количестве {4}.\n " \
              "Запах мочи: {5} " \
              "\n Сушка: {6} " \
              "\n Чистка подушек: {7}".format(
                data['name'],
                data['phone'],
                data['city'],
                data['item'],
                data['count'],
                data['urine'],
                data['drying'],
                data['pillows'], )
    url_text = "https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}".format(
        token=TOKEN, chat_id=CHAT_ID, message=message)
    url_photo = "https://api.telegram.org/bot{token}/sendPhoto?chat_id={chat_id}".format(
        token=TOKEN, chat_id=CHAT_ID)
    files = [
        ('photo',
         ('imageToSave.jpeg', open('main_app/uploaded_image/imageToSave.jpeg', 'rb'), 'image/jpeg'))
    ]
    payload = {}
    headers = {}

    response_photo = requests.request("POST", url_photo, headers=headers, files=files)
    response_text = requests.request("POST", url_text, headers=headers)
    if response_text and response_photo:
        return "Message has been send successful!!"
