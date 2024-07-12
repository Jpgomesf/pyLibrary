from app.repositories.user_repository import UserRepository

class UserService:
    @staticmethod
    def get_all_users():
        return UserRepository.get_all()

    @staticmethod
    def get_user_by_id(user_id):
        return UserRepository.get_by_id(user_id)

    @staticmethod
    def get_user_by_email(email):
        return UserRepository.get_by_email(email)

    @staticmethod
    def create_user(user_data):
        if UserRepository.get_by_email(user_data['email']):
            raise ValueError('Email already exists')
        return UserRepository.create(user_data)

    @staticmethod
    def update_user(user_id, user_data):
        return UserRepository.update(user_id, user_data)

    @staticmethod
    def delete_user(user_id):
        return UserRepository.delete(user_id)
