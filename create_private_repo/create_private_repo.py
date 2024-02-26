import random

import requests
import os
import subprocess
import json

from constants_file import LOCAL_PATH, TOKEN, USERNAME


def create_private_repo(repo_name):
    if repo_name:
        local_folder = os.path.join(LOCAL_PATH, repo_name)
        headers = {
            'Authorization': 'token ' + TOKEN,
            'Accept': 'application/vnd.github.v3+json'
        }
        data = {'name': repo_name, 'private': True}
        create_repo_url = 'https://api.github.com/user/repos'
        response = requests.post(create_repo_url, headers=headers, data=json.dumps(data))
        if response.status_code == requests.codes.created:
            print("Success", "Repository created successfully")
            os.makedirs(local_folder, exist_ok=True)
            os.chdir(local_folder)
            subprocess.run(['git', 'init'])
            remote_url = f'https://github.com/{USERNAME}/{repo_name}.git'
            subprocess.run(['git', 'remote', 'add', 'origin', remote_url])
            return "Success"
        else:
            return("Error", f"Failed to create repository. Status code: {response.status_code}")


# Example usage:
# try:
#     repository_to_create = create_private_repo(f"Test{random.randint(1, 70)}")
#     print(repository_to_create)
# except ValueError as e:
#     print(f"Error: {e}")