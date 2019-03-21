import os
import time
import logging

basedir = os.path.abspath(os.path.dirname(__file__))


class GMTFormatter(logging.Formatter):
    converter = time.gmtime


class Config:
    """Base configuration."""

    DEBUG = True
    TESTING = False
    SERVER_NAME = "127.0.0.1:8888"
    HANDLING_PROTOCOL = "http"
    BCRYPT_LOG_ROUNDS = 12
    SECRET_KEY = "UGp66j!JF^P@f_Em"

    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

    MAIL_PORT = 465
    MAIL_USERNAME = 't.partner@partner.betronic.online'
    MAIL_DEFAULT_SENDER = 't.partner@partner.betronic.online'
    MAIL_PASSWORD = 'xtkz,ft,f'

    ADMINS = ["george98trofimencev@gmail.com",
              "test.betronic.partner@mail.ru",
              't.partner@partner.betronic.online',
              ]

    DATABASE = {
        "host": "localhost",
        "port": 5431,
        "user": "postgres",
        "password": "postgres",
        "name": "dbetronic",
        "pool_size": 10,
    }
    DATABASE_URI = (
        "postgresql://%(user)s:%(password)s@" "%(host)s:%(port)s/%(name)s"
        % DATABASE
    )

    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "lines": {
                "format": "%(asctime)s [%(levelname)s] "
                          "%(pathname)s %(lineno)d %(message)s",
                "()": GMTFormatter,
            },
            "simple": {
                "format": "%(asctime)s [%(levelname)s] %(message)s",
                "()": GMTFormatter,
            },
        },
        "handlers": {
            "default": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "simple",
            },
            "debug": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "lines",
            },
        },
    }
