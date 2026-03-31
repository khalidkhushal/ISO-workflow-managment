from datetime import datetime

class Organization:
    def __init__(self, name):
        self.name = name
        self.created_at = datetime.utcnow()
        self.is_active = True

    def to_dict(self):
        return {
            'name': self.name,
            'created_at': self.created_at,
            'is_active': self.is_active
        }