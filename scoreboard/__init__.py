import os
from json import load
from flask import Flask, render_template, send_from_directory
from scoreboard.updateEndpoint import updateFile, getValue

def create_app(test_config=None):

    configFile = open("config.json")
    config = load(configFile)
    configFile.close()

    app = Flask(__name__)

    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'scoreboard.sqlite')
    )

    app.config.from_object('config.DevelopmentConfig')

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return render_template("index.html", config=config)

    @app.route('/update/<fileName>/<newValue>')
    def update(fileName, newValue):
        for file in config["files"]:
            if file["name"] == fileName:
                response = updateFile(file, newValue)
                return response
        return "not found."

    @app.route('/<fileName>')
    def get(fileName):
        for file in config["files"]:
            if file["name"] == fileName:
                response = getValue(file)
                return response
        return "not found."


    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'),
                                'favicon.ico', mimetype='image/vnd.microsoft.icon')

    return app