import docx


def clean_diary(input_path, output_path):
    # Load the .docx file
    doc = docx.Document(input_path)
    entries = []  # Store the final entries (groups of paragraphs)
    current_entry = []  # Temporarily store paragraphs for the current entry

    # Iterate through all paragraphs in the document
    for para in doc.paragraphs:
        text = para.text.strip()  # Strip leading/trailing whitespace
        if text:
            current_entry.append(text)  # Add non-empty paragraph to the current entry
        else:
            if current_entry:
                # When encountering an empty line, finalize the current entry
                entries.append('\n'.join(current_entry))
                current_entry = []  # Reset for the next entry

    # Ensure the last entry is added if the document doesn't end with an empty line
    if current_entry:
        entries.append('\n'.join(current_entry))

    # Join all entries with a newline separator (indicating a new entry)
    full_text = '\n\n'.join(entries)

    # Save the cleaned text to a .txt file
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(full_text)

    return full_text  # Optionally return the cleaned text for further use


#####################################
#### Cleaning & Processing Diary ####
#####################################

clean_diary(r'Data\Diary_Full.docx', r'Data\v4_step1_cleaned_diary.txt')
