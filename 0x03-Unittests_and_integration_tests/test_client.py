#!/usr/bin/env python3
"""
Test the client module
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import (
        GithubOrgClient,
)


class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([
        ('google',),
        ('abc',),
    ])
    @patch('client.get_json',
           return_value={'repos_url':
                         'https://api.github.com/orgs/repos'})
    def test_org(self, org_name, mock_get_json):
        """
        test that `GithubOrgClient.org` returns the correct value
        """
        client = GithubOrgClient(org_name)
        result = client.org
        mock_get_json.assert_called_once_with(
                f'https://api.github.com/orgs/{org_name}')
        self.assertEqual(result,
                         {'repos_url': 'https://api.github.com/orgs/repos'})

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        test the `GithubOrgClient._public_repos_url` method
        """
        mock_org.return_value = {'repos_url':
                                 'https://api.github.com/orgs/test_org/repos'}
        client = GithubOrgClient('test_org')

        result = client._public_repos_url
        self.assertEqual(result,
                         'https://api.github.com/orgs/test_org/repos')

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        test that the list of repos is what you'd expect from
        the chosen payload
        """
        mock_get_json.return_value = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": {"key": "mit"}}
        ]
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = \
                    'https://api.github.com/orgs/test_org/repos'
            client = GithubOrgClient('test_org')

            result = client.public_repos()
            self.assertEqual(result, ['repo1', 'repo2', 'repo3'])
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                    'https://api.github.com/orgs/test_org/repos')
