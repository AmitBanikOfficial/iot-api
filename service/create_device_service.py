try:
    from flask import request,jsonify
    from model.device_model import Device
    from extensions import db
    from datetime import datetime
    import uuid
    print("Modules imported succssfully")
except Exception as e:
    print("Some modules are missing.")
    print(e)


# Function to create new device
def create_new_device():
    try:
        # Getting the data
        device_name = request.json['device_name']
        if Device.query.filter_by(device_name=device_name).first() is not None:
            return jsonify({'error': "Device name is already taken"}), 409
        
        # Assigning unique IDs to device and sensors
        device_id = uuid.uuid4()
        temperature_sensor_id = uuid.uuid4()
        pressure_sensor_id = uuid.uuid4()
        
        # Setting default value for the sensor
        temperature_sensor_value = 0.0
        pressure_sensor_value = 0.0

        # Inserting New device into Database
        device = Device(device_id = str(device_id), device_name = device_name, temperature_sensor_id = str(temperature_sensor_id),temperature_sensor_value = temperature_sensor_value,pressure_sensor_id = str(pressure_sensor_id),pressure_sensor_value = pressure_sensor_value,reported_at=datetime.now())
        db.session.add(device)
        db.session.commit()
        return jsonify({"_message":"Device added successfully",
                        "device_name":device_name,
                        "device_id":device.device_id,
                        "temperature_sensor_id" : device.temperature_sensor_id,
                        "temperature_sensor_value" : device.temperature_sensor_value,
                        "pressure_sensor_id" : device.pressure_sensor_id,
                        "pressure_sensor_value" : device.pressure_sensor_value,
                        "reported_at" : device.reported_at}),201
    except KeyError as key_err:
        return jsonify({"error":"Please provide device name"}),400
    except Exception as e:
        return jsonify({"error":f"{e}"}),400