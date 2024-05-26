from google.oauth2 import service_account
from googleapiclient.discovery import build

# Load your credentials from the JSON file
SCOPES = ['https://www.googleapis.com/auth/documents']
creds = service_account.Credentials.from_service_account_file('credentials.json', scopes=SCOPES)

# Create the service object
service = build('docs', 'v1', credentials=creds)

# The ID of the document to update
DOCUMENT_ID = '1yi1G0m2Zxf-mJ8tkfY74_vMDYtZp3E96WkeIfRU_yA0'

## insert some text
requests = [
    {
        'insertText': {
            'location': {
                'index': 1,
            },
            'text': 'Hello, world!'
        }
    }
]

## Send the request to the Google Docs API
result = service.documents().batchUpdate(documentId=DOCUMENT_ID, body={'requests': requests}).execute()

print(result)
