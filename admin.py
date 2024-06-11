import csv
import requests

def list_repo_collaborators(api_endpoint, github_pat, org_name, csv_file_path, output_csv_file=None):
    """
    Get a list of collaborators for repositories listed in a CSV file and optionally store it in another CSV file.
 
    Inputs:
    - API endpoint (for GHES/GHAE compatibility)
    - PAT of appropriate scope
    - Organization name
    - CSV file path containing repository names
    - (Optional) CSV file path to store the collaborators
 
    Outputs:
    - Dictionary where keys are repository names and values are lists of admin collaborators for each repository
    """
    try:
        with open(csv_file_path, 'r') as csvfile:
            # Read the CSV file
            csv_reader = csv.reader(csvfile)
            next(csv_reader)  # Skip the header row
            repo_collaborators = {}

            for row in csv_reader:
                repo_name = row[0].strip()  # Get the repository name from the first column
                
                # Construct the URL for fetching collaborators
                collaborators_url = f"{api_endpoint}/repos/{org_name}/{repo_name}/collaborators"

                # Set up headers with the authorization token
                headers = {
                    'Authorization': f'token {github_pat}'
                }

                # Make the API call to fetch collaborators
                response = requests.get(collaborators_url, headers=headers)
                response.raise_for_status()  # Raise an exception for any HTTP error
                collaborators = response.json()

                # Extract admin collaborators
                admin_collaborators = [collaborator["login"] for collaborator in collaborators if collaborator["permissions"]["admin"]]

                # Store the admin collaborators in the dictionary
                repo_collaborators[repo_name] = admin_collaborators

        # If a CSV file path for output is provided, store the admin collaborators in the CSV
        if output_csv_file:
            with open(output_csv_file, 'w', newline='') as outfile:
                writer = csv.writer(outfile)
                writer.writerow(['Repository'] + [f'Admin Collaborator {i+1}' for i in range(max(len(admins) for admins in repo_collaborators.values()))])
                for repo, admins in repo_collaborators.items():
                    writer.writerow([repo] + admins)
            print(f"Admin collaborators saved to {output_csv_file}")

        return repo_collaborators

    except FileNotFoundError:
        print(f"CSV file not found: {csv_file_path}")
        return {}
    except requests.exceptions.RequestException as e:
        print(f"Error fetching collaborators: {e}")
        return {}

# Example usage
api_endpoint = "https://api.github.com"
github_pat = "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"
org_name = "hotstar-org"
input_csv_file = "github_repos.csv"
output_csv_file = "admin_collaborators.csv"

repo_collaborators = list_repo_collaborators(api_endpoint, github_pat, org_name, input_csv_file, output_csv_file)
print("Repository Collaborators:", repo_collaborators)
