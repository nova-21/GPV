import unittest
import mock
import json

from get_list_of_repositories.get_repos import get_repositories

try:
    repos_info = get_repositories()
    for repo in repos_info:
        print(f"Repo Name: {repo['name']}, Status: {repo['status']}")
except ValueError as e:
    print(f"Error: {e}")