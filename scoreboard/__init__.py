import os
from json import load
from flask import Flask, render_template, send_from_directory, request, url_for
from scoreboard.updateEndpoint import updateFile, getValue

def create_app(test_config=None):

    configFile = open("config.json")
    config = load(configFile)
    configFile.close()

    for file in config["files"]:
        file["value"] = getValue(config["root"], file)
        print("hi" + file["value"])
        

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
                response = updateFile(config["root"], file, newValue)
                return response
        return "not found."

    @app.route('/update', methods =['POST'])
    def updateMultiline():
        for variable in request.form: 
            for file in config["files"]:
                if file["name"] == variable:
                    updateFile(config["root"], file, request.form[variable])
        return render_template("index.html", config=config)

    @app.route('/<fileName>')
    def get(fileName):
        for file in config["files"]:
            if file["name"] == fileName:
                response = getValue(config["root"], file)
                return response
        return "not found."


    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'),
                                'favicon.ico', mimetype='image/vnd.microsoft.icon')

    def populateInitialValues():
        for file in config["files"]:
            setattr(file, "value", getValue(config["root"], file))
    return app