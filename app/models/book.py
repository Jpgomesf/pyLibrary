from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    published_date = db.Column(db.Date, nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable=False)

    genre = db.relationship('Genre', backref=db.backref('books', lazy=True))

    def __init__(self, title, author, published_date, genre_id):
                self.title = title
                self.author = author
                self.published_date = published_date
                self.genre_id = genre_id

    def __repr__(self):
        return f'<Book {self.title}>'
