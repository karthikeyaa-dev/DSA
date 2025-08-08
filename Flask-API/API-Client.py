import requests

BASE_URL='http://127.0.0.1:5000'

def create_user(name):
    payload={"name":name}
    response=requests.post(f"{BASE_URL}/users", json=payload)
    print(f"POST--->{response.status_code}")
    try:
        print("Response:", response.json())
    except requests.exceptions.JSONDecodeError:
        print("❌ Server did not return JSON.")

def get_user():
    response=requests.get(f"{BASE_URL}/users")
    print(f"GET--->{response.status_code}")
    try:
        print("Response:", response.json())
    except requests.exceptions.JSONDecodeError:
        print("❌ Server did not return JSON.")

if __name__=="__main__":
    create_user("Rohit")
    get_user()
