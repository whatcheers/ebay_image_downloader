# ebay_scripts

Collection of Ebay scripts for /r/ebayselleradvice

## Overview

This script allows you to download images from eBay listings. You need to provide a CSV file with eBay IDs, titles, and image URLs. The script will download all the images into separate directories based on the item titles.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/whatcheers/ebay_scripts.git
    cd ebay_scripts
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv ebay_env
    source ebay_env/bin/activate  # On Windows use `ebay_env\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Prepare your input data:**

    - Obtain the CSV file from the specified website.
    - That website is [https://www.isdntek.com/ebaytools/BulkPhotoScanner.htm](https://www.isdntek.com/ebaytools/BulkPhotoScanner.htm)
    - Enter the store name, select the site, and then get items. Then hit auto scan.
    - Once the scan completes, scroll down to the report, select "semicolon separated" and "ZipAll". Select "include titles" and then build the report.
    - Once this completes, select all the text and paste it into a CSV file in the same directory as this script named `input_data.csv`.

    The CSV file should have the following format:

    ```
    ebay_id;title;image_urls
    ```

    Example:

    ```
    1234567890;Sample Item;"https://example.com/image1.jpg|https://example.com/image2.jpg"
    ```

2. **Run the script:**

    ```sh
    python ebay-parsestore.py
    ```

3. **Check the downloaded images:**

    - The images will be downloaded into the `ebay_items` directory.
    - Each item will have its own subdirectory named after the item's title (sanitized and truncated to 20 characters).

## Notes

- Ensure that the URLs in the CSV file are valid and accessible.
- The script uses a multi-threaded approach to download images concurrently.
- This script was tested on Windows 11 only.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.