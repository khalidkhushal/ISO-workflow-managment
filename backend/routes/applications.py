from flask import Blueprint, request, jsonify
from bson import ObjectId
from datetime import datetime
from utils.database import db
from models.application import Application, ApplicationStageHistory

bp = Blueprint('applications', __name__, url_prefix='/api/applications')

@bp.route('/', methods=['POST'])
def create_application():
    data = request.get_json()

    application = Application(
        org_id=data['org_id'],
        workflow_id=data['workflow_id']
    )

    result = db.get_collection('applications').insert_one(application.to_dict())
    application_id = str(result.inserted_id)

    # Get first stage of the workflow
    first_stage = db.get_collection('workflow_stages').find_one({
        'workflow_id': data['workflow_id']
    }, sort=[('order', 1)])

    if first_stage:
        # Create initial stage history
        history = ApplicationStageHistory(
            application_id=application_id,
            stage_id=str(first_stage['_id'])
        )
        db.get_collection('application_stage_history').insert_one(history.to_dict())

        # Update application with current stage
        db.get_collection('applications').update_one(
            {'_id': result.inserted_id},
            {'$set': {'current_stage_id': str(first_stage['_id'])}}
        )

    return jsonify({
        'id': application_id,
        'message': 'Application created successfully'
    }), 201

@bp.route('/', methods=['GET'])
def get_applications():
    org_id = request.args.get('org_id')
    workflow_id = request.args.get('workflow_id')

    query = {}
    if org_id:
        query['org_id'] = org_id
    if workflow_id:
        query['workflow_id'] = workflow_id

    applications = list(db.get_collection('applications').find(query))

    for app in applications:
        app['_id'] = str(app['_id'])

    return jsonify(applications)

@bp.route('/<application_id>/advance', methods=['POST'])
def advance_application(application_id):
    data = request.get_json()

    # Get current application
    application = db.get_collection('applications').find_one({
        '_id': ObjectId(application_id)
    })

    if not application:
        return jsonify({'error': 'Application not found'}), 404

    # Get current stage
    current_stage = db.get_collection('workflow_stages').find_one({
        '_id': ObjectId(application['current_stage_id'])
    })

    if not current_stage:
        return jsonify({'error': 'Current stage not found'}), 404

    # Get next stage
    next_stage = db.get_collection('workflow_stages').find_one({
        'workflow_id': application['workflow_id'],
        'order': current_stage['order'] + 1
    })

    if not next_stage:
        return jsonify({'error': 'No next stage available'}), 400

    # Mark current stage as exited
    db.get_collection('application_stage_history').update_one(
        {
            'application_id': application_id,
            'stage_id': application['current_stage_id'],
            'exited_at': None
        },
        {'$set': {'exited_at': datetime.utcnow()}}
    )

    # Create new stage history entry
    history = ApplicationStageHistory(
        application_id=application_id,
        stage_id=str(next_stage['_id']),
        status=data.get('status', 'entered')
    )
    db.get_collection('application_stage_history').insert_one(history.to_dict())

    # Update application with new current stage
    db.get_collection('applications').update_one(
        {'_id': ObjectId(application_id)},
        {'$set': {'current_stage_id': str(next_stage['_id'])}}
    )

    return jsonify({'message': 'Application advanced to next stage'})

@bp.route('/<application_id>/history', methods=['GET'])
def get_application_history(application_id):
    history = list(db.get_collection('application_stage_history').find({
        'application_id': application_id
    }).sort('entered_at', 1))

    for entry in history:
        entry['_id'] = str(entry['_id'])

    return jsonify(history)