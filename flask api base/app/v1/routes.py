from app.v1.controllers import get_service_info
from flask import Blueprint

v1_bp = Blueprint('v1', __name__)

# Register all routes
v1_bp.route('/service', methods=['GET'])(get_service_info)
