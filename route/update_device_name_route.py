try:
    from flask import Blueprint
    from service.update_device_name_service import update_device_name
    from flask_jwt_extended import jwt_required
    print("Modules imported succssfully")
except Exception as e:
    print("Some modules are missing.")
    print(e)


update_device_name_bp = Blueprint('update_device_name_bp',__name__)


@update_device_name_bp.route("/update_device_name",methods = ['PUT'])
@jwt_required()
def device_name_update():
    return update_device_name()