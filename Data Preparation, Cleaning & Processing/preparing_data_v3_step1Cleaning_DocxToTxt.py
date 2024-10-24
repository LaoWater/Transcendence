import docx


def clean_diary(input_path, output_path):
    # Load the .docx file
    doc = docx.Document(input_path)
    cleaned_text = []
    current_text = []

    # Read each paragraph in the document
    for para in doc.paragraphs:
        text = para.text
        if text:
            current_text.append(text)
        elif current_text:  # Encountering a new line, process the accumulated text
            # Join the non-empty lines of current text into a single string with a newline
            combined_text = '\n'.join(current_text)
            cleaned_text.append(combined_text)
            current_text = []  # Reset for the next block of text

    # To ensure the last block is added if the document does not end with an empty line
    if current_text:
        combined_text = '\n'.join(current_text)
        cleaned_text.append(combined_text)

    # Join different blocks with double newlines to maintain clear separation
    cleaned_output = '\n\n'.join(cleaned_text)

    # Save the cleaned text to a .txt file
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(cleaned_output)


#####################################
#### Cleaning & Processing Diary ####
#####################################

clean_diary(r'Data\Diary_Full.docx', r'Data\v3_step1_cleaned_diary.txt')
