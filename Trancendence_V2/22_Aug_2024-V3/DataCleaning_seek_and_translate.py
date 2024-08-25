###############################################################
## Input Diary is 5-7% in Romanian & Others ##
## This script assesses if text_Chunk is in any other than language and needs translation ##
## Then feeding the found out paragraphs chunks to LLM ##
## Finally, putting it all together into Translated_Data.jsonl - to be later used in PromptResponseDataset creation. ##
## Basically, it is seeking what text is not in english and feeding only the necessary identified non-english patterns
## To an LLM, greatly reducing cost of tokens ##
###############################################################

from langdetect import detect
import os
import json
from openai import OpenAI


def is_english(text_check):
    try:
        return detect(text_check) == 'en'
    except:
        return False


def read_jsonl_and_convert_to_list():
    # Preparing results files to read
    working_dir = os.getcwd()
    file_path_origin = os.path.join(working_dir, r'training_data_original.jsonl')

    # Read the JSONL results from the specified full path
    diary_entries_split = []
    with open(file_path_origin, 'r') as file:
        for line in file:
            json_obj = json.loads(line)
            diary_entries_split.append(json_obj['text'])
    return diary_entries_split


# Function to translate text using integrated OpenAI API calls
def Translate_Agent(chunk_to_translate):
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """I will give you a text in Romanian. (or perhaps some inputs may be in some other languages
                I need you to read & translate the text accurately - yet keeping good flow, logic and grammar.
                Return STRICTLY the translated text - this will be later picked up and appended in json, do not 
                write anything extra. 
                If you think there is anything which might trigger your security policy, please skip that part, words,
                Or slightly modify them keeping the same context & sentiment so that everything is fine regarding
                policy"""
            },
            {
                "role": "user",
                "content": f"The text to be translated is: '{chunk_to_translate}'"
            }
        ]
    )

    response_text = response.choices[0].message.content
    return response_text


#####################
### Script Begins ###
#####################

text = read_jsonl_and_convert_to_list()
translated_text = []
translations_count = 0

for chunk in text:
    langauge_check = is_english(chunk)
    if langauge_check:
        # If text is in English, append it as is
        translated_text.append(chunk)

    if not langauge_check:
        translated = Translate_Agent(chunk)
        translated_text.append(translated)
        print(f"Non-English text found and translated: {translated} \n")
        translations_count += 1

print(f"Translations completed with Total of {translations_count} processed translations."
      )
with open('translated_data.jsonl', 'w') as outfile:
    for item in translated_text:
        json.dump({"text": item}, outfile)
        outfile.write('\n')

