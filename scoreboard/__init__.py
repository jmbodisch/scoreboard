import os
from flask import Flask


def create_app(test_config=None):
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
        return 'Hello, World!'

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

    @app.route('/teamA/<name>')
    def teamA():
        return 1
    return app