
# IOT API

A simple IOT API which can:

    - register users
    - allow users to login
    - allow users to apply for loan using JWT
    - allow users to create device using JWT
    - allow users to update device name
    - allow users to send data to a sensor, API automatically inserts new record for each sensor data updates
    - allow users to get sensor data for a given time window which is queryable 


### Requirements

You will need Python and virtualenv module installed. Remaning will be installed via requriements.txt.

### Install

Clone the repo, create a virtualenv and install the requirements:

```
git clone https://github.com/AmitBanikOfficial/iot-api.git
cd iot-api
virtualenv iotapienv
for Windows:
iotapienv\Scripts\activate
for linux/mac:
source iotapienv/bin/activate
pip install -r requirements
```

### Run 

```
for Windows:
python app.py
for linux/mac:
python3 app.py
```

### Routes

```
http://127.0.0.1:5000/register
http://127.0.0.1:5000/login
http://127.0.0.1:5000/create_device
http://127.0.0.1:5000/send_data_to_sensor
http://127.0.0.1:5000/update_device_name
http://127.0.0.1:5000/get_sensor_data_over_time_query
```

### API

#### Register User

```
http://127.0.0.1:5000/register
```
Method  - POST

Accepts - username(str), password(str) - in form of JSON

Returns - JSON

Username length validation:
![Register](screenshots/01username_length_validation.png)

Username type validation:
![Register](screenshots/02username_should_be_only_alphanumeric.png)

Password length validation:
![Register](screenshots/03password_length_validation.png)

Password type validation:
![Register](screenshots/04password_cannot_have_space.png)

Username already taken validation:
![Register](screenshots/05username_is_already_taken.png)


Registering a normal user with missing details:
![Register](screenshots/06register_normal_user_with_missing_details.png)

Registering a user with proper details:
![Register](screenshots/07register_user_with_proper_details.png)

After successfull registration, User table looks like:

![Register](screenshots/08user_data_in_table_after_successful_registration.png)


#### Login User

```
http://127.0.0.1:5000/login
```

Method  - POST 

Accepts - username(str), password(str) in form of JSON

Returns - JSON, if successfull then with Access Token

If the user does not exist in the database:
![Login](screenshots/09login_user_does_not_exist.png)

If user provides incorrect password:
![Login](screenshots/10login_user_with_incorrect_password.png)

Successfull user login:
![Login](screenshots/11login_success.png)



#### Create Device

```
http://127.0.0.1:5000/create_device
```

Method  - POST 

Accepts - device_name(str) in form of JSON, requires access token as Authorization

Returns - JSON, with device name, unique device id, unique temperature sensor id, default temperature sensor value as 0.0 (float),unique pressure sensor id, default pressure sensor value as 0.0 (float), reported at - datetimestamp upto milliseconds

Create device:
![Create](screenshots/12create_device.png)

Create device with missing information:
![Create](screenshots/13create_device_with_incorrect_information.png)


Device data in database after successfull addition:
![Create](screenshots/14create_device_success_db.png)


#### Send data to a sensor

```
http://127.0.0.1:5000/send_data_to_sensor
```

Method  - PUT 

Accepts - sensor_id(str), sensor_value(float) in form of JSON, requires access token as Authorization

Returns - JSON


Sending data with exisitng sensor id:
![Send](screenshots/15send_data_success.png)

Database details after sending data with exisitng sensor id:
![Send](screenshots/16send_data_success_db_details.png)

Sending data with non-exisitng sensor id:
![Send](screenshots/17send_data_nonexist_sensor.png)


#### Update device name

```
http://127.0.0.1:5000/update_device_name
```

Method  - PUT 

Accepts - old_device_name(str), new_device_name(str) in form of JSON, requires access token as Authorization

Returns - JSON

Update existing device name:
![Update](screenshots/18update_existing_device_name.png)

Update non-existing device name:
![Update](screenshots/19update_non_existing_device_name.png)

Database after updating exisitng device:
![Update](screenshots/20update_existing_device_database.png)


#### Get sensor data over time

```
http://127.0.0.1:5000/get_sensor_data_over_time_query
```

Method  - GET 

Accepts - name(str), from(str) and to(str) in form of parameter, requires access token as Authorization

Returns - JSON

Get data for existing sensor over a period of time:
![Time](screenshots/21get_data_existing_device.png)

Get data for non existing sensor over a period of time:
![Time](screenshots/22get_data_non_existing_device.png)


## Run Unit tests

```
cd iot-api
python test_app.py
```



















