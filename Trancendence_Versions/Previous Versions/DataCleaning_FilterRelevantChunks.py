#####################################
### Diary.docx was transformed in previous versions in .jsonl ###
### Each paragraph from the Main Document has been transformed into a json object - in full_training_data_original.jsonl ###
### In this script we are transforming it from paragraphs format into a structured LLM dataset ###
### This is because in this context, there is no use for un-supervised learning ###
### For what we're trying to achieve, we'll explore 3 methods: Trained for: Prompt Generation, Role-base Conversation
### and Sentiment Analysis. (+possibly others)
### Therefore, before beginning any training, we need to properly create the datasets.
#####################################
from openai import OpenAI
import json
import os


# Function to generate a prompt using OpenAI
# Gpt 4-o-mini seems a lot cheaper than GPT 3.5 and performing better

def generate_prompt(paragraph):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """You are an assistant to an AI team, working on training an LLM based on a deep, 
                vast diary entry of a great Healer and intimate student of the intricacies of life.
                You will be fed one paragraph at a time.
                Later, the qualified paragraphs will be used to create a Training Dataset.
                
                For example, "sold car today" - is a short/ vague entry with no higher dimensions of lessons & takeaways 
                Basically Ponder if the entry can be used it on the broader spectrum of taking out a lesson from there 
                - and not extraordinarily specific to One.
                *And Decide if the fed message qualifies or not for the Greater training dataset.*
                If no lesson - return "ToBeRemoved"
                If great lesson - kindly format & grammatically correct.
                If mild/moderate lesson - adjust it keeping the same sentiment, you are free to add some modifications 
                to this category if you comprehend the greater sentiment.
         
         
            We'll later feed this again into an LLM - to read and generate a prompt
            (Because we'll be using a Supervised PromptResponse training method)
             You will return STRICTLY either "ToBeRemoved" which we'll later handle
             OR the *paragraph* to be appended to main list - OR paragraph slightly modified so it falls into the
             discussed context.
             
             Rather modify content so that a proper question/topic is assigned rather than removing it.
             Removal rate should be less than 1-2%.
             
            Don't return any additional text"""
            },
            {
                "role": "user",
                "content": f"Paragraph to analyze & process & filter: '{paragraph}'"
            }
        ]
    )

    response_text = response.choices[0].message.content
    return response_text


#######################
#### Script Begins ####
#######################

# Initialize the OpenAI client with your API key
client = OpenAI()
print(client)

# Preparing results files to read
working_dir = os.getcwd()
file_path_origin = os.path.join(working_dir, r'full_translated_data.jsonl')

# Read the JSONL results from the specified full path
diary_entries_split = []
data_counter = 0
with open(file_path_origin, 'r') as file:
    for line in file:
        json_obj = json.loads(line)
        diary_entries_split.append(json_obj['text'])
        if data_counter >= 25:
            break
        data_counter += 1

print("Generating script...")

# Generate prompts and structure the data
data = []
count = 1
for entry in diary_entries_split:
    print(f"Parsing entry number {count} ...")
    prompt = generate_prompt(entry)
    data.append({
        "filtered": prompt,
        "original_entry": entry
    })
    count += 1

# Save the structured data into a JSON file
with open('DataCleaning_AIFilteredChunks.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Data has been saved to DataCleaning_AIFilteredChunks.json")

for _ in range(10):
    print(diary_entries_split[_])
    print('\n')
