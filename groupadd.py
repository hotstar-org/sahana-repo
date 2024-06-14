import requests

# Read account IDs from userlist.txt
with open('userlist.txt', 'r') as file:
    account_ids = file.read().splitlines()

# URL and authentication details
url = 'https://jiratest275.atlassian.net/rest/api/3/group/user?groupId=d217b15d-d4a0-4b99-a428-6de4689e1444'
username = 'sahanan@devtools.in'
api_token = 'ATATT3xFfGF0W6uFddHAHtu4T0Luq8O7nIRJNQJwZXsbC7Ln8lJGBBKHenNqzHYVYqn0ApsrR5jSGFj8zo5NWkWLcXHIq6PSwVoz_rJIvCQQvJ_3csBnje4OzMqn9YwVmrKeKpJ9vxEV7X8TviTJajdHJoh4Trmc8HuPZ3VUweZNLogFnxWdv4I=0F9E71DB'

# Headers
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

# Iterate through account IDs and make POST requests
for account_id in account_ids:
    data = {
        'accountId': account_id
    }
    response = requests.post(url, auth=(username, api_token), headers=headers, json=data)
    
    # Print response
    print(f"Account ID: {account_id}, Response: {response.text}")
