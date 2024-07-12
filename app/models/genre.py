from app import db

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    def __init__(self, name):
                self.name = name

    def __repr__(self):
        return f'<Genre {self.name}>'
