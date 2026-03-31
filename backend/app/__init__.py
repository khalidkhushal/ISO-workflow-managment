from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os

def create_app():
    app = Flask(__name__)

    load_dotenv()

    app.config['MONGO_URI'] = os.getenv('MONGO_URI', 'mongodb://localhost:27017/iso_workflow')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')

    CORS(app)

    from routes import organizations, users, workflows, applications
    app.register_blueprint(organizations.bp)
    app.register_blueprint(users.bp)
    app.register_blueprint(workflows.bp)
    app.register_blueprint(applications.bp)

    return app