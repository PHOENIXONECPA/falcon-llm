"""
Simple tests for the Apify data processor to validate basic functionality.
"""
import unittest
from unittest.mock import Mock, patch
import apify_data_processor

class TestApifyDataProcessor(unittest.TestCase):
    
    @patch('apify_data_processor.requests.get')
    def test_fetch_apify_data_success(self, mock_get):
        """Test successful data fetching from Apify API."""
        # Mock successful response
        mock_response = Mock()
        mock_response.json.return_value = [{"id": 1, "data": "test"}]
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        # Test the function
        result = apify_data_processor.fetch_apify_data("http://test-url.com")
        
        # Assertions
        mock_get.assert_called_once_with("http://test-url.com")
        mock_response.raise_for_status.assert_called_once()
        self.assertEqual(result, [{"id": 1, "data": "test"}])
    
    @patch('apify_data_processor.requests.post')
    def test_add_items_to_dataset_success(self, mock_post):
        """Test successful addition of items to dataset."""
        # Mock successful response
        mock_response = Mock()
        mock_response.json.return_value = {"success": True}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        # Test data
        dataset_id = "test_dataset_id"
        items = [{"id": 1, "data": "test"}]
        token = "test_token"
        
        # Test the function
        result = apify_data_processor.add_items_to_dataset(dataset_id, items, token)
        
        # Expected URL and headers
        expected_url = f"https://api.apify.com/v2/datasets/{dataset_id}/items"
        expected_headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
        
        # Assertions
        mock_post.assert_called_once_with(expected_url, json=items, headers=expected_headers)
        mock_response.raise_for_status.assert_called_once()
        self.assertEqual(result, {"success": True})

if __name__ == '__main__':
    unittest.main()