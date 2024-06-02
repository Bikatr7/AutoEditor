## custom modules
from modules.text_splitter import generate_sentence_chunks

with open('sample_text/short.txt', 'r', encoding='utf-8') as f:
    text = f.read()

reassembled_text = ""

chunks = generate_sentence_chunks(text, 1000)

for chunk in chunks:
    print(chunk)
    print("-----")
