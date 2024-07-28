import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_urL', 'postgresql://postgres:password@127.0.0.1:5432/location-db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
