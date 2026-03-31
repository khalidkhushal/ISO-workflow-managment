from flask import Blueprint, request, jsonify
from bson import ObjectId
from utils.database import db
from models.organization import Organization

bp = Blueprint('organizations', __name__, url_prefix='/api/organizations')

@bp.route('/', methods=['POST'])
def create_organization():
    data = request.get_json()

    organization = Organization(
        name=data['name']
    )

    result = db.get_collection('organizations').insert_one(organization.to_dict())

    return jsonify({
        'id': str(result.inserted_id),
        'message': 'Organization created successfully'
    }), 201

@bp.route('/', methods=['GET'])
def get_organizations():
    organizations = list(db.get_collection('organizations').find({'is_active': True}))

    for org in organizations:
        org['_id'] = str(org['_id'])

    return jsonify(organizations)

@bp.route('/<organization_id>', methods=['GET'])
def get_organization(organization_id):
    organization = db.get_collection('organizations').find_one({
        '_id': ObjectId(organization_id),
        'is_active': True
    })

    if not organization:
        return jsonify({'error': 'Organization not found'}), 404

    organization['_id'] = str(organization['_id'])
    return jsonify(organization)

@bp.route('/<organization_id>', methods=['PUT'])
def update_organization(organization_id):
    data = request.get_json()

    result = db.get_collection('organizations').update_one(
        {'_id': ObjectId(organization_id)},
        {'$set': data}
    )

    if result.modified_count == 0:
        return jsonify({'error': 'Organization not found'}), 404

    return jsonify({'message': 'Organization updated successfully'})

@bp.route('/<organization_id>', methods=['DELETE'])
def delete_organization(organization_id):
    result = db.get_collection('organizations').update_one(
        {'_id': ObjectId(organization_id)},
        {'$set': {'is_active': False}}
    )

    if result.modified_count == 0:
        return jsonify({'error': 'Organization not found'}), 404

    return jsonify({'message': 'Organization deleted successfully'})