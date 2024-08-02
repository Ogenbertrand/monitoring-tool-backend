import os
import logging

class Config:
    # Fetch credentials from environment variables
    DB_USER = os.getenv('DB_USER', 'location-user')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5433')
    DB_NAME = os.getenv('DB_NAME', 'location-db')
    
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Log the database URI for debugging (excluding the password)
    logging.basicConfig(level=logging.DEBUG)
    logging.debug(f"SQLALCHEMY_DATABASE_URI: postgresql://{DB_USER}:*****@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Example usage in a Flask application
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
