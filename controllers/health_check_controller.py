from flask import Blueprint, jsonify
import subprocess

health_bp = Blueprint('health_bp', __name__)

@health_bp.route('/health', methods=['GET'])
def health_check():
    service_name = "your-service-name"  # Замените на имя вашего сервиса
    try:
        result = subprocess.run(['systemctl', 'is-active', service_name], stdout=subprocess.PIPE, text=True)
        status = result.stdout.strip()
        if status == "active":
            return jsonify({'status': 'Running'})
        else:
            return jsonify({'status': 'Not Running'})
    except Exception as e:
        return jsonify({'status': 'Error', 'message': str(e)}), 500
