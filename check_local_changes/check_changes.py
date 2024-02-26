import os
import subprocess

from constants_file import LOCAL_PATH


def check_local_changes(repo_name):
    local_folder = os.path.join(LOCAL_PATH, repo_name)
    os.chdir(local_folder)
    status_output = subprocess.check_output(['git', 'status', '--porcelain']).decode('utf-8')

    if status_output:
        return ("There are local changes in the repository.")
    else:
        return ("No local changes in the repository.")

# try:
#     print(check_local_changes("Test9"))
# except:
#     print("Failed")
