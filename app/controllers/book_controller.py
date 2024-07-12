from flask import request, jsonify
from app.services.book_service import BookService

def register_book_routes(app):
    @app.route('/books', methods=['POST'])
    def add_book():
        data = request.get_json()
        new_book = BookService.create_book(data)
        return jsonify({
            'message': 'Book added successfully',
            'book': {
                'id': new_book.id,
                'title': new_book.title,
                'author': new_book.author,
                'published_date': new_book.published_date,
                'genre': new_book.genre.name,
                'genre_id': new_book.genre_id
            }
        }), 201

    @app.route('/books', methods=['GET'])
    def get_books():
        books = BookService.get_all_books()
        return jsonify([{
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'published_date': book.published_date,
            'genre': book.genre.name,
            'genre_id': book.genre_id
        } for book in books]), 200

    @app.route('/books/<int:id>', methods=['GET'])
    def get_book(id):
        book = BookService.get_book_by_id(id)
        return jsonify({
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'published_date': book.published_date,
            'genre': book.genre.name,
            'genre_id': book.genre_id
        }), 200

    @app.route('/books/<int:id>', methods=['PUT'])
    def update_book(id):
        data = request.get_json()
        updated_book = BookService.update_book(id, data)
        return jsonify({
            'message': 'Book updated successfully',
            'book': {
                'id': updated_book.id,
                'title': updated_book.title,
                'author': updated_book.author,
                'published_date': updated_book.published_date,
                'genre': updated_book.genre.name,
                'genre_id': updated_book.genre_id
            }
        }), 200

    @app.route('/books/<int:id>', methods=['DELETE'])
    def delete_book(id):
        BookService.delete_book(id)
        return jsonify({'message': 'Book deleted successfully'}), 200

    @app.route('/genres/<int:genre_id>/books', methods=['GET'])
    def get_books_by_genre(genre_id):
        books = BookService.get_books_by_genre(genre_id)
        return jsonify([{
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'published_date': book.published_date,
            'genre': book.genre.name,
            'genre_id': book.genre_id
        } for book in books]), 200
