import os
from json import load, dump
import string
from flask import Flask, render_template, send_from_directory, request, Response
from flask_cors import CORS
from scoreboard.updateEndpoint import updateFile, getValue
from scoreboard.util import format_filename

def create_app(test_config=None):

    configFile = open("config.json")
    config = load(configFile)
    configFile.close()

    if not 'root' in config:
        config["root"] = ''

    for file in config["files"]:
        file["value"] = getValue(config["root"], file)
        print("hi" + file["value"])
        

    app = Flask(__name__)
    CORS(app)

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
                return response, 200
        return "not found.", 400

    @app.route('/update', methods =['POST'])
    def updateMultiline():
        for variable in request.form: 
            for file in config["files"]:
                if file["name"] == variable:
                    updateFile(config["root"], file, request.form[variable])
        return render_template("index.html", config=config), 200

    @app.route('/add', methods=["POST"])
    def addFile():
        fileName = format_filename(request.form["name"])
        filePath = format_filename(request.form["name"]) + ".txt"
        fileType = request.form["type"]
        label = request.form["name"]
        file = {
            'name': fileName,
            'label': label,
            'path': filePath,
            'type': fileType
        }
        config["files"].append(file)
        return render_template("index.html", config=config), 201

    @app.route('/<fileName>')
    def get(fileName):
        for file in config["files"]:
            if file["name"] == fileName:
                response = getValue(config["root"], file)
                return response, 200
        return "not found.", 400

    @app.route('/delete/<fileName>', methods=["GET"])
    def delete(fileName):
        for file in config["files"]:
            if file["name"] == fileName:
                config["files"].remove(file)
        return render_template("index.html", config=config), 200

    @app.route('/save')
    def saveConfig():
        file = open('config.json', 'w+')
        dump(config, file)
        file.close()
        return "", 200


    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'),
                                'favicon.ico', mimetype='image/vnd.microsoft.icon')

    def populateInitialValues():
        for file in config["files"]:
            setattr(file, "value", getValue(config["root"], file))
    return app