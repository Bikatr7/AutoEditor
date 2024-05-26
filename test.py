from google.oauth2 import service_account
from googleapiclient.discovery import build

# Load your credentials from the JSON file
SCOPES = ['https://www.googleapis.com/auth/documents']
creds = service_account.Credentials.from_service_account_file('credentials.json', scopes=SCOPES)

# Create the service object
service = build('docs', 'v1', credentials=creds)

# The ID of the document to update
DOCUMENT_ID = '1yi1G0m2Zxf-mJ8tkfY74_vMDYtZp3E96WkeIfRU_yA0'

# Get the document
document = service.documents().get(documentId=DOCUMENT_ID).execute()

requests = []
paragraphs = []

# Iterate over the elements in the document to find paragraphs and their end indices
for element in document['body']['content']:
    if 'paragraph' in element:
        # Get the text from the paragraph
        text = ''.join([run['textRun']['content'] for run in element['paragraph']['elements'] if 'textRun' in run])
        
        # Get the end index of the paragraph
        end_index = element['endIndex'] - 1
        
        # Store the paragraph text and its end index
        paragraphs.append((end_index, text))

# Insert the paragraphs in reverse order to avoid shifting issues
for end_index, text in reversed(paragraphs):
    requests.append({
        'insertText': {
            'location': {
                'index': end_index,
            },
            'text': '\n' + text
        }
    })

# Send the request to the Google Docs API
result = service.documents().batchUpdate(documentId=DOCUMENT_ID, body={'requests': requests}).execute()

print(result)
