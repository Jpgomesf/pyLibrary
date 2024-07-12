from app.repositories.genre_repository import GenreRepository

class GenreService:
    @staticmethod
    def get_all_genres():
        return GenreRepository.get_all()

    @staticmethod
    def get_genre_by_id(genre_id):
        return GenreRepository.get_by_id(genre_id)

    @staticmethod
    def create_genre(genre_data):
        return GenreRepository.create(genre_data)

    @staticmethod
    def update_genre(genre_id, genre_data):
        return GenreRepository.update(genre_id, genre_data)

    @staticmethod
    def delete_genre(genre_id):
        return GenreRepository.delete(genre_id)
