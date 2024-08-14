# 1. pip install requests
# 2 .import requests


import requests

def download_file(url, download_path):
    response = requests.get(url)
    with open(download_path, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded: {download_path}")

# Example usage
url = 'https://example.com/file.zip'
download_path = 'C:\\Downloads\\file.zip'
download_file(url, download_path)
