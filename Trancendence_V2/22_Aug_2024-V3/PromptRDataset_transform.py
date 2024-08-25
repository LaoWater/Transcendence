#####################################
### Diary.docx was transformed in previous versions in .jsonl ###
### Each paragraph from the Main Document has been transformed into a json object - in training_data_original.jsonl ###
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
                "content": """You are an assistant that generates concise prompts for given text.
We are training a LLM based on a provided diary text.
Each text is fed from a greater diary text.
-------------------------------------------------------
We are creating prompts to facilitate this training.
The purpose is to create PromptResponseDataset in the form of (prompt-generated text) - to later train an LLM.
So consider this when generating a prompt.
ideally, you would use short-medium concise prompts which serve as a summary of the input paragraph.
A good prompt would be ~Explain the concepts of Natural Truth in Holistic Health.~
Or ~Digestive system health connection to the Mind.~
-----------------------------------
Do not use keyphrases like "diary entry", "diary" in your prompts - as this is ultimately going to be used
by our customers to discuss/understand Holistic Health Concepts from the LLM Fine-tuned to old man's Diary.
Neither use "Explore, Discuss" - but rather leave out the necessary words

Still, it should not micro-niche so hard into specific keywords from explored paragraph, 
but rather play around the greater summarization of it.


"""
            },
            {
                "role": "user",
                "content": f"Generate a prompt for the following text: '{paragraph}'"
            }
        ]
    )

    response_text = response.choices[0].message.content
    return response_text


#######################
#### Script Begins ####
#### See Readme.md ####
#######################

# Initialize the OpenAI client with your API key
client = OpenAI()
print(client)

# Preparing results files to read
working_dir = os.getcwd()
file_path_origin = os.path.join(working_dir, r'training_data.jsonl')

# Read the JSONL results from the specified full path
diary_entries_split = []
with open(file_path_origin, 'r') as file:
    for line in file:
        json_obj = json.loads(line)
        diary_entries_split.append(json_obj['text'])

print("Generating script...")

# Generate prompts and structure the data
data = []
count = 1
for entry in diary_entries_split:
    print(f"Parsing entry number {count} ...")
    prompt = generate_prompt(entry)
    data.append({
        "prompt": prompt,
        "generated_text": entry
    })
    count += 1

# Save the structured data into a JSON file
with open('PromptResponseDataset.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Data has been saved to PromptResponseDataset.json")

for _ in range(10):
    print(diary_entries_split[_])
    print('\n')
