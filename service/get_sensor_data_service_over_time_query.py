try:
    from flask import jsonify,request
    from model.device_model import devices_schema, Device
    from datetime import datetime
    print("Modules imported succssfully")
except Exception as e:
    print("Some modules are missing.")
    print(e)

def get_sensor_data_over_time_query():
    try:
        # Creating a dictionary from the arguments
        args = request.args
        args_dict = args.to_dict()

        from_time = datetime.strptime(args_dict['from'],'%Y%m%d%H%M%S%f')
        to_time = datetime.strptime(args_dict['to'],'%Y%m%d%H%M%S%f')
        sensor_id = str(args_dict['name'])

        # Check if the sensor ID is for temperature
        if Device.query.filter_by(temperature_sensor_id = sensor_id).first() is not None:
            
            temperature_sensor_obj = Device.query.filter_by(temperature_sensor_id = sensor_id).order_by(Device.reported_at.desc()).first()
            
            if temperature_sensor_obj:
                # If data exists for the given parameters
                sensor_data = Device.query.filter(Device.temperature_sensor_id == sensor_id and Device.reported_at.between(from_time,to_time)).all()
                sensor_data_result = devices_schema.dump(sensor_data)

                # Building the output
                final_out = []
                
                for i in sensor_data_result:
                    
                    sensor_dict = {}
                    sensor_dict['temperature_sensor_id'] = i['temperature_sensor_id']
                    sensor_dict['temperature_sensor_value'] = i['temperature_sensor_value']
                    sensor_dict['reported_at'] = i['reported_at']
                    final_out.append(sensor_dict)
                
                return jsonify({"sensor_data":final_out}),200
            else:
                return jsonify({"message":f"No data found for {sensor_id} within {from_time} and {to_time}"}),404

        # Check if the sensor ID is for pressure
        elif Device.query.filter_by(pressure_sensor_id = sensor_id).first() is not None:
            
            pressure_sensor_obj = Device.query.filter_by(pressure_sensor_id = sensor_id).order_by(Device.reported_at.desc()).first()
            
            if pressure_sensor_obj:
                # If data exists for the given parameters
    
                sensor_data = Device.query.filter(Device.pressure_sensor_id == sensor_id and Device.reported_at.between(from_time,to_time)).all()
                sensor_data_result = devices_schema.dump(sensor_data)
            
                # Building the output
                final_out = []
                
                for i in sensor_data_result:
                    
                    sensor_dict = {}
                    sensor_dict['pressure_sensor_id'] = i['pressure_sensor_id']
                    sensor_dict['pressure_sensor_value'] = i['pressure_sensor_value']
                    sensor_dict['reported_at'] = i['reported_at']
                    final_out.append(sensor_dict)
                
                return jsonify({"sensor_data":final_out}),200
            else:
                return jsonify({"message":f"No data found for {sensor_id} within {from_time} and {to_time}"}),404
        else:
            return jsonify({"_message":f"sensor with ID {sensor_id} does not exists"}),404
    except KeyError as keyerr:
        return jsonify({"error":"Missing details. Please provide name, from and to values in paramters"}),400
    except Exception as e:
        return jsonify({"error":f"{e}"}),400
