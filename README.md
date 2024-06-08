## AutoEditor
Exploration into an auto-editor for LN translations

Goal is to be used with Kudasai.

## Plans
- Known issues:
  1. Gpt could fuck with the text way too much, we need to somehow make sure we only give it the text to edit (not stuff like toc's etc)
  
- Goal: Automate the following steps:
    1. tense correction (narration into simple past tense)
    2. format calls and texting (italize)
    3. pronoun correction (have the gender chart )
   
## Architecture plans
- To be used in conjunction with Kudasai (https://github.com/bikatr7/kudasai)
- Would take in some outputs of Kudasai (translated_text.txt and je_check_text.txt) and output:

  1. auto_edited_text.txt
  2. je_check_text_with_auto_edits.txt (this could either be a new layer, add the logs underneath, or just replace the old one)
  3. editing_log.txt (this would be a new file that would contain the logs of the changes made) 