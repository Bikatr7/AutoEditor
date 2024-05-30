import typing

def get_paragraphs(document) ->  typing.List[typing.Tuple[int, str]]:

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

    return paragraphs

def insert_paragraphs(index_text_tuples:typing.List[typing.Tuple[int, str]]) -> typing.List[typing.Dict[str, typing.Dict[str, str]]]:

    requests = []


    return requests