import os
import csv
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Define the scope
SCOPES = ['https://www.googleapis.com/auth/drive.file']

# Authenticate and build the Drive service
def authenticate():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If credentials are not valid or don't exist
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save for future use
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('drive', 'v3', credentials=creds)

def upload_and_share_pdfs(folder_path):
    service = authenticate()
    output_data = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.pdf'):
            file_path = os.path.join(folder_path, filename)
            file_metadata = {'name': filename}
            media = MediaFileUpload(file_path, mimetype='application/pdf')
            file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

            # Make file public
            service.permissions().create(
                fileId=file['id'],
                body={'type': 'anyone', 'role': 'reader'}
            ).execute()

            # Get shareable link
            file_info = service.files().get(fileId=file['id'], fields='webViewLink').execute()
            output_data.append((filename, file_info['webViewLink']))

    # Write to CSV
    with open('pdf_links.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['PDF Name', 'Public URL'])
        writer.writerows(output_data)

    print("Links saved to pdf_links.csv")

# Call with the local folder path
upload_and_share_pdfs('path_to_your_pdf_folder')
