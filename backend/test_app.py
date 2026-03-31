#!/usr/bin/env python3

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))

from app import create_app
from utils.database import db

def test_app_creation():
    """Test that the Flask app can be created successfully"""
    app = create_app()
    assert app is not None
    assert 'MONGO_URI' in app.config
    print("✅ Flask app creation test passed")

def test_database_connection():
    """Test database connection initialization"""
    app = create_app()
    db.init_app(app)
    assert db.client is not None
    assert db.db is not None
    print("✅ Database connection test passed")

def test_models():
    """Test that models can be instantiated"""
    from models.user import User
    from models.organization import Organization
    from models.workflow import Workflow, WorkflowStep

    user = User("test@example.com", "password123", "Test User")
    assert user.email == "test@example.com"
    assert user.check_password("password123")

    org = Organization("Test Org", "Test Description", "user123")
    assert org.name == "Test Org"

    workflow = Workflow("Test Workflow", "Test Description", "org123", "user123")
    assert workflow.name == "Test Workflow"

    step = WorkflowStep("Test Step", "Test Description", "user123")
    assert step.name == "Test Step"

    print("✅ Models test passed")

if __name__ == "__main__":
    print("Running basic tests...")
    test_app_creation()
    test_database_connection()
    test_models()
    print("All basic tests passed!")