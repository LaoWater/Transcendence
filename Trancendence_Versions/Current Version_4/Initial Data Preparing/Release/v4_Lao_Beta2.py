import re
from openai import OpenAI
import random

client = OpenAI()

prompt = 'What is Love? What is to fall in love?'

completion = client.chat.completions.create(
  model="ft:gpt-4o-mini-2024-07-18:personal::AAh0b7Uy:ckpt-step-934",
  messages=[
    {"role": "system", "content": ""},
    {"role": "user", "content": "What is Love? What is to fall in love?"}
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
print("Lao Beta 2:")
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

