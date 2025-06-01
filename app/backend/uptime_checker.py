# uptime_checker.py
import requests

url = 'http://localhost:5000/health'

try:
    response = requests.get(url, timeout=3)
    if response.status_code == 200:
        print("✅ Service is UP")
    else:
        print(f"⚠️ Service returned status: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"❌ Service DOWN. Error: {e}")
