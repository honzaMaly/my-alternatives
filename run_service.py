#!/usr/bin/env python

"""Script to run API service"""
from flask import Flask, render_template
from werkzeug.middleware.proxy_fix import ProxyFix

from app.api import service_api
from config import Config

# create the application
app: Flask = Flask(__name__)
app.config.from_object(Config)
# lazy initialized of individual parts of the service
service_api.init_app(app)
# fix serving Swagger DOCs over "https"
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)


@app.route("/")
def index():
    """Route to render the HTML"""
    return render_template("index.html")


# start the API service
if __name__ == '__main__':
    app.run(host=Config.HOST, port=Config.PORT)
