class Config(object):
    DEBUG = False
    TESTING = False
    # Common config settings like SECRET_KEY, DATABASE_URI, etc.

class DevelopmentConfig(Config):
    DEBUG = True
    # Development-specific settings

class ProductionConfig(Config):
    DEBUG = False
    # Production-specific settings
