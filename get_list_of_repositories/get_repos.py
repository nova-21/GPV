import requests
import os
import subprocess
import json

from constants_file import LOCAL_PATH, TOKEN, USERNAME

def get_repositories():
    token = TOKEN
    headers = {
        'Authorization': 'token ' + token,
        'Accept': 'application/vnd.github.v3+json'
    }
    get_repos_url = f'https://api.github.com/user/repos?type=private'
    response = requests.get(get_repos_url, headers=headers)

    if response.status_code == requests.codes.ok:
        repos = json.loads(response.text)
        repo_info = []

        for repo in repos:
            repo_name = repo['name']
            local_status = "Local" if os.path.exists(os.path.join(LOCAL_PATH, repo_name)) else "En línea"
            repo_info.append({"name": repo_name, "status": local_status})

        return repo_info
    else:
        raise ValueError(f"No se pudieron obtener los repositorios. Código de estado: {response.status_code}")

# Example usage:
# try:
#     repos_info = get_repositories()
#     for repo in repos_info:
#         print(f"Repo Name: {repo['name']}, Status: {repo['status']}")
# except ValueError as e:
#     print(f"Error: {e}")
