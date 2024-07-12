from app.models.genre import Genre
from app import db

class GenreRepository:
    @staticmethod
    def get_all():
        return Genre.query.all()

    @staticmethod
    def get_by_id(genre_id):
        return Genre.query.get_or_404(genre_id)

    @staticmethod
    def create(genre_data):
        new_genre = Genre(name=genre_data['name'])
        db.session.add(new_genre)
        db.session.commit()
        return new_genre

    @staticmethod
    def update(genre_id, genre_data):
        genre = Genre.query.get_or_404(genre_id)
        genre.name = genre_data['name']
        db.session.commit()
        return genre

    @staticmethod
    def delete(genre_id):
        genre = Genre.query.get_or_404(genre_id)
        db.session.delete(genre)
        db.session.commit()
