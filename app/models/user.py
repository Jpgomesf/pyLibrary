from app import db

user_genre = db.Table('user_genre',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'), primary_key=True)
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    preferences = db.relationship('Genre', secondary=user_genre, lazy='subquery',
                                  backref=db.backref('users', lazy=True))

    def __repr__(self):
        return f'<User {self.name}>'
