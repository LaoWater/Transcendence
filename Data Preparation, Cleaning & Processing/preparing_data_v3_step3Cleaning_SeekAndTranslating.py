import json
import openai
from langdetect import detect, LangDetectException
from openai import OpenAI


# Function to check if the text is in English
def is_english(text):
    try:
        return detect(text) == 'en'
    except LangDetectException:
        print(f"Could not detect language for the text: {text[:50]}...")  # Print a portion of the text for context
        return False


# Function to translate text to English using GPT-3.5
def translate_to_english(text, model="gpt-4o-mini", temperature=0.7):
    client = OpenAI()
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": """You are a helpful assistant that translates text to English.
            Consider that language translation are incomplete and may often be lacking context understanding.
            You are free to read teh text and interpret it with medium temperature and make the necessary 
            changes/adjustments so that the broader understanding and art of writing is kept"""},

            {"role": "user", "content": f"Translate the following text to English:\n\n{text}"}
        ],
        temperature=temperature
    )

    response_text = response.choices[0].message.content
    return response_text


# Function to process the JSON data
def process_json_data(json_data):
    translated_entries = []

    for entry in json_data:
        text = entry['chunk']

        # Check if the text is in English
        if is_english(text):
            print("Detected English text. Adding to the translated entries.")
            print(text)
            print("\n\n")
            translated_entries.append(entry)  # Keep the original if it's in English
        else:
            print("Detected other language! Calling Translation LLM for text:")
            print(f"ORIGINAL TEXT:\n{text}\n")

            # Translate the text to English
            translated_text = translate_to_english(text)

            # Debugging notification after translation
            print("Translated text (after API call):")
            print(f"{translated_text}\n")

            # Append the translated text to the list
            translated_entries.append({'text': translated_text})

    return translated_entries


# Read the JSON data from the file
input_file_path = 'Data/v3_step2_cleaned_diary.json'
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    diary_json = json.load(input_file)

# Process the JSON data to translate non-English text
translated_json_data = process_json_data(diary_json)

# Save the translated JSON data to a new file
output_file_path = 'Data/v3_step3_translated_diary.json'
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(translated_json_data, output_file, indent=2)

print("Translated JSON data has been saved to", output_file_path)
