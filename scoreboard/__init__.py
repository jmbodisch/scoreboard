import os
from json import load, dump, dumps
import string
from textwrap import indent
from flask import Flask, render_template, send_from_directory, request, Response, send_file
from flask_cors import CORS
from scoreboard.updateEndpoint import updateFile, getValue
from scoreboard.util import *
import logging

def create_app(test_config=None):
    logging.info('loading config.json')
    config = {}
    try:
        configFile = open("config.json", 'r+')
        config = load(configFile)
        configFile.close()
    except:
        logging.warning('Error while loading config. Instantiating default config.')
        sampleFile = open("sampleconfig.json")
        config = load(sampleFile)
        sampleFile.close()
        outfile = open('config.json', 'w+')
        dump(config, outfile)
        outfile.close()


    if not 'root' in config:
        logging.warning('No root directory defined in config. Please specify a root directory, otherwise the local directory will be used.')
        config["root"] = ''

    logging.info('Gathering initial values')
    for file in config["files"]:
        
        file["value"] = getValue(config["root"], file)
        logging.info(file["name"] + ": " + file["value"])
        

    app = Flask(__name__)
    CORS(app)
    
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
                    sort_config(config)
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
            'type': fileType,
            'order': len(config["files"])
        }
        config["files"].append(file)
        sort_config(config)
        return render_template("index.html", config=config), 201

    @app.route('/movedown/<fileName>')
    def moveDown(fileName):
        for file in config["files"]:
            if file["name"] == fileName:
                if file["order"] >= len(config["files"]) - 1:
                    return render_template("index.html", config=config), 400
                else:
                    update_order(config, file["order"], file["order"]+1)
                    return render_template("index.html", config=config), 200
        return render_template("index.html", config=config), 400

    @app.route('/moveup/<fileName>')
    def moveUp(fileName):
        for file in config["files"]:
            if file["name"] == fileName:
                if file["order"] <= 0:
                    return render_template("index.html", config=config), 400
                else:
                    update_order(config, file["order"], file["order"]-1)
                    return render_template("index.html", config=config), 200
        return render_template("index.html", config=config), 400


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

    @app.route('/download', methods=["GET"])
    def downloadConfig():
        configCopy = config.copy()
        configCopy['root'] = ''
        return Response(dumps(configCopy, indent=1),
            mimetype='application/json',
            headers={'Content-Disposition':'attachment;filename=config.json'})

    @app.route('/details', methods=["POST"])
    def updateDetails():
        data = request.get_json()
        for index, file in enumerate(config['files']):
            if file['name'] == data['name']:
                file['name'] = data['newName']
                file['label'] = data['label']
                file['path'] = data['path']
                config['files'][index] = file

        return render_template("index.html", config=config), 200

    @app.route('/scoreboard', methods=["GET"])
    def scoreboard():
        return render_template('scoreboard.html', config=config), 400

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'),
                                'favicon.ico', mimetype='image/vnd.microsoft.icon')

    def populateInitialValues():
        for file in config["files"]:
            setattr(file, "value", getValue(config["root"], file))
    return app