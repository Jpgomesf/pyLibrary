from flask import request, jsonify
from app.services.recommendation_service import RecommendationService

def register_recommendation_routes(app, prefix=''):
    @app.route(f'{prefix}/recommendations', methods=['POST'])
    def get_recommendations():
        data = request.get_json()
        prompt = data.get('prompt')
        if not prompt:
            return jsonify({'error': 'Prompt is required'}), 400

        recommended_books = RecommendationService.get_recommendations_from_llm(prompt)

        books_list = recommended_books.get("books", [])
        available_books, unavailable_books = RecommendationService.get_available_books(books_list)

        return jsonify({
            'available_books': available_books,
            'unavailable_books': unavailable_books
        }), 200
