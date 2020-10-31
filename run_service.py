from flask import Flask, render_template

from config import Config

# create the application
app: Flask = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def index():
    """Route to render the HTML"""
    return render_template("index.html")


# start the API service
if __name__ == '__main__':
    app.run(host=Config.HOST, port=Config.PORT)