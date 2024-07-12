from flask import request, jsonify
from app.services.genre_service import GenreService

def register_genre_routes(app):
    @app.route('/genres', methods=['POST'])
    def add_genre():
        data = request.get_json()
        new_genre = GenreService.create_genre(data)
        return jsonify({'message': 'Genre added successfully', 'genre': {'id': new_genre.id, 'name': new_genre.name}}), 201

    @app.route('/genres', methods=['GET'])
    def get_genres():
        genres = GenreService.get_all_genres()
        return jsonify([{'id': genre.id, 'name': genre.name} for genre in genres]), 200

    @app.route('/genres/<int:id>', methods=['GET'])
    def get_genre(id):
        genre = GenreService.get_genre_by_id(id)
        return jsonify({'id': genre.id, 'name': genre.name}), 200

    @app.route('/genres/<int:id>', methods=['PUT'])
    def update_genre(id):
        data = request.get_json()
        updated_genre = GenreService.update_genre(id, data)
        return jsonify({'message': 'Genre updated successfully', 'genre': {'id': updated_genre.id, 'name': updated_genre.name}}), 200

    @app.route('/genres/<int:id>', methods=['DELETE'])
    def delete_genre(id):
        GenreService.delete_genre(id)
        return jsonify({'message': 'Genre deleted successfully'}), 200
