import requests
import csv

# GitHub API endpoint for outside collaborators of an organization
url = 'https://api.github.com/orgs/hotstar-org/outside_collaborators'

# Personal access token (replace with your own token)
token = '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'

# GitHub API version
api_version = '2022-11-28'

# Headers for the request
headers = {
    'Accept': 'application/vnd.github.v3+json',
    'Authorization': f'Bearer {token}',
    'X-GitHub-Api-Version': api_version
}

try:
    # Send GET request to GitHub API
    response = requests.get(url, headers=headers)
    
    # Check if request was successful
    if response.status_code == 200:
        # Extract JSON data
        outside_collaborators = response.json()
        
        # CSV file name to save data
        csv_file = 'outside_collaborators.csv'
        
        # Extracting relevant data for CSV
        fieldnames = ['login', 'id', 'type', 'site_admin']
        
        # Writing data to CSV
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for collaborator in outside_collaborators:
                writer.writerow({
                    'login': collaborator['login'],
                    'id': collaborator['id'],
                    'type': collaborator['type'],
                    'site_admin': collaborator['site_admin']
                })
        
        print(f"Successfully saved outside collaborators to {csv_file}")
    else:
        print(f"Failed to retrieve outside collaborators. Status code: {response.status_code}")
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
