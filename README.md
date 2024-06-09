## AutoEditor
Exploration into an auto-editor for LN translations.

This project aimed to be used with [Kudasai](https://github.com/Bikatr7/Kudasai).

## Old Plans
### Known Issues
1. GPT could interfere with the text excessively. We need to ensure only relevant text is given to edit, avoiding non-text content like tables of contents (TOCs) and in the cae of Goal #1, avoiding quotes.
2. Doing many passes, is at best, expensive, and at worst, reckless.

### Goals
Automate the following steps:
1. **Tense Correction**: Convert narration into simple past tense.
2. **Formatting**: Italicize calls and text messages.
3. **Pronoun Correction**: Use a gender chart for accurate pronoun use.

## Old Architecture Plans
To be used in conjunction with Kudasai ([Kudasai GitHub Repository](https://github.com/bikatr7/kudasai)). The AutoEditor would take outputs from Kudasai (translated_text.txt and je_check_text.txt) and produce:

1. **auto_edited_text.txt**: The final edited text.
2. **je_check_text_with_auto_edits.txt**: The JE check text with auto edits, either as a new layer, logs underneath, or replacing the old one.
3. **editing_log.txt**: A log file containing records of the changes made.

## Realizations
1. **Single Pass Strategy**: Performing multiple passes on already translated text is not effective. LLMs do not follow instructions well enough in certain areas, so the best strategy is to do as much as possible in a single pass.
2. **Pronoun Correction**: This was a genius idea and can be done by determining the genders of named entities ahead of time. Inserting them into the system prompt speeds up the process.
3. **Integration with Kudasai**: It's much easier to combine the logic of AutoEditor into Kudasai, making it more specialized and efficient.

## Postnote
The AutoEditor project primarily involved planning what needed to be done to advance Kudasai's workflow. 

- Goals 1 and 2 of the original plan can be achieved to an acceptable degree by including them in the system prompt, avoiding additional passovers.
- Goal 3 can also be accomplished by the above method, though it is more complicated.

The planned features of AutoEditor will be integrated directly into Kudasai. As of AutoEditor's archiving on June 9, 2024, this integration was already in progress by Bikatr7, with an intended release in version 3.4.9.