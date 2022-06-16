# importing required modules and libraries
try:
    from flask import Flask
    from config import db_path, secrete_key,jwt_access_expires
    from flask_jwt_extended import JWTManager
    from extensions import db,ma
    
    from route.register_user_route import register_bp
    from route.login_user_route import login_bp
    from route.create_device_route import create_device_bp
    from route.send_data_to_sensor_route import send_data_to_sensor_bp
    from route.get_sensor_data_over_time_query_route import get_sensor_data_over_time_query_bp
    from route.update_device_name_route import update_device_name_bp
    
    print("Modules imported succssfully")
except Exception as e:
    print("Some modules are missing.")
    print(e)

# Initiating app
app = Flask(__name__)

# Adding configurations
app.config['SQLALCHEMY_DATABASE_URI'] = db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
app.config['SECRET_KEY'] = secrete_key
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = jwt_access_expires

# To ensure the db is created before the 1st run
@app.before_first_request
def create_tables():
    db.create_all()


# Initiating jwt, sqlalchemy and marshmellow
jwt = JWTManager(app)
db.init_app(app)
ma.init_app(app)


# Registering the blueprints for which the routes were defined
app.register_blueprint(register_bp)
app.register_blueprint(login_bp)
app.register_blueprint(create_device_bp)
app.register_blueprint(send_data_to_sensor_bp)
app.register_blueprint(get_sensor_data_over_time_query_bp)
app.register_blueprint(update_device_name_bp)


if __name__ == '__main__':
    # To run in debug mode, or else use app.run()
    app.run(debug=True)
