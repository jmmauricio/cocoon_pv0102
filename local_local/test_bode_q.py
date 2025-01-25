
import json
import numpy as np
import time

# api_ip = '127.0.0.1'
# api_port = 8200
# api_client = http.client.HTTPConnection(api_ip, api_port, timeout=2)

api_headers = {'Content-type': 'application/json'}

import requests

url = 'http://127.0.0.1:8200/setpoints'

x = requests.post(url, headers=api_headers, json = {"record":True})

for freq in np.arange(0.1,1.5,0.1):
    x = requests.post(url, headers=api_headers, json = {"Q_POI_sin_ref_amplitude":0.1,"Q_POI_sin_ref_hz":freq})
    time.sleep(20.0)
    x = requests.post(url, headers=api_headers, json = {"Q_POI_sin_ref_amplitude":0.0,"Q_POI_sin_ref_hz":0.0})
    time.sleep(5.0)
x = requests.post(url, headers=api_headers, json = {"record":False})
x = requests.post(url, headers=api_headers, json = {"stop_ppc":True})

# def set_setpoints(setpoints_dict):
#     ppc_setpoints_json = json.dumps(setpoints_dict)  # Convert dictionary to JSON format
#     print(ppc_setpoints_json)

#     api_client.request('POST', '/setpoints', ppc_setpoints_json, api_headers)     # Send POST request
#     response = api_client.getresponse() # Get response from server
#     response_string = response.read().decode()   
#     print(response_string)

# set_setpoints({"record":False})
# set_setpoints({"Q_POI_sin_ref_amplitude":0.0,"Q_POI_sin_ref_hz":0.5})
# time.sleep(2.0)

# print('Test running')
# set_setpoints({"record":True})
# time.sleep(1.0)

# set_setpoints({"Q_POI_sin_ref_amplitude":0.1,"Q_POI_sin_ref_hz":0.5})
# print('Sin wave applied running')
# time.sleep(10.0)

# set_setpoints({"Q_POI_sin_ref_amplitude":0.1,"Q_POI_sin_ref_hz":0.5})
# print('Sin wave applied running')
# time.sleep(10.0)

# # set_setpoints({"record":False})
# # print('Stop recording')

