
try:
    from extensions import db,ma
    from sqlalchemy import Column, Integer, String, Float,DateTime
    from datetime import datetime
    print("Modules imported succssfully")
except Exception as e:
    print("Some modules are missing.")
    print(e)

# User database models
class Device(db.Model):
    __tablename__ = 'device'
    entry_number = Column(Integer,nullable = False, primary_key=True)
    device_id = Column(String, nullable = False)
    device_name = Column(String,nullable = False)
    temperature_sensor_id = Column(String, nullable = False)
    temperature_sensor_value = Column(Float, nullable = False,default = 0.0)
    pressure_sensor_id = Column(String, nullable = False)
    pressure_sensor_value = Column(Float, nullable = False, default = 0.0)
    reported_at = Column(DateTime,default=datetime.now())


class DeviceSchema(ma.Schema):
    class Meta:
        fields = ('entry_number','device_id','device_name','temperature_sensor_id','temperature_sensor_value','pressure_sensor_id','pressure_sensor_value','reported_at')


device_schema = DeviceSchema()
devices_schema = DeviceSchema(many=True)

