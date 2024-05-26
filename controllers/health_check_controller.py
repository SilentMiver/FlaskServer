from flask import Blueprint, jsonify
import subprocess

health_bp = Blueprint('health_bp', __name__)

@health_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'Running'})
