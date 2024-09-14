import os
import json
import time
import openai
from openai import OpenAI
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def is_prompt_similar(new_prompt, existing_prompts, threshold=0.8):
    if not existing_prompts:
        return False  # No prompts to compare with
    vectorizer = TfidfVectorizer().fit_transform([new_prompt] + existing_prompts)
    vectors = vectorizer.toarray()
    cosine_matrix = cosine_similarity(vectors)
    # Compare the new prompt with each existing prompt
    similarities = cosine_matrix[0, 1:]
    return any(sim >= threshold for sim in similarities)


# Read the categorized diary data
input_file_path = 'Data/v3_step4_categorized_diary.json'
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    categorized_entries = json.load(input_file)


def generate_prompt_content(chunk_category, chunk, model="gpt-4o-mini", temperature=0.8):
    client = OpenAI()
    messages = [
        {
            "role": "system",
            "content": "You are a creative assistant that generates prompts based on provided text & text category."
                       "Take the time to properly set the category before reading and before generating prompt."
                       "The promps should be clear and precise, they are going to be used in a PrompGenerated Dataset"
                       "Used for LLM training."
        },
        {
            "role": "user",
            "content": f"""
Using the following category and text, create an imagination-inviting prompt of 3 to 20 words that reflects the 
sentiment of the category and is relevant to the text. The prompt should not be too specific and should 
encourage creative thinking.

**Important Instructions:**
- Return only the JSON object and nothing else.
- Do **not** include any code block markers (e.g., triple backticks) or language identifiers.
- Ensure the JSON is properly formatted, using double quotes for strings.
- Strings must be enclosed in double quotes (`"`).
- Do not use triple quotes or single quotes.
- Escape any special characters as needed.
- Do not include any explanations or additional text.

Category: {chunk_category}

Text:
\"\"\"{chunk}\"\"\"

Return the result in JSON format:
{{"prompt": "Generated prompt", "content": "Original text chunk"}}
"""
        }
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=777
    )

    response_text = response.choices[0].message.content

    # Parse the JSON output
    try:
        generated_result = json.loads(response_text)
    except json.JSONDecodeError:
        # If parsing fails, print the error and assistant's response for debugging
        print(f"JSON decoding error: {json.JSONDecodeError}")
        print(f"While processing chunk with category '{chunk_category}'")
        print(f"Assistant's response:\n{response_text}")
        generated_result = None

    except Exception as e:
        # Handle other exceptions
        print(f"An error occurred: {e}")
        generated_result = None

    return generated_result


prompt_content_pairs = []

for idx, entry in enumerate(categorized_entries):
    category = entry.get('category')
    chunk_text = entry.get('chunk')

    if not chunk_text or not category:
        continue  # Skip if missing data

    if category != "Uncertain":
        print(f"Processing entry {idx + 1}/{len(categorized_entries)}")

        result = generate_prompt_content(category, chunk_text)
        if result:
            prompt_content_pairs.append(result)
        else:
            print(f"Failed to generate prompt-content pair for entry {idx + 1}")
    else:
        print(f"Skipping entry {idx + 1}/{len(categorized_entries)} (Disregarded)")

    time.sleep(1)  # Adjust as needed to respect rate limits


def clean_text(text):
    return ' '.join(text.strip().split())


output_file_path = 'Data/v3_step5_creating_prompt_content_pairs.jsonl'

with open(output_file_path, 'w', encoding='utf-8') as file:
    for pair in prompt_content_pairs:
        prompt = clean_text(pair['prompt'])
        content = clean_text(pair['content'])
        data = {
            "prompt": prompt,
            "content": content
        }
        file.write(json.dumps(data) + '\n')

print(f"Prompt-content pairs have been saved to {output_file_path}")

print("All generated prompts for review before creating Final DataSet:")
for pair in prompt_content_pairs:
    prompt = clean_text(pair['prompt'])
    print(f"Prompt: {prompt}")
