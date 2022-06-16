try:
    from flask import Blueprint
    from service.create_device_service import create_new_device
    from flask_jwt_extended import jwt_required
    print("Modules imported succssfully")
except Exception as e:
    print("Some modules are missing.")
    print(e)

create_device_bp = Blueprint('create_device_bp',__name__)

@create_device_bp.route("/create_device",methods = ['POST'])
@jwt_required()
def create_device():
    return create_new_device()
