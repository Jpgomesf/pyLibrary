from app.models.book import Book
from app import db

class BookRepository:
    @staticmethod
    def get_all():
        return Book.query.all()

    @staticmethod
    def get_by_id(book_id):
        return Book.query.get_or_404(book_id)

    @staticmethod
    def create(book_data):
        new_book = Book(
            title=book_data['title'],
            author=book_data['author'],
            published_date=book_data['published_date'],
            genre_id=book_data['genre_id']
        )
        db.session.add(new_book)
        db.session.commit()
        return new_book

    @staticmethod
    def update(book_id, book_data):
        book = Book.query.get_or_404(book_id)
        book.title = book_data['title']
        book.author = book_data['author']
        book.published_date = book_data['published_date']
        book.genre_id = book_data['genre_id']
        db.session.commit()
        return book

    @staticmethod
    def delete(book_id):
        book = Book.query.get_or_404(book_id)
        db.session.delete(book)
        db.session.commit()

    @staticmethod
    def get_by_title_or_author(keyword):
        return Book.query.filter(
            (Book.title.ilike(f'%{keyword}%')) | 
            (Book.author.ilike(f'%{keyword}%'))
        ).all()

    @staticmethod
    def get_by_genre(genre_id):
        return Book.query.filter_by(genre_id=genre_id).all()
