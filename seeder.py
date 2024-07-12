import os
import datetime
from app import create_app, db
from app.models.genre import Genre
from app.models.book import Book

def seed_genres():
    genres = [
        {'name': 'Fiction'},
        {'name': 'Science Fiction'},
        {'name': 'Fantasy'},
        {'name': 'Non-Fiction'},
        {'name': 'Mystery'},
        {'name': 'Biography'}
    ]

    for genre_data in genres:
        genre = Genre(name=genre_data['name'])
        db.session.add(genre)
    db.session.commit()
    print("Genres have been seeded successfully.")

def seed_books():
    books = [
        {'title': 'Dune', 'author': 'Frank Herbert', 'published_date': datetime.date(1965, 8, 1), 'genre_name': 'Science Fiction'},
        {'title': '1984', 'author': 'George Orwell', 'published_date': datetime.date(1949, 6, 8), 'genre_name': 'Fiction'},
        {'title': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'published_date': datetime.date(1937, 9, 21), 'genre_name': 'Fantasy'},
        {'title': 'Sapiens', 'author': 'Yuval Noah Harari', 'published_date': datetime.date(2011, 9, 4), 'genre_name': 'Non-Fiction'},
        {'title': 'The Da Vinci Code', 'author': 'Dan Brown', 'published_date': datetime.date(2003, 3, 18), 'genre_name': 'Mystery'},
        {'title': 'The Diary of a Young Girl', 'author': 'Anne Frank', 'published_date': datetime.date(1947, 6, 25), 'genre_name': 'Biography'}
    ]

    for book_data in books:
        genre = Genre.query.filter_by(name=book_data['genre_name']).first()
        if genre:
            book = Book(
                title=book_data['title'],
                author=book_data['author'],
                published_date=book_data['published_date'],
                genre_id=genre.id
            )
            db.session.add(book)
    db.session.commit()
    print("Books have been seeded successfully.")

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        seed_genres()
        seed_books()
