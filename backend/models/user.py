from datetime import datetime
import bcrypt

class User:
    def __init__(self, email, password, full_name):
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.full_name = full_name
        self.created_at = datetime.utcnow()
        self.organizations = []
        self.is_active = True
        self.role = 'user'

    def to_dict(self):
        return {
            'email': self.email,
            'password': self.password,
            'full_name': self.full_name,
            'created_at': self.created_at,
            'organizations': self.organizations,
            'is_active': self.is_active,
            'role': self.role
        }

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))