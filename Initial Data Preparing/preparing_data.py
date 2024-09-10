import pypandoc
import re
import json


def clean_text(text):
    # Remove multiple spaces and newlines
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def extract_text_from_docx(filepath):
    try:
        output = pypandoc.convert_file(filepath, 'plain')
        return output
    except Exception as e:
        print(f"Failed to extract text from {filepath}. Ensure the file exists and is a valid .docx file.")
        raise e


def split_into_chunks(text, max_length=512):
    sentences = text.split('. ')
    chunks_all = []
    current_chunk = []

    for sentence in sentences:
        if len(' '.join(current_chunk + [sentence])) <= max_length:
            current_chunk.append(sentence)
        else:
            chunks_all.append(' '.join(current_chunk))
            current_chunk = [sentence]

    if current_chunk:
        chunks_all.append(' '.join(current_chunk))

    return chunks_all


# Replace 'diary.docx' with the path to your .docx file
file_path = r'Data\diary.docx'
try:
    diary_text = extract_text_from_docx(file_path)
except Exception as e:
    print(f"Error processing file: {e}")
    exit()

#####################################
#### Cleaning & Processing Diary ####
#####################################

cleaned_diary_text = clean_text(diary_text)

# Split the cleaned text into chunks
chunks = split_into_chunks(cleaned_diary_text)

# Save the cleaned text to a plain text file
output_cleaned_text_path = 'Data\v1_cleaned_diary.txt'
try:
    with open(output_cleaned_text_path, 'w', encoding='utf-8') as f:
        f.write(cleaned_diary_text)
    print(f"Cleaned text successfully saved to {output_cleaned_text_path}")
except Exception as e:
    print(f"Failed to save cleaned text to {output_cleaned_text_path}: {e}")

# Create JSON objects for each chunk
training_data = [{"text": chunk} for chunk in chunks]

# Write the JSON objects to a JSONL file
output_jsonl_path = 'Data\training_data.jsonl'
with open(output_jsonl_path, 'w', encoding='utf-8') as f:
    for entry in training_data:
        json.dump(entry, f)
        f.write('\n')

print(f"Training data successfully saved to {output_jsonl_path}")
