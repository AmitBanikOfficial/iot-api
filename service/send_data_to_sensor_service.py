try:
    from flask import request,jsonify
    from model.device_model import Device
    from extensions import db
    from datetime import datetime
    print("Modules imported succssfully")
except Exception as e:
    print("Some modules are missing.")
    print(e)


def send_data_to_sensor():
    try:
        sensor_id = request.json['sensor_id']
        sensor_value = float(request.json['sensor_value'])

        # Check if the provided sensor ID is of temperature sensor type
        if Device.query.filter_by(temperature_sensor_id = sensor_id).first() is not None:
            
            # Creating an object of that sensor ID
            temperature_sensor_obj = Device.query.filter_by(temperature_sensor_id = sensor_id).order_by(Device.reported_at.desc()).first()
            
            # Getting details of that sensor ID
            device_id = temperature_sensor_obj.device_id
            device_name = temperature_sensor_obj.device_name
            temperature_sensor_value = sensor_value
            pressure_sensor_id = temperature_sensor_obj.pressure_sensor_id
            pressure_sensor_value = temperature_sensor_obj.pressure_sensor_value

            # Creating a new entry of that sensor ID with updated sensor value
            device = Device(device_id = str(device_id), device_name = device_name, temperature_sensor_id = str(sensor_id),temperature_sensor_value = temperature_sensor_value,pressure_sensor_id = str(pressure_sensor_id),pressure_sensor_value = pressure_sensor_value,reported_at=datetime.now())
            db.session.add(device)
            db.session.commit()
            return jsonify({'_message': "Data updated"}), 201

        # Check if the provided sensor id is of pressure sensor type
        elif Device.query.filter_by(pressure_sensor_id = sensor_id).first() is not None:
            
            # Creating an object of that sensor ID
            pressure_sensor_obj = Device.query.filter_by(pressure_sensor_id = sensor_id).order_by(Device.reported_at.desc()).first()

            # Getting details of that sensor ID
            device_id = pressure_sensor_obj.device_id
            device_name = pressure_sensor_obj.device_name
            pressure_sensor_value = sensor_value
            temperature_sensor_id = pressure_sensor_obj.temperature_sensor_id
            temperature_sensor_value = pressure_sensor_obj.temperature_sensor_value

            # Creating a new entry of that sensor ID with updated sensor value
            device = Device(device_id = str(device_id), device_name = device_name, temperature_sensor_id = temperature_sensor_id,temperature_sensor_value = temperature_sensor_value,pressure_sensor_id = str(sensor_id),pressure_sensor_value = sensor_value,reported_at=datetime.now())
            db.session.add(device)
            db.session.commit()
            return jsonify({'_message': "Data updated"}), 201
        else:
            return jsonify({"_message":f"sensor with ID {sensor_id} does not exists"}),404
    except KeyError as keyerr:
        return jsonify({"error":"Missing details. Please provide sensor_id and sensor_value"}),400
    except Exception as e:
        return jsonify({"error":f"{e}"}),400