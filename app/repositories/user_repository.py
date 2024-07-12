from app.models.user import User
from app.models.genre import Genre
from app import db

class UserRepository:
    @staticmethod
    def get_all():
        return User.query.all()

    @staticmethod
    def get_by_id(user_id):
        return User.query.get_or_404(user_id)

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def create(user_data):
        new_user = User(
            name=user_data['name'],
            email=user_data['email']
        )
        if 'preferences' in user_data:
            genres = Genre.query.filter(Genre.id.in_(user_data['preferences'])).all()
            new_user.preferences.extend(genres)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def update(user_id, user_data):
        user = User.query.get_or_404(user_id)
        user.name = user_data['name']
        user.email = user_data['email']
        if 'preferences' in user_data:
            user.preferences = Genre.query.filter(Genre.id.in_(user_data['preferences'])).all()
        db.session.commit()
        return user

    @staticmethod
    def delete(user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
