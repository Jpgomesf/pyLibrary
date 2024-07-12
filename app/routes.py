from app.controllers.book_controller import register_book_routes
from app.controllers.user_controller import register_user_routes
from app.controllers.genre_controller import register_genre_routes
from app.controllers.version_controller import register_version_routes

def register_routes(app):
    register_version_routes(app)
    
    api_v1 = '/api/v1'
    register_book_routes(app, prefix=api_v1)
    register_user_routes(app, prefix=api_v1)
    register_genre_routes(app, prefix=api_v1)
