import requests
import datetime

URL = "https://eu4sxlx00006.corpnet2.com/v1/status"

def check_status():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        response = requests.get(URL, timeout=10)
        status_code = response.status_code
        
        print(f"[{timestamp}] Status Code: {status_code}")
        
        if status_code != 200:
            print("❌ ALERT: Service is DOWN or not returning 200!")
        else:
            print("✅ Service is UP")
    
    except Exception as e:
        print(f"❌ ERROR: Cannot reach URL — {e}")

if _name_ == "_main_":
    check_status()
[08:53, 10/02/2026] Suman: import requests
import datetime

URL = "https://eu4sxlx00006.corpnet2.com/v1/status"

def check_status():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        response = requests.get(URL, timeout=10)
        status_code = response.status_code
        
        print(f"[{timestamp}] Status Code: {status_code}")
        
        if status_code != 200:
            print("❌ ALERT: Service is DOWN or not returning 200!")
        else:
            print("✅ Service is UP")
    
    except Exception as e:
        print(f"❌ ERROR: Cannot reach URL — {e}")

if _name_ == "_main_":
    check_status()