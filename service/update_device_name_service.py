try:
    from flask import jsonify,request
    from model.device_model import device_schema,devices_schema, Device
    from datetime import datetime
    from extensions import db
    print("Modules imported succssfully")
except Exception as e:
    print("Some modules are missing.")
    print(e)


def update_device_name():
    try:
        old_device_name = request.json['old_device_name']
        new_device_name = request.json['new_device_name']

        if Device.query.filter_by(device_name=old_device_name).first() is None:
            return jsonify({'error': f"Device name {old_device_name} does not exist"}), 404

        if Device.query.filter_by(device_name=new_device_name).first() is not None:
            return jsonify({'error': f"Device name {new_device_name} is already taken"}), 409
        
        Device.query.filter_by(device_name=old_device_name).update({"device_name":new_device_name})
        db.session.commit()
        
        return jsonify({"_message": f"device name updated from {old_device_name} to {new_device_name}"}),201
    except KeyError as keyerr:
        return jsonify({"error":"Missing details. Please provide old_device_name and new_device_name"}),400
    except Exception as e:
        return jsonify({"error":f"{e}"}),400