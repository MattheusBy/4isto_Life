"""
   Module retrieves data from url-page "get_price". After then, it sends data from user to telegram-bot
   Owner of app can get this information in his telegram-account associated with telegram-bot and can
   send back actual price to user use SMS.
"""

import telebot
from flask import request


def send_to_telegram():
    # extract data from user's request. Images saves locally
    data = request.form.to_dict()
    request.files["photo"].save("main_app/uploaded_image/imageToSave.jpeg")
    # CHAT_ID and TOKEN provides permissions to send data to owner's app
    CHAT_ID = '-815155782'
    TOKEN = "5661560876:AAERwxrmUbxPBmvD54-Ootboe_cbclyva1s"
    # Create message-body
    message = "От {0}\n Телефон {1}. \n Населенный пункт: {2}. \n Изделие: {3} в количестве {4}.\n Запах мочи: {5} \n Сушка: {6} \n Чистка подушек: {7}".format(
        data['name'],
        data['phone'],
        data['city'],
        data['item'],
        data['count'],
        data['urine'],
        data['drying'],
        data['pillows'],)
    # Create Telebot instance and send user's data
    bot = telebot.TeleBot(token=TOKEN)
    bot.send_photo(chat_id=CHAT_ID, photo=open("main_app/uploaded_image/imageToSave.jpeg", 'rb'))
    bot.send_message(chat_id=CHAT_ID, text=message)
