"""Flask configuration."""
class Config(object):
    SECRET_KEY="asdfasdasdffasdf"

class TestConfig(Config):
    TESTING = True
    DEBUG = False

class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True