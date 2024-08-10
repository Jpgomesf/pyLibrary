from flask import request, jsonify
from app.services.recommendation_service import RecommendationService

def register_translation_routes(app, prefix=''):
    @app.route(f'{prefix}/translation', methods=['POST'])
    def get_translation():
        data = request.get_json()
        prompt = data.get('prompt')
        lang = data.get('lang')
        if not prompt:
            return jsonify({'error': 'Prompt is required'}), 400
        
        translated_content = RecommendationService.get_translation(prompt, lang)
        print(translated_content)
        # translated_content = 'translated_content'

        return jsonify({
            'content': translated_content,
        }), 200
