import requests
import json

BASE_URL = "http://127.0.0.1:5000"

def test_health():
    print("Testing health endpoint...")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")

def test_diabetes():
    print("Testing diabetes prediction...")
    payload = {"features": [1, 85, 66, 29, 0, 26.6, 0.351, 31]}
    response = requests.post(f"{BASE_URL}/predict/diabetes", json=payload)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")

def test_heart():
    print("Testing heart disease prediction...")
    payload = {"features": [45, 1, 3, 120, 200, 0, 1, 150, 0, 1.0, 2, 0, 2]}
    response = requests.post(f"{BASE_URL}/predict/heart", json=payload)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")

def test_parkinsons():
    print("Testing parkinsons prediction...")
    payload = {"features": [197.076, 206.896, 192.055, 0.00289, 0.00001, 0.00166, 0.00168, 0.00498, 0.01098, 0.097, 0.00563, 0.0068, 0.00802, 0.01689, 0.00339, 26.775, 0.422229, 0.741367, -7.3483, 0.177551, 1.743867, 0.085569]}
    response = requests.post(f"{BASE_URL}/predict/parkinsons", json=payload)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")

if __name__ == "__main__":
    try:
        test_health()
        test_diabetes()
        test_heart()
        test_parkinsons()
        print("All tests completed successfully!")
    except Exception as e:
        print(f"Error: {e}")
