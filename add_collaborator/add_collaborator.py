import requests

from constants_file import TOKEN, USERNAME


def add_collaborator(repo_name, collaborator_username):
    headers = {
        'Authorization': 'token ' + TOKEN,
        'Accept': 'application/vnd.github.v3+json'
    }
    add_collaborator_url = f'https://api.github.com/repos/{USERNAME}/{repo_name}/collaborators/{collaborator_username}'
    response = requests.put(add_collaborator_url, headers=headers)
    if response.status_code == requests.codes.created:
        return("Collaborator added successfully")

    else:
        return(f"Failed to add collaborator. Status code: {response.status_code}")


# Example usage:
# try:
#     repository_to_create = add_collaborator("Test1","nova-21")
#     print(repository_to_create)
# except ValueError as e:
#     print(f"Error: {e}")