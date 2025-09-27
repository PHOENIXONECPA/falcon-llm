import requests

def fetch_apify_data(api_url):
    """Fetch data from the Apify dataset API."""
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()

def add_items_to_dataset(dataset_id, items, apify_token):
    """
    Add items to a target Apify dataset.
    Args:
        dataset_id (str): Target Apify dataset ID.
        items (list): List of items to add.
        apify_token (str): Apify API token for authentication.
    """
    url = f"https://api.apify.com/v2/datasets/{dataset_id}/items"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {apify_token}"
    }
    response = requests.post(url, json=items, headers=headers)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    # Source dataset API URL
    source_api_url = "https://api.apify.com/v2/datasets/ed2vzvDfE86Ajhuso/items?format=json&clean=true"
    # Target dataset ID (replace this with your target dataset)
    target_dataset_id = "YOUR_TARGET_DATASET_ID"
    # Apify API token (replace with your actual token)
    apify_token = "YOUR_APIFY_API_TOKEN"

    # Fetch items from source
    items = fetch_apify_data(source_api_url)

    # Add items to target dataset
    result = add_items_to_dataset(target_dataset_id, items, apify_token)
    print("Items added result:", result)