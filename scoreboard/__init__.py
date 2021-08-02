import os
from flask import Flask, render_template, send_from_directory
from updateEndpoint import updateFile


def create_app(test_config=None):

    configFile = open("config.json")
    config = json.load(configFile)
    configFile.close()

    app = Flask(__name__, instance_relative_config=False)

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
    def hello():
        return render_template("index.html")

    @app.route('/update/<fileName>/<newValue>')
    def updateFile(fileName, newValue):
        for file in config["files"]:
            if file["name"] == fileName:
                updateFile(file, newValue)
        return

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'),
                                'favicon.ico', mimetype='image/vnd.microsoft.icon')

    @app.route('/scoreA')
    def scoreAincrement():
        scorefile = open(app.config["SCORE_A"], 'r+')
        score = scorefile.read()
        print(f"retrieved value: {score}")
        try:
            score = int(score)
        except:
            score = 0
        score += 1
        scorefile.seek(0)
        scorefile.write(str(score))
        scorefile.truncate()
        scorefile.close()
        return str(score)
    
    @app.route('/scoreA/<int:newScore>')
    def scoreASet(newScore):
        scorefile = open(app.config["SCORE_A"], 'r+')
        score = scorefile.read()
        print(f"retrieved value: {score}")
        score = newScore
        scorefile.seek(0)
        scorefile.write(str(score))
        scorefile.truncate()
        scorefile.close()
        return str(score)

    @app.route('/scoreB')
    def scoreBincrement():
        scorefile = open(app.config["SCORE_B"], 'r+')
        score = scorefile.read()
        print(f"retrieved value: {score}")
        try:
            score = int(score)
        except:
            score = 0
        score += 1
        scorefile.seek(0)
        scorefile.write(str(score))
        scorefile.truncate()
        scorefile.close()
        return str(score)

    @app.route('/scoreB/<int:newScore>')
    def scoreBSet(newScore):
        scorefile = open(app.config["SCORE_B"], 'r+')
        score = scorefile.read()
        print(f"retrieved value: {score}")
        score = newScore
        scorefile.seek(0)
        scorefile.write(str(score))
        scorefile.truncate()
        scorefile.close()
        return str(score)

    @app.route('/teamA/<newName>')
    def teamA(newName):
        namefile = open(app.config["TEAM_A"], 'r+')
        name = namefile.read()
        print(f"retrieved value: {name}")
        name = newName
        namefile.seek(0)
        namefile.write(name)
        namefile.truncate()
        namefile.close()
        return name

    @app.route('/teamB/<newName>')
    def teamB(newName):
        namefile = open(app.config["TEAM_B"], 'r+')
        name = namefile.read()
        print(f"retrieved value: {name}")
        name = newName
        namefile.seek(0)
        namefile.write(name)
        namefile.truncate()
        namefile.close()
        return name

    return app