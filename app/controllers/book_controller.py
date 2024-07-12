from flask import request, jsonify
from app.services.book_service import BookService

def register_book_routes(app):
    @app.route('/books', methods=['POST'])
    def add_book():
        data = request.get_json()
        new_book = BookService.create_book(data)
        return jsonify({'message': 'Book added successfully', 'book': new_book}), 201

    @app.route('/books', methods=['GET'])
    def get_books():
        books = BookService.get_all_books()
        return jsonify([{'id': book.id, 'title': book.title, 'author': book.author, 'published_date': book.published_date} for book in books]), 200

    @app.route('/books/<int:id>', methods=['GET'])
    def get_book(id):
        book = BookService.get_book_by_id(id)
        return jsonify({'id': book.id, 'title': book.title, 'author': book.author, 'published_date': book.published_date}), 200

    @app.route('/books/<int:id>', methods=['PUT'])
    def update_book(id):
        data = request.get_json()
        updated_book = BookService.update_book(id, data)
        return jsonify({'message': 'Book updated successfully', 'book': updated_book}), 200

    @app.route('/books/<int:id>', methods=['DELETE'])
    def delete_book(id):
        BookService.delete_book(id)
        return jsonify({'message': 'Book deleted successfully'}), 200
