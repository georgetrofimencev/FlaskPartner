from config.base.config import Config
from logging.config import dictConfig


class ProductionConfig(Config):
    """Production configuration."""
    HANDLING_PROTOCOL = "https"
    SERVER_NAME = '0.0.0.0:8888'
    DEBUG = False
    logger_conf = Config.LOGGING
    dictConfig(logger_conf)


class DevelopmentConfig(Config):
    """Development configuration."""
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_RECORD_QUERIES = True
    logger_conf = Config.LOGGING
    dictConfig(logger_conf)


class TestingConfig(Config):
    """Configuration for Testing"""
    TESTING = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_RECORD_QUERIES = True
    logger_conf = Config.LOGGING
    dictConfig(logger_conf)
