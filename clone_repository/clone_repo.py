import os
import subprocess

from constants_file import LOCAL_PATH, TOKEN, USERNAME

def clone_repo(repo_name, local_path=None):
    local_folder = os.path.join(local_path or LOCAL_PATH, repo_name)
    if not os.path.exists(local_folder):
        print(f"{repo_name} does not exist locally. Cloning...")
        os.makedirs(local_folder, exist_ok=True)
        try:
            subprocess.check_call(['git', 'clone', f'https://{TOKEN}@github.com/{USERNAME}/{repo_name}.git', local_folder])
            print(f"{repo_name} cloned successfully.")
            return repo_name
        except subprocess.CalledProcessError as e:
            print(f"Error cloning {repo_name}: {e}")
            return False
    else:
        print(f"{repo_name} already exists locally.")
        return repo_name if os.path.isdir(local_folder) else False

#Example
# try:
#     clone_repo("Test9")
# except:
#     print("Failed")