import csv
import json
import os
import requests
import time
import re
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def sanitize_filename(filename):
    # Remove or replace characters that are invalid in Windows filenames
    filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    filename = re.sub(r'[~`]', '_', filename)  # Replace ~ and ` with underscore
    filename = re.sub(r'\s+', '', filename)  # Remove all spaces
    filename = filename.strip()  # Remove leading and trailing spaces
    return filename[:20]  # Truncate to 20 characters

def download_image(url, path):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        os.makedirs(os.path.dirname(path), exist_ok=True)  # Ensure directory exists
        with open(path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {path}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
        return False

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def parse_input_data(file_path):
    items = []
    with open(file_path, 'r', encoding='utf-8') as f:
        # Skip header row
        next(f)
        for line in f:
            try:
                # Split by comma but handle quoted fields properly
                parts = line.strip().split(',')
                if len(parts) >= 7:  # Ensure we have at least 7 columns
                    ebay_id = parts[0].strip('"')
                    title = parts[5].strip('"')
                    url = parts[6].strip('"')
                    
                    # Only add if we have a valid URL
                    if url and url.startswith('http'):
                        items.append({
                            'ebay_id': ebay_id,
                            'title': title,
                            'image_urls': [url]
                        })
            except Exception as e:
                print(f"Error processing line: {line.strip()}")
                print(f"Error details: {str(e)}")
                continue
    return items

def process_items(items):
    base_dir = "ebay_items"
    create_directory(base_dir)
    
    download_tasks = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        for item in items:
            # Create directory for item
            folder_name = sanitize_filename(item['title'])
            item_dir = os.path.join(base_dir, folder_name)
            create_directory(item_dir)
            
            # Schedule image downloads
            for url_index, url in enumerate(item['image_urls']):
                if not is_valid_url(url):
                    print(f"Skipping invalid URL: {url}")
                    continue
                
                file_extension = os.path.splitext(urlparse(url).path)[1]
                file_name = f"{folder_name}_Img{url_index + 1}{file_extension}"
                file_path = os.path.join(item_dir, file_name)
                
                download_tasks.append(executor.submit(download_image, url, file_path))
        
        # Wait for all downloads to complete
        for future in as_completed(download_tasks):
            future.result()

# Parse the input data
items = parse_input_data('input_data.txt')

# Process items and download images
process_items(items)

print("Download process completed.")