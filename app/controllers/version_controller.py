from flask import jsonify
from app.version import __version__

def register_version_routes(app):
    @app.route('/version', methods=['GET'])
    def get_version():
        return jsonify({'version': __version__}), 200
