try:
    from flask import Blueprint
    from service.send_data_to_sensor_service import send_data_to_sensor
    from flask_jwt_extended import jwt_required
    print("Modules imported succssfully")
except Exception as e:
    print("Some modules are missing.")
    print(e)

send_data_to_sensor_bp = Blueprint('send_data_to_sensor_bp',__name__)

@send_data_to_sensor_bp.route("/send_data_to_sensor",methods = ['PUT'])
@jwt_required()
def send_data():
    return send_data_to_sensor()
