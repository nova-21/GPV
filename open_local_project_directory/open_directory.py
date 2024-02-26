import os
import subprocess

from constants_file import LOCAL_PATH


def open_directory(directory):
    if os.W_OK:
        subprocess.Popen(f'explorer "{directory}"')

# try:
#     open_directory(LOCAL_PATH)
# except:
#     print("A")