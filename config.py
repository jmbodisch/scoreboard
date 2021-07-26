"""Flask configuration."""
class Config(object):
    SECRET_KEY="asdfasdasdffasdf"

class ProductionConfig(Config):
    SECRET_KEY="bigbadprodboi"
    DEBUG = False
    TESTING = False

class TestConfig(Config):
    TESTING = True
    DEBUG = False

class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    SCORE_A=r"C:\Users\boing\Documents\Splatoon\OBS\Thembo IHOP\score1.txt"
    SCORE_B=r"C:\Users\boing\Documents\Splatoon\OBS\Thembo IHOP\score2.txt"
    TEAM_A=r"C:\Users\boing\Documents\Splatoon\OBS\Thembo IHOP\team1.txt"
    TEAM_B=r"C:\Users\boing\Documents\Splatoon\OBS\Thembo IHOP\team2.txt"