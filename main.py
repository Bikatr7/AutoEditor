## third-party libraries
from google.oauth2 import service_account
from googleapiclient.discovery import build

## custom modules
from possible_approaches.text_duplication import text_duplication
from possible_approaches.page_duplication import page_duplication
from possible_approaches.inline_edits import get_paragraphs, insert_paragraphs

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

## Get the requests to duplicate the text
##requests = text_duplication(document)
##requests = page_duplication(document)
index_text_tuples = get_paragraphs(document)

for i, (index, text) in enumerate(index_text_tuples):
    print(f"{i+1}. {text}")

requests = insert_paragraphs(index_text_tuples)

## Send the request to the Google Docs API
result = service.documents().batchUpdate(documentId=DOCUMENT_ID, body={'requests': requests}).execute()

print(result)
