def text_duplication(document):

    requests = []
    paragraphs = []

    ## Iterate over the elements in the document to find paragraphs and their end indices
    for element in document['body']['content']:
        if('paragraph' in element):
            ## Get the text from the paragraph
            text = ''.join([run['textRun']['content'] for run in element['paragraph']['elements'] if 'textRun' in run])
            
            ## Get the end index of the paragraph
            end_index = element['endIndex'] - 1
            
            ## Store the paragraph text and its end index
            paragraphs.append((end_index, text))

    ## Insert the paragraphs in reverse order to avoid shifting issues
    for end_index, text in reversed(paragraphs):
        requests.append({
            'insertText': {
                'location': {
                    'index': end_index,
                },
                'text': '\n' + text
            }
        })

    return requests