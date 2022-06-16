import os
import config
from app import app
import unittest
import json

my_server = 'http://127.0.0.1:5000'

if os.path.exists(config.db_file):
    os.remove(config.db_file)

class TestApp(unittest.TestCase):
            
    def test_01_register_normal_user_with_proper_details(self):
        self.client = app.test_client()
        item = {"username":"username5678","password":"username5678"}
        resp = self.client.post(f"{my_server}/register",data=json.dumps(item),headers={'Content-Type': 'application/json'})
        self.assertEqual(resp.status_code,201)


    def test_02_register_normal_user_with_same_username_details(self):
        self.client = app.test_client()
        item = {"username":"username5678","password":"username5678"}
        resp = self.client.post(f"{my_server}/register",data=json.dumps(item),headers={'Content-Type': 'application/json'})
        self.assertEqual(resp.status_code,409)


    def test_03_register_normal_user_with_missing_details(self):
        self.client = app.test_client()
        item = {"username":"username5678"}
        resp = self.client.post(f"{my_server}/register",data=json.dumps(item),headers={'Content-Type': 'application/json'})
        self.assertEqual(resp.status_code,400)
    

    def test_04_login_normal_user_with_proper_details(self):
        # Initiating client object  
        self.client = app.test_client()
        item = {"username":"username5678","password":"username5678"}
        result = self.client.post(f'{my_server}/login',data=json.dumps(item),headers={'Content-Type': 'application/json'})
        self.assertEqual(result.status_code,201)


    def test_05_login_normal_user_with_incorrect_details(self):
        # Initiating client object  
        self.client = app.test_client()
        item = {"username":"username5678","password":"username5688"}
        result = self.client.post(f'{my_server}/login',data=json.dumps(item),headers={'Content-Type': 'application/json'})
        self.assertEqual(result.status_code,401)


    def test_06_create_new_device_with_correct_details(self):
        self.client = app.test_client()
        item = {"username":"username5678","password":"username5678"}
        result = self.client.post(f'{my_server}/login',data=json.dumps(item),headers={'Content-Type': 'application/json'})
        data = json.loads(result.data)
        access_token = data['access']
        device_data = {'device_name':'amit'}
        create_device = self.client.post(f'{my_server}/create_device',data=json.dumps(device_data),headers={'Content-Type': 'application/json',"Authorization": f"Bearer {access_token}"})
        self.assertEqual(create_device.status_code,201)


    def test_07_create_new_device_with_incorrect_details(self):
        self.client = app.test_client()
        item = {"username":"username5678","password":"username5678"}
        result = self.client.post(f'{my_server}/login',data=json.dumps(item),headers={'Content-Type': 'application/json'})
        data = json.loads(result.data)
        access_token = data['access']
        device_data = {'device_nam':'amit'}
        create_device = self.client.post(f'{my_server}/create_device',data=json.dumps(device_data),headers={'Content-Type': 'application/json',"Authorization": f"Bearer {access_token}"})
        self.assertEqual(create_device.status_code,400)
        

    def test_08_create_new_device_with_same_details(self):
        self.client = app.test_client()
        item = {"username":"username5678","password":"username5678"}
        result = self.client.post(f'{my_server}/login',data=json.dumps(item),headers={'Content-Type': 'application/json'})
        data = json.loads(result.data)
        access_token = data['access']
        device_data = {'device_name':'amit'}
        create_device = self.client.post(f'{my_server}/create_device',data=json.dumps(device_data),headers={'Content-Type': 'application/json',"Authorization": f"Bearer {access_token}"})
        self.assertEqual(create_device.status_code,409)
        
    
    def test_09_send_data_to_sensor_with_proper_details(self):
        self.client = app.test_client()
        item = {"username":"username5678","password":"username5678"}
        result = self.client.post(f'{my_server}/login',data=json.dumps(item),headers={'Content-Type': 'application/json'})
        data = json.loads(result.data)
        access_token = data['access']
        device_data = {'device_name':'banik'}
        create_device = self.client.post(f'{my_server}/create_device',data=json.dumps(device_data),headers={'Content-Type': 'application/json',"Authorization": f"Bearer {access_token}"})
        create_device_data = json.loads(create_device.data)
        sensor_id = create_device_data['temperature_sensor_id']
        sensor_data = {'sensor_id':sensor_id,'sensor_value': 9.57}
        send_sensor_data = self.client.put(f'{my_server}/send_data_to_sensor',data=json.dumps(sensor_data),headers={'Content-Type': 'application/json',"Authorization": f"Bearer {access_token}"})
        self.assertEqual(send_sensor_data.status_code,201)
        

    def test_10_send_data_to_sensor_with_incorrect_details(self):
        self.client = app.test_client()
        item = {"username":"username5678","password":"username5678"}
        result = self.client.post(f'{my_server}/login',data=json.dumps(item),headers={'Content-Type': 'application/json'})
        data = json.loads(result.data)
        access_token = data['access']
        device_data = {'device_name':'abanik'}
        create_device = self.client.post(f'{my_server}/create_device',data=json.dumps(device_data),headers={'Content-Type': 'application/json',"Authorization": f"Bearer {access_token}"})
        create_device_data = json.loads(create_device.data)
        sensor_id = 'incorrect_id'
        sensor_data = {'sensor_id':sensor_id,'sensor_value': 9.57}
        send_sensor_data = self.client.put(f'{my_server}/send_data_to_sensor',data=json.dumps(sensor_data),headers={'Content-Type': 'application/json',"Authorization": f"Bearer {access_token}"})
        self.assertEqual(send_sensor_data.status_code,404)
        
        
    def test_11_update_device_name_with_correct_details(self):
        self.client = app.test_client()
        item = {"username":"username5678","password":"username5678"}
        result = self.client.post(f'{my_server}/login',data=json.dumps(item),headers={'Content-Type': 'application/json'})
        data = json.loads(result.data)
        access_token = data['access']
        rename_device_data = {'old_device_name':'banik','new_device_name':'something'}
        update_device_data = self.client.put(f'{my_server}/update_device_name',data=json.dumps(rename_device_data),headers={'Content-Type': 'application/json',"Authorization": f"Bearer {access_token}"})
        self.assertEqual(update_device_data.status_code,201)
        
    
    def test_12_update_device_name_with_incorrect_details(self):
        self.client = app.test_client()
        item = {"username":"username5678","password":"username5678"}
        result = self.client.post(f'{my_server}/login',data=json.dumps(item),headers={'Content-Type': 'application/json'})
        data = json.loads(result.data)
        access_token = data['access']
        rename_device_data = {'old_device_name':'asdadbanik','new_device_name':'something'}
        update_device_data = self.client.put(f'{my_server}/update_device_name',data=json.dumps(rename_device_data),headers={'Content-Type': 'application/json',"Authorization": f"Bearer {access_token}"})
        self.assertEqual(update_device_data.status_code,404)
        

    def test_13_get_sensor_data_with_correct_details(self):
        self.client = app.test_client()
        item = {"username":"username5678","password":"username5678"}
        result = self.client.post(f'{my_server}/login',data=json.dumps(item),headers={'Content-Type': 'application/json'})
        data = json.loads(result.data)
        access_token = data['access']
        device_data = {'device_name':'amitbanik'}
        create_device = self.client.post(f'{my_server}/create_device',data=json.dumps(device_data),headers={'Content-Type': 'application/json',"Authorization": f"Bearer {access_token}"})
        create_device_data = json.loads(create_device.data)
        sensor_id = create_device_data['temperature_sensor_id']
        sensor_query_data = f'?name={sensor_id}&from=20220611170000&to=20220619075959'
        get_sensor_data = self.client.get(f'{my_server}/get_sensor_data_over_time_query{sensor_query_data}',headers={'Content-Type': 'application/json',"Authorization": f"Bearer {access_token}"})
        self.assertEqual(get_sensor_data.status_code,200)


    def test_14_get_sensor_data_with_incorrect_details(self):
        self.client = app.test_client()
        item = {"username":"username5678","password":"username5678"}
        result = self.client.post(f'{my_server}/login',data=json.dumps(item),headers={'Content-Type': 'application/json'})
        data = json.loads(result.data)
        access_token = data['access']
        device_data = {'device_name':'amitbanik'}
        create_device = self.client.post(f'{my_server}/create_device',data=json.dumps(device_data),headers={'Content-Type': 'application/json',"Authorization": f"Bearer {access_token}"})
        create_device_data = json.loads(create_device.data)
        sensor_id = 'device_which_is_not_present'
        sensor_query_data = f'?name={sensor_id}&from=20220611170000&to=20220619075959'
        get_sensor_data = self.client.get(f'{my_server}/get_sensor_data_over_time_query{sensor_query_data}',headers={'Content-Type': 'application/json',"Authorization": f"Bearer {access_token}"})
        self.assertEqual(get_sensor_data.status_code,404)


if __name__ == "__main__":
    unittest.main()
