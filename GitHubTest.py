import unittest
from unittest.mock import patch
import GitHubApi


class TestGetHub(unittest.TestCase):

    @patch("GitHubApi.getrepo")
    def testConnection1(self, mock_connect):
        mock_connect.return_value = [200, {"helloworld": "2",
                                           "Assignment-2": "1",
                                           "vaibhavvashisht16": "12",
                                           "Triangle567": "8",
                                           "CS546": "14",
                                           "Homework-04a---Develop-with-the-Perspective-of-the-Tester-in-mind": "10",
                                           "HW-05---Static-Code-Analysis": "4"}]
        self.assertTrue(GitHubApi.getrepo("vaibhavvashisht16")[0])

    @patch("GitHubApi.getrepo")
    def test_repos1(self, mock_connect):
        mock_connect.return_value = [200, {"helloworld": "2",
                                           "Assignment-2": "1",
                                           "vaibhavvashisht16": "12",
                                           "Triangle567": "8",
                                           "CS546": "14",
                                           "Homework-04a---Develop-with-the-Perspective-of-the-Tester-in-mind": "10",
                                           "HW-05---Static-Code-Analysis": "4"}]
        self.assertIs(mock_connect()[1], GitHubApi.getrepo("vaibhavvashisht16")[1])

    @patch("GitHubApi.getrepo")
    def testConnection2(self, mock_connect):
        mock_connect.return_value = [200, {""}]
        self.assertTrue(GitHubApi.getrepo("GautamP2393")[0])

    @patch("GitHubApi.getrepo")
    def test_repos2(self, mock_connect):
        mock_connect.return_value = [200, {""}]
        self.assertIs(mock_connect()[1], GitHubApi.getrepo("GautamP2393")[1])


if __name__ == '__main__':
    print('Running unit tests')
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGetHub)
    unittest.TextTestRunner(verbosity=2).run(suite)

