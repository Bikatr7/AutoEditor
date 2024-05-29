def page_duplication(document):
    requests = []
    paragraphs = []
    page_break_indices = [0]  
    last_index = 0

    for element in document['body']['content']:
        if('paragraph' in element):
            ## Get the text from the paragraph
            text = ''.join([run['textRun']['content'] for run in element['paragraph']['elements'] if 'textRun' in run])
            
            ## Get the end index of the paragraph
            end_index = element['endIndex'] - 1
            
            ## Store the paragraph text and its end index
            paragraphs.append((end_index, text))
            last_index = end_index
        
        if('sectionBreak' in element and 'startIndex' in element):
            page_break_indices.append(element['startIndex'])

    ## Append the end of the document as a page break
    page_break_indices.append(last_index + 1)

    ## Insert the paragraphs in reverse order to avoid shifting issues
    for i in range(len(page_break_indices) - 1, 0, -1):
        page_paragraphs = [(end_index, text) for end_index, text in paragraphs 
                           if page_break_indices[i-1] <= end_index < page_break_indices[i]]
        
        for end_index, text in reversed(page_paragraphs):
            requests.append({
                'insertText': {
                    'location': {
                        'index': end_index,
                    },
                    'text': '\n' + text
                }
            })

    return requests