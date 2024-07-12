import os
import datetime
from app import create_app, db
from app.models import Book

def seed_books():
    books = [
        {
            'title': 'The Catcher in the Rye',
            'author': 'J.D. Salinger',
            'published_date': datetime.date(1951, 7, 16)
        },
        {
            'title': 'To Kill a Mockingbird',
            'author': 'Harper Lee',
            'published_date': datetime.date(1960, 7, 11)
        },
        {
            'title': '1984',
            'author': 'George Orwell',
            'published_date': datetime.date(1949, 6, 8)
        },
        {
            'title': 'Pride and Prejudice',
            'author': 'Jane Austen',
            'published_date': datetime.date(1813, 1, 28)
        },
        {
            'title': 'The Great Gatsby',
            'author': 'F. Scott Fitzgerald',
            'published_date': datetime.date(1925, 4, 10)
        }
    ]

    for book in books:
        new_book = Book(
            title=book['title'],
            author=book['author'],
            published_date=book['published_date']
        )
        db.session.add(new_book)

    db.session.commit()
    print("Books have been seeded successfully.")

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        seed_books()
