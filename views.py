from flask import Flask, render_template, request

from telegram_bot import send_to_telegram

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process')
def process():
    return render_template('process.html')


@app.route('/prices')
def prices():
    return render_template('prices.html')


@app.route('/get_price', methods=['post', 'get'])
def get_price():
    if request.method == 'POST':
        send_to_telegram()
        return render_template('done.html')
    if request.method == 'GET':
        return render_template('get_price.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/calendar')
def calendar():
    return render_template("calendar.html")


@app.route('/order')
def order():
    return render_template("order.html")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
