import os
import random
import subprocess

from check_local_changes.check_changes import check_local_changes
from constants_file import LOCAL_PATH

def create_commit_and_push(repo_name):
    local_folder = os.path.join(LOCAL_PATH, repo_name)

    # Change working directory to the local repository folder
    os.chdir(local_folder)

    # Check for local changes
    local_changes = check_local_changes(repo_name)

    if local_changes == "There are local changes in the repository.":
        try:
            # Stage all changes
            subprocess.run(['git', 'add', '.'])

            # Commit changes
            subprocess.run(['git', 'commit', '-m', 'Add new changes'])

            # Push changes to the remote repository
            subprocess.run(['git', 'push', 'origin', 'main'])  # Modify 'main' based on your branch name

            return "Success", "Commit created and pushed successfully."
        except subprocess.CalledProcessError as e:
            return "Error", f"Failed to create commit and push changes. Error: {e}"
    else:
        return("There are no local changes in the repository.")
#
# Example
# try:
#     print(create_commit_and_push("Test9"))
# except:
#     print("Failed")