from datetime import datetime

class Application:
    def __init__(self, org_id, workflow_id, current_stage_id=None):
        self.org_id = org_id
        self.workflow_id = workflow_id
        self.current_stage_id = current_stage_id
        self.status = 'pending'
        self.created_at = datetime.utcnow()

    def to_dict(self):
        return {
            'org_id': self.org_id,
            'workflow_id': self.workflow_id,
            'current_stage_id': self.current_stage_id,
            'status': self.status,
            'created_at': self.created_at
        }

class ApplicationStageHistory:
    def __init__(self, application_id, stage_id, status='entered'):
        self.application_id = application_id
        self.stage_id = stage_id
        self.status = status
        self.entered_at = datetime.utcnow()
        self.exited_at = None

    def to_dict(self):
        return {
            'application_id': self.application_id,
            'stage_id': self.stage_id,
            'status': self.status,
            'entered_at': self.entered_at,
            'exited_at': self.exited_at
        }

    def mark_exited(self):
        self.exited_at = datetime.utcnow()