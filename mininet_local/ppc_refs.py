
import requests
import json
import time

url = "http://10.10.0.4:8200/setpoints"
headers = {"Content-Type": "application/json"}

data = {
    "P_POI_ref": 0.5,
    "Q_POI_ref": 0.0,
    "Q_POI_sin_ref_amplitude": 0.0,
    "Q_POI_sin_ref_hz": 0.1
}
response = requests.post(url, headers=headers, data=json.dumps(data))
print('Getting steady state')
time.sleep(5)


data = {"record":True}
response = requests.post(url, headers=headers, data=json.dumps(data))
# Check the response
#print("Status Code:", response.status_code)
print("Response Text:", response.text)
print('Start recording')
time.sleep(1)

data = {
    "P_POI_ref": 0.5,
    "Q_POI_ref": 0.0,
    "Q_POI_sin_ref_amplitude": 0.0,
    "Q_POI_sin_ref_hz": 0.2
}
response = requests.post(url, headers=headers, data=json.dumps(data))

# Check the response
print('Reference change applied')
time.sleep(10)


data = {
    "record":False
}

# Send the POST request
response = requests.post(url, headers=headers, data=json.dumps(data))
print('Stop recording')
