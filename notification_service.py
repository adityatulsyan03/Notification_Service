from flask import Flask, request, jsonify, render_template
from datetime import datetime
import uuid

app = Flask(__name__)
notifications = {}

@app.route('/notifications', methods=['POST'])
def create_notification():
    data = request.get_json()
    if not data or 'user_id' not in data or 'type' not in data or 'message' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    
    if data['type'] not in ['email', 'sms', 'in_app']:
        return jsonify({'error': 'Invalid notification type'}), 400
    
    timestamp = datetime.now().isoformat()
    notification_id = str(uuid.uuid4())
    notification = {
        'id': notification_id,
        'user_id': data['user_id'],
        'type': data['type'],
        'message': data['message'],
        'timestamp': timestamp,
        'target': data.get('target')
    }
    
    if data['user_id'] not in notifications:
        notifications[data['user_id']] = []
    notifications[data['user_id']].append(notification)
    
    return jsonify({'status': 'success', 'timestamp': timestamp}), 201

@app.route('/users/<user_id>/notifications', methods=['GET'])
def get_user_all_notifications(user_id):
    user_notifications = notifications.get(user_id, [])
    return jsonify(user_notifications)

@app.route('/users/<user_id>/<id>/notifications', methods=['GET'])
def get_user_notifications(user_id,id):
    user_notifications = notifications.get(user_id, [])
    notification = next((n for n in user_notifications if n['id'] == id), None)
    if notification:
        return jsonify(notification)
    return jsonify({'error': 'Notification not found'}), 404

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)