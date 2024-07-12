from app.repositories.book_repository import BookRepository

class BookService:
    @staticmethod
    def get_all_books():
        return BookRepository.get_all()

    @staticmethod
    def get_book_by_id(book_id):
        return BookRepository.get_by_id(book_id)

    @staticmethod
    def create_book(book_data):
        return BookRepository.create(book_data)

    @staticmethod
    def update_book(book_id, book_data):
        return BookRepository.update(book_id, book_data)

    @staticmethod
    def delete_book(book_id):
        return BookRepository.delete(book_id)

    @staticmethod
    def get_books_by_genre(genre_id):
        return BookRepository.get_by_genre(genre_id)
