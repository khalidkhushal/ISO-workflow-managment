from flask import Blueprint, request, jsonify
from bson import ObjectId
from utils.database import db
from models.workflow import Workflow, WorkflowStage

bp = Blueprint('workflows', __name__, url_prefix='/api/workflows')

@bp.route('/', methods=['POST'])
def create_workflow():
    data = request.get_json()

    workflow = Workflow(
        name=data['name'],
        org_id=data['org_id']
    )

    result = db.get_collection('workflows').insert_one(workflow.to_dict())

    return jsonify({
        'id': str(result.inserted_id),
        'message': 'Workflow created successfully'
    }), 201

@bp.route('/', methods=['GET'])
def get_workflows():
    org_id = request.args.get('org_id')

    query = {'is_active': True}
    if org_id:
        query['org_id'] = org_id

    workflows = list(db.get_collection('workflows').find(query))

    for workflow in workflows:
        workflow['_id'] = str(workflow['_id'])

    return jsonify(workflows)

@bp.route('/<workflow_id>/stages', methods=['POST'])
def add_workflow_stage(workflow_id):
    data = request.get_json()

    stage = WorkflowStage(
        name=data['name'],
        workflow_id=workflow_id,
        order=data['order']
    )

    result = db.get_collection('workflow_stages').insert_one(stage.to_dict())

    return jsonify({
        'id': str(result.inserted_id),
        'message': 'Workflow stage added successfully'
    }), 201

@bp.route('/<workflow_id>/stages', methods=['GET'])
def get_workflow_stages(workflow_id):
    stages = list(db.get_collection('workflow_stages').find({
        'workflow_id': workflow_id
    }).sort('order', 1))

    for stage in stages:
        stage['_id'] = str(stage['_id'])

    return jsonify(stages)