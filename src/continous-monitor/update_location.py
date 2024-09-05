import requests 
import schedule  
import time

def get_users():
    response = requests.get("http://localhost:5000/api/users")  
    return response.json()

def fetch_latest_location(user):
    return {"latitude": 12.34, "longitude": 56.78}

def update_user_location(user_id, latest_location):
    url = f"http://localhost:5000/api/users/{user_id}/location"
    payload = {"latitude": latest_location["latitude"], "longitude": latest_location["longitude"]}
    response = requests.put(url, json=payload)
    if response.status_code == 200:
        print(f"Updated location for user {user_id}")
    else:
        print(f"Failed to update location for user {user_id}")

def update_all_user_locations():
    users = get_users()
    for user in users:
        latest_location = fetch_latest_location(user)
        update_user_location(user['id'], latest_location)

schedule.every(5).minutes.do(update_all_user_locations)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
