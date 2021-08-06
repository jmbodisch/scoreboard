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