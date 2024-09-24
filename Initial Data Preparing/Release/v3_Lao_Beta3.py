import re
from openai import OpenAI
import random

client = OpenAI()

prompt = ('Give me some advice on how to approach working on something which needs to be done but it'
          'is overwhelming and the Mind wants to keep postponing it')

completion = client.chat.completions.create(
  model="ft:gpt-4o-mini-2024-07-18:personal::AAh0bCFk",
  messages=[
    {"role": "system", "content": "You are Lao, a Healer and philosopher - but most of all,"
                                  "A humble student of life, sharing his experiences and lessons."},
    {"role": "user", "content": f"{prompt}"}
  ]
)

print(f"Q: {prompt} \n")
# Assuming the LLM's output is in completion.choices[0].message.content
completion_content = completion.choices[0].message.content


# Function to split text after every 2-3 punctuation marks
def split_into_paragraphs(text):
    # Regex pattern to match punctuation marks (., ?, !)
    sentences = re.split(r'([.!?])', text)

    paragraphs_processing = []
    temp_paragraph = ""
    count = 0

    for i in range(0, len(sentences) - 1, 2):  # iterate over sentences with punctuation
        temp_paragraph += sentences[i] + sentences[i + 1]  # Combine sentence and punctuation
        count += 1

        if count >= random.randint(2, 3):  # Randomly decide between 2 or 3 punctuation marks
            paragraphs_processing.append(temp_paragraph.strip())  # Add paragraph
            temp_paragraph = ""
            count = 0

    if temp_paragraph:
        paragraphs_processing.append(temp_paragraph.strip())  # Add the last paragraph if not empty

    return paragraphs_processing


# Generate paragraphs
paragraphs = split_into_paragraphs(completion_content)

# Print each paragraph
print("Lao Beta 3:")
for paragraph in paragraphs:
    print(paragraph)
    print()  # Adds a blank line between paragraphs


####################################
## Comparing to Normal Base Model ##
####################################

exit()

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": ""},
    {"role": "user", "content": "What is the fine line between the mine interfering with the body "
                                "and guiding it towards healthful, mindful, blessed eating?"}
  ]
)

print("\n\n\nBase Model:")
print(completion.choices[0].message.content)

