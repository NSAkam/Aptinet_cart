import unittest
from scripts.Services.restapi import restAPI
from unittest.mock import patch, Mock


class TestRestApi(unittest.TestCase):
    def setUp(self) -> None:
        self.api = restAPI()
        
    @patch('requests.get')
    def test_Get(self, mock_get):
        mock_response = Mock()
        mock_response.text = "Mock response data"
        mock_get.return_value = mock_response
        self.api.Get("")
        self.assertEqual(self.api.recived.emit.call_count, 1)
        self.api.recived.emit.assert_called_once_with("Mock response data")
        
    @patch('requests.post')
    def test_Post(self, mock_post):
        mock_response = Mock()
        mock_response.text = "Mock response data"
        mock_post.return_value = mock_response
        self.api.Post("", {"key": "value"})
        self.assertEqual(self.api.recived.emit.call_count, 1)
        self.api.recived.emit.assert_called_once_with("Mock response data")



if __name__ == '__main__':
    unittest.main()
        
    