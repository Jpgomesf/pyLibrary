from flask import request, jsonify
from app.services.user_service import UserService

def register_user_routes(app):
    @app.route('/users', methods=['POST'])
    def add_user():
        data = request.get_json()
        try:
            new_user = UserService.create_user(data)
            return jsonify({'message': 'User added successfully', 'user': {'id': new_user.id, 'name': new_user.name, 'email': new_user.email, 'preferences': [genre.id for genre in new_user.preferences]}}), 201
        except ValueError as e:
            return jsonify({'error': str(e)}), 400

    @app.route('/users', methods=['GET'])
    def get_users():
        users = UserService.get_all_users()
        return jsonify([{'id': user.id, 'name': user.name, 'email': user.email, 'preferences': [genre.id for genre in user.preferences]} for user in users]), 200

    @app.route('/users/<int:id>', methods=['GET'])
    def get_user(id):
        user = UserService.get_user_by_id(id)
        return jsonify({'id': user.id, 'name': user.name, 'email': user.email, 'preferences': [genre.id for genre in user.preferences]}), 200

    @app.route('/users/<int:id>', methods=['PUT'])
    def update_user(id):
        data = request.get_json()
        updated_user = UserService.update_user(id, data)
        return jsonify({'message': 'User updated successfully', 'user': {'id': updated_user.id, 'name': updated_user.name, 'email': updated_user.email, 'preferences': [genre.id for genre in updated_user.preferences]}}), 200

    @app.route('/users/<int:id>', methods=['DELETE'])
    def delete_user(id):
        UserService.delete_user(id)
        return jsonify({'message': 'User deleted successfully'}), 200
