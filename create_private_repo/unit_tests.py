import random
import unittest
import mock
import json

from create_private_repo import create_private_repo

from constants_file import LOCAL_PATH, TOKEN, USERNAME

class TestCreatePrivateRepo(unittest.TestCase):

    @mock.patch('requests.post')
    def test_create_success(self, mock_request_post):
        mock_response = mock.Mock()
        mock_response.status_code = 201
        mock_request_post.return_value = mock_response
        repo_name = "TestRepo"
        result = create_private_repo(f"{repo_name}{random.randint(1, 70)}")
        self.assertEqual(result, "Success")

    @mock.patch('requests.post')
    def test_create_failed(self, mock_request_post):
        mock_response = mock.Mock()
        mock_response.status_code = 401
        mock_request_post.return_value = mock_response

        repo_name = "TestRepo"
        result = create_private_repo(repo_name)
        self.assertTrue(result[0] == "Error")
        self.assertEqual(result[1], f"Failed to create repository. Status code: 401")

if __name__ == "__main__":
    unittest.main()