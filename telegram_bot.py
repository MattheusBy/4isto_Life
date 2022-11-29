import telegram
from flask import request


def send_to_telegram():
    data = request.form.to_dict()
    request.files["photo"].save("uploaded_image/imageToSave.jpg")
    CHAT_ID = '-815155782'
    TOKEN = "5661560876:AAERwxrmUbxPBmvD54-Ootboe_cbclyva1s"
    message = "От {0}\n Телефон {1}. \n Населенный пункт: {2}. \n Изделие: {3} в количестве {4}.\n Запах мочи: {5} \n Сушка: {6} \n Чистка подушек: {7}".format(
        data['name'],
        data['phone'],
        data['city'],
        data['item'],
        data['count'],
        data['urine'],
        data['drying'],
        data['pillows'], )
    bot = telegram.Bot(token=TOKEN)
    bot.send_photo(chat_id=CHAT_ID, photo=open('uploaded_image/imageToSave.jpg', 'rb'))
    bot.send_message(chat_id=CHAT_ID, text=message)
