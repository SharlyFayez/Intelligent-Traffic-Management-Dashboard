import requests
import random
import time

API_URL = "http://localhost:8000/traffic"

while True:
    traffic_count = random.randint(1, 50)

    try:
        response = requests.post(API_URL, params={"count": traffic_count})
        print(f"Sent: {traffic_count}, Status: {response.status_code}")
    except Exception as e:
        print("Error:", e)

    time.sleep(1)
