from flask import jsonify


def get_service_info():
    return jsonify(
        {'status': True, 'data': {}, 'message': "Service info fetched."}
    )
