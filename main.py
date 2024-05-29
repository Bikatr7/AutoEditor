## third-party libraries
from google.oauth2 import service_account
from googleapiclient.discovery import build

## custom modules
from possible_approaches.text_duplication import text_duplication

## Load credentials from the JSON file
SCOPES = ['https://www.googleapis.com/auth/documents']
creds = service_account.Credentials.from_service_account_file('credentials.json', scopes=SCOPES)

## Create the service object
service = build('docs', 'v1', credentials=creds)

## The ID of the document to update
DOCUMENT_ID = '1BYRyHOcTuCiPj0Jrdf8_3kO7kU6YnYgD0al-06xPVqM'

try:
    ## Get the document
    document = service.documents().get(documentId=DOCUMENT_ID).execute()

except Exception as e:

    DOCUMENT_ID = input(f"Document retrieved failed due to {e}. \n\nPlease enter the document ID: ") 
    document = service.documents().get(documentId=DOCUMENT_ID).execute()


    requests = text_duplication(document)



## Send the request to the Google Docs API
result = service.documents().batchUpdate(documentId=DOCUMENT_ID, body={'requests': requests}).execute()

print(result)
