## custom modules
from modules.text_splitter import generate_sentence_chunks
from modules.GPTConnector import GPTConnector

async def main():

    with open('sample_text/short.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    with open ('openai.txt', 'r', encoding='utf-8') as f:
        api_key = f.read()

    GPTConnector.set_api_key(api_key)

    tense_correction_prompt = "For the below text, please correct all narration (text without quotes) into simple past tense. Your response should be the altered text, in the exact same sentence structure. (all text provided, but with the necessary corrections (no text in quotes changed, spacing preserved. Same number of lines.))"

    chunks = generate_sentence_chunks(text, 1000)
    new_chunks = []

    for chunk in chunks:
        print(chunk)
        print("-----")



    for chunk in chunks:
        response = await GPTConnector.make_request("gpt-4o", prompt=chunk, instructions=tense_correction_prompt)
        new_chunks.append(response)

    for old_chunk, new_chunk in zip(chunks, new_chunks):
        print("old_chunk")
        print(old_chunk)
        print("-----")
        print("new_chunk")
        print(new_chunk)
        print("-----")
        
    new_text = " ".join(new_chunks)

    with open('sample_text/short_corrected.txt', 'w', encoding='utf-8') as f:
        f.write(new_text)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())