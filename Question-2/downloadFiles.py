# Write a Python program to download files from the server. If the downloaded files are zip files it should
# be extracted in the C:\\Extracted Folder and the name of the folder should be the same as the
# downloaded file.

import os
import requests
import zipfile

def download_file(url, download_path):
    """Download a file from a URL and save it locally."""
    response = requests.get(url)
    with open(download_path, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded: {download_path}")

def extract_zip(file_path, extract_to):
    """Extract a ZIP file to a specified directory."""
    if zipfile.is_zipfile(file_path):
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print(f"Extracted: {file_path} to {extract_to}")
    else:
        print(f"{file_path} is not a ZIP file.")

def main():
    url = 'https://example.com/file.zip'  # Replace with the actual file URL
    download_folder = 'C:\\Downloads'  # Folder where files will be downloaded
    extract_folder_base = 'C:\\Extracted'  # Base folder for extraction

    # Ensure the download folder exists
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # Download the file
    file_name = os.path.basename(url)
    download_path = os.path.join(download_folder, file_name)
    download_file(url, download_path)

    # Extract if it's a ZIP file
    if file_name.endswith('.zip'):
        extract_to = os.path.join(extract_folder_base, os.path.splitext(file_name)[0])
        if not os.path.exists(extract_to):
            os.makedirs(extract_to)
        extract_zip(download_path, extract_to)

if __name__ == '__main__':
    main()
