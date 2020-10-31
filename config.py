"""Configuration of variables for the DEMO."""
import os
from os import environ


class Config:
    """Set configuration."""
    SECRET_KEY = environ.get('SECRET_KEY', 'dev')  # set to DEV when value is missing
    FLASK_APP = environ.get('FLASK_APP', 'MY_ALTERNATIVES')
    PORT = int(os.environ.get("PORT", 5000))  # set to 5000 when value is missing
    HOST = os.environ.get("HOST", '0.0.0.0')  # set HOST to local when value is missing
