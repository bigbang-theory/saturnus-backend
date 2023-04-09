class GenerateData():
    from faker import Faker
    
    global fake
    fake = Faker()

    # generate data user acak menggunakan library faker
    def generate_user():
        return {
            'user_id': fake.uuid4(),
            'username': fake.user_name(),
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'address': [GenerateData.generate_address() for i in range(3)],
            'role_id': {
                'role_id': 'User',
                'name': 'user 1',
            }
        }

    # generate data address acak menggunakan library faker
    def generate_address():
        return {
            'address_id': fake.uuid4(),
            'name': fake.name(),
            'phone': fake.phone_number(),
            'address': fake.address(),
            'city': fake.city(),
            'state': fake.state(),
            'country': fake.country(),
            'post_code': fake.zipcode(),
        }

from flask import Blueprint, request, jsonify
import requests

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/', methods=['GET'])
def get_users():
    total = request.args.get('total', 5)
    users = [GenerateData.generate_user() for i in range(int(total))]
    return jsonify({
        'error': None,
        'data': users,
    })

@user_blueprint.route('/', methods=['POST'])
def index():
    users = request.form['username']
    print(users)
    return {
        'user': users
    }