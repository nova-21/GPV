import requests

from constants_file import TOKEN, USERNAME


def get_collaborators(repo_name):
    headers = {
        'Authorization': 'token ' + TOKEN,
        'Accept': 'application/vnd.github.v3+json'
    }
    collaborators_url = f'https://api.github.com/repos/{USERNAME}/{repo_name}/collaborators'

    try:
        response = requests.get(collaborators_url, headers=headers)
        if response.status_code == requests.codes.ok:
            collaborators_list = [collaborator['login'] for collaborator in response.json()]
            return "Success", collaborators_list
        else:
            return "Error", f"Failed to retrieve collaborators. Status code: {response.status_code}"
    except requests.RequestException as e:
        return "Error", f"An error occurred while making the request: {e}"

#Example
# result, collaborators = get_collaborators("Test9")
# if result == "Success":
#     print(f"Collaborators in the repository: {collaborators}")
# else:
#     print(f"Error: {collaborators}")
