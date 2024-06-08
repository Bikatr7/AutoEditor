import re

def generate_sentence_chunks(input_string, split_index):
    def find_sentence_end(s, start_index):
        match = re.search(r'[.!?](\s|$)', s[start_index:])
        if match:
            return start_index + match.end()
        else:
            return len(s)
    
    result = []
    current_index = 0
    
    while current_index < len(input_string):
        if current_index + split_index < len(input_string):
            end_index = find_sentence_end(input_string, current_index + split_index)
        else:
            end_index = len(input_string)
        
        result.append(input_string[current_index:end_index])
        current_index = end_index
    
    return result