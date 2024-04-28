'''A Flask/WSGI application that will create and modify text files.'''
import os
import logging
from json import load, dump, dumps
from flask import Flask, render_template, send_from_directory, request, Response
from flask_cors import CORS
from scoreboard.update_endpoint import update_file, get_value
from scoreboard.util import *

def create_app():
    logging.info('loading config.json')
    config = {}
    try:
        with open("config.json", 'r+', encoding="utf-8") as config_file:
            config = load(config_file)
            config_file.close()
    except Exception:
        logging.warning('Error while loading config. Instantiating default config.')
        with open("sampleconfig.json", encoding="utf-8") as sample_file:
            config = load(sample_file)
            sample_file.close()
        with open('config.json', 'w+', encoding="utf-8") as outfile:
            dump(config, outfile)
            outfile.close()

    if 'root' not in config:
        logging.warning('No root directory defined in config. Please specify a root directory, otherwise the local directory will be used.')
        config["root"] = 'example'

    if not os.path.exists(config['root']):
        logging.warning('The specified root directory did not exist. Creating one.')
        os.makedirs(config['root'])

    logging.info('Gathering initial values')
    for file in config["files"]:
        file["value"] = get_value(config["root"], file)
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

    @app.route('/update/<file_name>/<new_value>')
    def update(file_name, new_value):
        for file in config["files"]:
            if file["name"] == file_name:
                response = update_file(config["root"], file, new_value)
                return response, 200
        return "not found.", 400

    @app.route('/update', methods =['POST'])
    def update_multiline():
        for variable in request.form:
            for file in config["files"]:
                if file["name"] == variable:
                    update_file(config["root"], file, request.form[variable])
                    sort_config(config)
        return render_template("index.html", config=config), 200

    @app.route('/add', methods=["POST"])
    def add_file():
        file_name = format_filename(request.form["name"])
        file_path = format_filename(request.form["name"]) + ".txt"
        file_type = request.form["type"]
        label = request.form["name"]
        file = {
            'name': file_name,
            'label': label,
            'path': file_path,
            'type': file_type,
            'order': len(config["files"])
        }
        config["files"].append(file)
        sort_config(config)
        return render_template("index.html", config=config), 201

    @app.route('/movedown/<file_name>')
    def move_down(file_name):
        for file in config['files']:
            if file['name'] == file_name:
                if file['order'] >= len(config['files']) - 1:
                    return render_template('index.html', config=config), 400
                update_order(config, file['order'], file['order']+1)
                return render_template('index.html', config=config), 200

        return render_template('index.html', config=config), 200

    @app.route('/moveup/<file_name>')
    def move_up(file_name):
        for file in config['files']:
            if file['name'] == file_name:
                if file['order'] <= 0:
                    return render_template('index.html', config=config), 400
                update_order(config, file['order'], file['order']-1)
                return render_template('index.html', config=config), 200
        return render_template('index.html', config=config), 200


    @app.route('/<file_name>')
    def get(file_name):
        for file in config["files"]:
            if file["name"] == file_name:
                response = get_value(config["root"], file)
                return response, 200
        return "not found.", 400

    @app.route('/delete/<file_name>', methods=["GET"])
    def delete(file_name):
        for file in config["files"]:
            if file["name"] == file_name:
                config["files"].remove(file)
        return render_template("index.html", config=config), 200

    @app.route('/save')
    def save_config():
        with open('config.json', 'w+', encoding="utf-8") as file:
            dump(config, file)
            file.close()
        return "", 200

    @app.route('/download', methods=["GET"])
    def download_config():
        config_copy = config.copy()
        config_copy['root'] = ''
        return Response(dumps(config_copy, indent=1),
            mimetype='application/json',
            headers={'Content-Disposition':'attachment;filename=config.json'})

    @app.route('/details', methods=["POST"])
    def update_details():
        data = request.get_json()
        for index, file in enumerate(config['files']):
            if file['name'] == data['name']:
                file['name'] = data['newName']
                file['label'] = data['label']
                file['path'] = data['path']
                config['files'][index] = file
                save_config()

        return render_template("index.html", config=config), 200

    @app.route('/scoreboard', methods=["GET"])
    def scoreboard():
        return render_template('scoreboard.html', config=config), 400

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'),
                                'favicon.ico', mimetype='image/vnd.microsoft.icon')

    return app
