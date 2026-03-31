from datetime import datetime

class Workflow:
    def __init__(self, name, org_id):
        self.name = name
        self.org_id = org_id
        self.created_at = datetime.utcnow()
        self.is_active = True

    def to_dict(self):
        return {
            'name': self.name,
            'org_id': self.org_id,
            'created_at': self.created_at,
            'is_active': self.is_active
        }

class WorkflowStage:
    def __init__(self, name, workflow_id, order):
        self.name = name
        self.workflow_id = workflow_id
        self.order = order
        self.created_at = datetime.utcnow()

    def to_dict(self):
        return {
            'name': self.name,
            'workflow_id': self.workflow_id,
            'order': self.order,
            'created_at': self.created_at
        }