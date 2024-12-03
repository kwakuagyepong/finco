from flask import Flask
from app.routes import authentication_blueprint
from app.auth_middleware import register_middleware
from app.db import mysql  # Import the MySQL instance

def create_app():
    app = Flask(__name__)

    # Configure MySQL
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'finco_ops_data_db'

    # Initialize MySQL
    mysql.init_app(app)

    app.secret_key = 'Alliswell@2024*'
    app.register_blueprint(authentication_blueprint)
    register_middleware(app)

    return app

app = create_app()
