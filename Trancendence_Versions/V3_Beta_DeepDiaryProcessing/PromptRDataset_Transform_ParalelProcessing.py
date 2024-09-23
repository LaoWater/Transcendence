#!/usr/bin/env python3
import concurrent.futures
from openai import OpenAI
import json
import os
import threading


# Function to generate a prompt using GPT-3.5
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
by our customers to discuss/understand Holistic Health Concepts from the LLM Fine-tuned to old man's Diary

Still, it should not micro-niche so hard into specific keywords from explored paragraph, 
but rather play around the greater summarization of it
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


# Generate prompts and structure the data
def process_entry(entry_p):
    thread_name = threading.current_thread().name
    print(f"Thread {thread_name} starting processing entry.")

    prompt_p = generate_prompt(entry_p)

    print(f"Thread {thread_name} finished processing entry.")

    return {"prompt": prompt_p, "generated_text": entry_p}

#######################
#### Script Begins ####
#### See Readme.md ####
#######################

# Initialize the OpenAI client with your API key
client = OpenAI()
print(client)

# Preparing results files to read
working_dir = os.getcwd()
file_path_origin = os.path.join(working_dir, r'training_data_top30_forGPTtest.jsonl')

# Read the JSONL results from the specified full path
diary_entries_split = []
with open(file_path_origin, 'r') as file:
    for line in file:
        json_obj = json.loads(line)
        diary_entries_split.append(json_obj['text'])

print("Generating script...")


data = []

# Using ThreadPoolExecutor for parallel processing
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(process_entry, diary_entries_split))

data.extend(results)

# Save the structured data into a JSON file
with open('PromptResponseDataset_V1.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Data has been saved to PromptResponseDataset_V1.json")