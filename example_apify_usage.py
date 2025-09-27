#!/usr/bin/env python3
"""
Example usage of the apify_utils module for working with Apify datasets.

This example demonstrates how to:
1. Fetch data from a source Apify dataset
2. Process or filter the data if needed
3. Add the data to a target Apify dataset

Usage:
    python3 example_apify_usage.py

Note: You'll need to replace the placeholder values with your actual:
- Source dataset API URL
- Target dataset ID
- Apify API token
"""

from apify_utils import fetch_apify_data, add_items_to_dataset
import os

def main():
    # Configuration - replace these with your actual values
    source_api_url = os.getenv('APIFY_SOURCE_URL', "https://api.apify.com/v2/datasets/ed2vzvDfE86Ajhuso/items?format=json&clean=true")
    target_dataset_id = os.getenv('APIFY_TARGET_DATASET_ID', "YOUR_TARGET_DATASET_ID")
    apify_token = os.getenv('APIFY_API_TOKEN', "YOUR_APIFY_API_TOKEN")
    
    print("Apify Dataset Transfer Utility")
    print("=" * 40)
    
    # Check if configuration is set
    if target_dataset_id == "YOUR_TARGET_DATASET_ID" or apify_token == "YOUR_APIFY_API_TOKEN":
        print("⚠️  Please set your actual target dataset ID and API token before running.")
        print("   You can set them as environment variables:")
        print("   export APIFY_TARGET_DATASET_ID='your_dataset_id'")
        print("   export APIFY_API_TOKEN='your_api_token'")
        print("\n   Or modify the values directly in this script.")
        return
    
    try:
        # Step 1: Fetch data from source dataset
        print(f"📥 Fetching data from source: {source_api_url}")
        items = fetch_apify_data(source_api_url)
        print(f"✓ Successfully fetched {len(items)} items from source dataset")
        
        # Step 2: Optional data processing
        # You can add filtering, transformation, or validation logic here
        processed_items = items  # For now, we'll use items as-is
        
        # Example of basic filtering (uncomment if needed):
        # processed_items = [item for item in items if some_condition(item)]
        
        print(f"📝 Processing complete. {len(processed_items)} items ready for transfer.")
        
        # Step 3: Add items to target dataset
        print(f"📤 Adding items to target dataset: {target_dataset_id}")
        result = add_items_to_dataset(target_dataset_id, processed_items, apify_token)
        print(f"✓ Successfully added items to target dataset")
        print(f"📊 Result: {result}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Please check your configuration and network connection.")

if __name__ == "__main__":
    main()