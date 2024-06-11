import csv
import requests

def fetch_all_repositories():
    # Define the GitHub API endpoint and organization name
    url = 'https://api.github.com/orgs/hotstar-org/repos'

    # Define headers with authorization token and API version
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': 'Bearer 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',
        'X-GitHub-Api-Version': '2022-11-28'
    }

    all_repos = []

    # Start with page 1
    page = 1

    while True:
        # Add the page parameter to the URL
        params = {'page': page}

        # Send GET request to GitHub API
        response = requests.get(url, headers=headers, params=params)

        # Check if request was successful (status code 200)
        if response.status_code == 200:
            # Parse JSON response
            repos = response.json()
            # If there are no more repositories, break out of the loop
            if not repos:
                break
            # Extend the list of repositories with the ones from this page
            all_repos.extend(repos)
            # Move to the next page
            page += 1
        else:
            print('Failed to fetch repositories. Status code:', response.status_code)
            break

    return all_repos

# Fetch all repositories
all_repositories = fetch_all_repositories()

# Specify the file path for CSV
csv_file_path = 'github_repos.csv'

# Define CSV header
csv_header = ['Name', 'Description', 'URL']

# Write repository data to CSV file
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_header)
    writer.writeheader()
    for repo in all_repositories:
        writer.writerow({'Name': repo['name'], 'Description': repo['description'], 'URL': repo['html_url']})

print(f'Repositories data has been saved to {csv_file_path}.')
