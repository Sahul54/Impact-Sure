# Write a Python program to upload files on SharePoint.

# pip install Office365-REST-Python-Client --> Install 
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File
from office365.runtime.auth.client_credential import ClientCredential

# SharePoint site and document library details
site_url = "https://sahul-sharepoint-site-url"
doc_library = "Shared Wala Documents"  # Replace with your document library name

# Authentication credentials
client_id = "your-client-id"
client_secret = "your-client-secret"

# File details
file_path = "path/to/your/file.txt"
target_folder = "/sites/sahul/Shared Documents"  # Adjust this to your folder structure

# Connect to the SharePoint site
credentials = ClientCredential(client_id, client_secret)
ctx = ClientContext(site_url).with_credentials(credentials)

# Open the file and upload it to SharePoint
with open(file_path, 'rb') as file_content:
    target_file_url = f"{target_folder}/{file_path.split('/')[-1]}"
    file_upload = ctx.web.get_folder_by_server_relative_url(doc_library).upload_file(target_file_url, file_content)
    ctx.execute_query()
    print(f"File '{file_upload.serverRelativeUrl}' has been uploaded successfully.")
