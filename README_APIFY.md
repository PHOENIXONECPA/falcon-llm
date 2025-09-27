# Apify Data Processor

This module provides functionality to fetch data from Apify datasets and add items to target datasets.

## Usage

The script `apify_data_processor.py` contains two main functions:

### `fetch_apify_data(api_url)`
Fetches data from the Apify dataset API.

**Parameters:**
- `api_url` (str): The URL of the Apify dataset API endpoint

**Returns:**
- JSON response containing the dataset items

### `add_items_to_dataset(dataset_id, items, apify_token)`
Adds items to a target Apify dataset.

**Parameters:**
- `dataset_id` (str): Target Apify dataset ID
- `items` (list): List of items to add to the dataset
- `apify_token` (str): Apify API token for authentication

**Returns:**
- JSON response from the API

## Running the Script

To use the script:

1. Replace the placeholder values in the main section:
   - `YOUR_TARGET_DATASET_ID`: Your actual target dataset ID
   - `YOUR_APIFY_API_TOKEN`: Your actual Apify API token

2. Run the script:
   ```bash
   python apify_data_processor.py
   ```

## Configuration

The script is pre-configured to fetch data from:
```
https://api.apify.com/v2/datasets/ed2vzvDfE86Ajhuso/items?format=json&clean=true
```

You can modify the `source_api_url` variable to fetch from a different dataset.

## Testing

Run the tests to validate functionality:
```bash
python test_apify_processor.py
```