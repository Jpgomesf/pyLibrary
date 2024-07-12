from app.controllers.book_controller import register_book_routes
from app.controllers.user_controller import register_user_routes
from app.controllers.genre_controller import register_genre_routes

def register_routes(app):
    register_book_routes(app)
    register_user_routes(app)
    register_genre_routes(app)
