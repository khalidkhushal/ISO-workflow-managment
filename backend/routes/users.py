from flask import Blueprint, request, jsonify
from bson import ObjectId
from utils.database import db
from models.user import User

bp = Blueprint('users', __name__, url_prefix='/api/users')

@bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()

    existing_user = db.get_collection('users').find_one({'email': data['email']})
    if existing_user:
        return jsonify({'error': 'User already exists'}), 400

    user = User(
        email=data['email'],
        password=data['password'],
        full_name=data['full_name']
    )

    result = db.get_collection('users').insert_one(user.to_dict())

    return jsonify({
        'id': str(result.inserted_id),
        'message': 'User registered successfully'
    }), 201

@bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()

    user = db.get_collection('users').find_one({'email': data['email']})
    if not user:
        return jsonify({'error': 'Invalid credentials'}), 401

    user_obj = User(user['email'], '', user['full_name'])
    user_obj.password = user['password']

    if not user_obj.check_password(data['password']):
        return jsonify({'error': 'Invalid credentials'}), 401

    return jsonify({
        'id': str(user['_id']),
        'email': user['email'],
        'full_name': user['full_name'],
        'message': 'Login successful'
    })

@bp.route('/', methods=['GET'])
def get_users():
    users = list(db.get_collection('users').find({'is_active': True}))

    for user in users:
        user['_id'] = str(user['_id'])
        del user['password']

    return jsonify(users)

@bp.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    user = db.get_collection('users').find_one({
        '_id': ObjectId(user_id),
        'is_active': True
    })

    if not user:
        return jsonify({'error': 'User not found'}), 404

    user['_id'] = str(user['_id'])
    del user['password']
    return jsonify(user)