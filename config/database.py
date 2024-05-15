"""config/database.py"""

from flask_sqlalchemy import SQLAlchemy

class Config:
    """Database Configuration"""
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://Anas:alx0723@localhost/ThootTrack'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
