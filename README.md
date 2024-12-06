# eBay Image Downloader

> **❤️ Support This Project**
> 
> If you find this tool helpful, consider buying me a coffee:
> 
> [![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/dbsurplussolutions)
>
> Your support helps maintain and improve this tool. Thank you!

A Python script to download images from eBay listings based on CSV input data.

## Features

- Reads CSV-formatted input data containing eBay item information
- Downloads images from eBay item listings
- Organizes downloaded images into directories based on item titles
- Multi-threaded downloading for improved performance
- Handles errors gracefully with informative messages
- Sanitizes directory names to avoid invalid characters

## Requirements

- Python 3.x
- `requests` library for downloading images

Install dependencies:
```bash
pip install -r requirements.txt
```

## Input Data Format

The script expects a CSV file (`input_data.txt`) with the following columns:
1. eBay Item ID (Column 1)
2. Item Title (Column 6)
3. Image URL (Column 7)

Example CSV format:
```
item_id,field2,field3,field4,field5,title,image_url
123456,,,,,Example Item,https://i.ebayimg.com/example.jpg
```

## Usage

1. Place your input data in `input_data.txt` with the required CSV format
2. Run the script:
```bash
python ebay-parsestore.py
```

The script will:
1. Read the input data file
2. Create directories for each item based on their titles
3. Download images into their respective directories
4. Skip any invalid URLs or problematic entries with appropriate error messages

## Output Structure

```
ebay_items/
├── Item1_Title/
│   └── Item1_Title_Img1.JPG
├── Item2_Title/
│   └── Item2_Title_Img1.JPG
└── ...
```

## Error Handling

The script handles various error cases:
- Invalid URLs
- Network errors during download
- Invalid file paths
- Malformed input data

Error messages will be printed to the console for debugging purposes.

## Notes

- The script automatically skips the header row in the CSV file
- Directory names are sanitized to remove invalid characters
- Images are downloaded concurrently using a thread pool for better performance
- Failed downloads are logged but don't stop the overall process
