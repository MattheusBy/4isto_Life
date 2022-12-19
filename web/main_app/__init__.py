"""
This package creates Flask-application and sets configuration.
It contains view-fuctions for renders templates ant its url-routes
"""

import os
from flask import Flask, render_template, request
from web.main_app.telegram_bot import send_to_telegram


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        # view-function for index-page
        return render_template('index.html')

    @app.route('/process')
    def process():
        # views-function for process-page
        return render_template('process.html')

    @app.route('/prices')
    def prices():
        # views-function for prices-page
        return render_template('prices.html')

    @app.route('/get_price', methods=['post', 'get'])
    def get_price():
        # views-function for get_price-page
        if request.method == 'POST':
            send_to_telegram()
            return render_template('request_send.html')
        if request.method == 'GET':
            return render_template('get_price.html')

    @app.route('/contacts')
    def contacts():
        # views-function for contacts_page
        return render_template('contacts.html')

    @app.route('/calendar')
    def calendar():
        # views-function for calendar-page
        return render_template("calendar.html")

    @app.route('/order')
    def order():
        # views-function for order-page
        return render_template("order.html")

    @app.errorhandler(404)
    def invalid_route(e):
        return render_template("404.html")

    @app.errorhandler(500)
    def invalid_route(e):
        return render_template("500.html")

    return app
