try:
    from flask import Blueprint
    from service.get_sensor_data_service_over_time_query import get_sensor_data_over_time_query
    from flask_jwt_extended import jwt_required
    print("Modules imported succssfully")
except Exception as e:
    print("Some modules are missing.")
    print(e)


get_sensor_data_over_time_query_bp = Blueprint('get_sensor_data_over_time_query_bp',__name__)

@get_sensor_data_over_time_query_bp.route("/get_sensor_data_over_time_query",methods = ['GET'])
@jwt_required()
def get_data_over_time():
        return get_sensor_data_over_time_query()
    