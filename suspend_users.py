import requests

# Constants
API_URL = 'https://api.atlassian.com/admin/v1/orgs/41911251-2ada-1555-68k5-a4j252k767a6/directory/users'
TOKEN = 'ATCTT3xFfGN0qiaMni9VlFUgoE_5Hcqi4g9BS2f7-OigcgEvD3IVA9UMsROvr-o4Dj85YnLO2giaYQi4B3LCvAwGFiDGvoeYyg90WfW5HIsRJ0IpEh_94lO-Q1Jo4ccRP4DDpPFxNzZuiGxeTM4m19X8cGPad3RD8XDj6lBBM6LCkNMk82eOrmg=64E8F293'
HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Accept': 'application/json'
}

def suspend_user(user_id):
    suspend_url = f"{API_URL}/{user_id}/suspend-access"
    response = requests.post(suspend_url, headers=HEADERS)

    if response.status_code == 204:
        print(f"User {user_id} suspended successfully.")
    elif response.status_code == 200:
        response_json = response.json()
        if "message" in response_json and "suspended" in response_json["message"].lower():
            print(f"User {user_id} suspended successfully.")
        else:
            print(f"Failed to suspend user {user_id}. Unexpected response content: {response.text}")
    else:
        print(f"Failed to suspend user {user_id}. Status code: {response.status_code}, Response: {response.text}")

def main():
    # Read user IDs from a text file (assuming each user ID is on a new line)
    with open('user_ids.txt', 'r') as file:
        user_ids = file.read().splitlines()

    # Suspend each user
    for user_id in user_ids:
        suspend_user(user_id)

if __name__ == '__main__':
    main()
