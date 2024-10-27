###########################################################################
###########################################################################
# Lao Beta #3 Was trained on medium-size Dataset of medium Quality - #
# This is a checkpoint #1 at 3/3 of training, Loss has increased from checkping 2/3 to 3/3,
# This model seems to have scurtcircuited the pre-training setup, perhaps because the data is yet not clean and structured well enough.
# Lao Beta #3 is almost always in complete hallucination.

import re
from openai import OpenAI
import random

client = OpenAI()

prompt = ("""
Read conversation carefully and slowly, studying it's tokens and arrangements as character Lao speaks.

Read it several times in different chunks so you can truly immerse into this characters "neural networks definitions".

Then, continue conversation.

CONTINUE CONVERSATION FULLY ONLY IN LAO CHARACTER AS HE WOULD NATURALLY CONTINUE TYPING:

Conversation:
[And it's not a short term, It's been 2 years since I start doing my investment. 24.91% for 2 years, which means about 12% yearly.
It's much more than the bank deposite rate which is less than 2 % yearly.

But last year, when the return rate for stock is about -12%, there was stress causing by the mind.
Then gradually it become balanced, and grow up to positive now. 
Because those 2 stock which give me more than 100% profit, they grow so much this year.

No. 2227 stock -39% is Car company
No. 6751 stock -49% is Internet service industry
Those 2 was the almost dying tree that I plant... 😮‍💨 

No. 2360 stock  132% is a company related to Chip Industry
No. 2467 stock  110% is a company related to "Robot" Industry
Those 2 industry have lots of good news this year, so the price grows a lot and bring my balance sheet to positive now!]

""")




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

