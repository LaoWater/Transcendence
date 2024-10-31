###########################################################################
###########################################################################
# Lao Beta #2 Was trained on medium-size Dataset of medium Quality - #
# This is a checkpoint #1 at 2/3 of training,
# Where we have touched a sweetspot between Pre-training data and training data
# Lao's touch is being felt clearly, yet not to a point where the binding of the pre-train with training becomes stainde and overwhelming for the LLM.
# Most stable Model yet and producer of Marvelling asnwers worthy of labeling them as "Complete Transcendence"
# That is when the Model produces something similar or better than the writer itself, although using different words, expressions and styles of "painting", but springing from a similar "Neural Network".


import re
from openai import OpenAI
import random

client = OpenAI()

prompt = """
Study below text and continue writing about the 4th phase of Learning.'

The Art of Learning has 3 main stages of Alchemy

I. The First Learning,
II. The Second Learning,
III. The Third Learning,

and one final Form of a Teaching:
IV. Spontaneous Birthing in Greatness when needed 
& continuous development using the first 3 dhammas.

The Art of Learning can enhance up to 10x One’s Learning Rate 
and Transferability of Skill to the Real World.
It is Alchemizing the dhamma in front of one with Faith, Purpose, Vision, Wisdom and Wisdom in Action.

There are, of course, other ways to Learn, just as there are many 
ways to Move, To Eat, to Live.
But we are Students of the Art of Life, emerging from a intimate, inter-connected meeting of all Life’s Arts, each requiring immense sufferings, sincere effort and dedication to unveil.
The Art of Breathing,
The Art of Eating,
The Art of Moving,
Lay the Foundation.

Today we study The Art of Learning.

/*****************************************************************************/

I. The First Learning: The Scholar
In the First Learning, One engages with the lesson as a Scholar – a first contact with the Teaching, stepping into the space where curiosity and discovery take precedence.
This initial engagement brings a fresh sense of observation, yet it moves with shallow neural activations, looking to make high-level connections.

The Scholar seeks to bridge these connections with known experiences and past learnings, using high-level neural pathways that remain exploratory and wide, yet underdeveloped.
Here, bottlenecks may arise as the Scholar reaches the edges of their current logistical, theory or real-world application understanding, restrained by the unknown and gaps in experience.

At this stage, the learning feels like an open field, one where the Scholar’s pen and mind move freely, alternating between the core material and the spontaneous high-level connections that emerge.

The Scholar remains rooted in One Question:
What skill, what dhamma, is One seeking to develop, and in what dimensions is it to be measured?

These insights emerge as the foundation of a multi-dimensional approach, where learning extends beyond itself and into all realms.
This is the "Scholar" step of the "Scholar Athlete" archetype.
The "Pen in one hand" from the "Warrior Monk with the Pen in one hand and the Blade in another" archetype.

/*****************************************************************************/

II. The Second Learning: Deep Integration & Usability across all “I”’s

CS50: Optimization - The Second Learning ~ [27-Oct-2024]
The Second Learning happened this night, as One sits down a second time in front of the Lesson, this time with the Pen & Paper in hand – and truly scrutinizes the teachings on low levels, allowing spontaneous ramifications of where God takes us, from one lesson to another.
The 3am-6am window, clear stomach, beautiful sleep and deeply Cleaned Dojo allows for the Clear Mind to completely Rise.

In the Second Learning, the neural paths reach a much higher depth and ease of accessibility for the Mind.
Even here, the high-level Sentiment is Code Re-usability.
Formatting the learned patterns in ways that can be easily accessible by other Gateways of writings, projects, videos, photos.
The Re-usability of the learned concept, code, and dhammas extends into all areas, not limited to Neo – but going further into the Builder, the Writer, The Healer.

In Unity, when One Learns, We all Learn.


/*****************************************************************************/


III. The Third Learning: The Dojo's Doors Open Towards the Battlefield

One gracefully puts down the warm pen and closes the book, heading into the Real World.
He first nourishes his body – the Fighter – in all realms.

Then he begins practicing what he had studied on top of his pre-trained (life-story) Alchemies.
There is no clinging to any outcomes, nor are there any emotions affecting the efficiency of the Fighting Beast.

Like a samurai walking the battlefield, he uses all of his senses to his advantage.
But he is always in the present – never lost in unnecessary predictions.

The Samurai's mind is not predicting from where the opponent might strike, therefore losing present-moment contact with all the senses.
So that when a true opponent appears, the Mind must first travel back to the present from its predictions and only from there React.
But rather, he remains deeply rooted in the present.
The Clear Mind in a Strong, Connected, Water-Flowing body allows the Mind to react at the speed of light (neural electricity) to the ever-changing inputs from the senses.

He fights with all his heart – for all his brothers he left at home, for dreams, for Freedom, for the work of God on this Earth, and the chance to be His soldier.
He does not abandon the battle in fearful sentiments, but rather Retires to the warm Dojo after the battle is won or the Beast is tired.

Inside the Dojo walls, he hangs his blade on the wall and allows the Beast to Rest.
The "I" learning the dhammas has completely played its part.
Now it is time to Die and be Born again when it is needed – Stronger, Faster, Wiser.

The Warrior Monk sleeps, as billions of neural patterns fire across the Realms of Theory and Experience inside his Mind - automatically seeking to converge the 2 Realms.
“Blessed are you, Lord our God, King of the Universe, for giving me the strength to Fight and Wisdom to Learn.”

"""



def comparing_to_base_model(completion_p):
    completion_p = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": ""},
            {"role": "user", "content": "What is the fine line between the mine interfering with the body "
                                        "and guiding it towards healthful, mindful, blessed eating?"}
        ]
    )

    print("\n\n\nBase Model:")
    print(completion_p.choices[0].message.content)


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



prompt_2 = ("advise One on when is the body(beast) hungry and when is the Mind")

completion = client.chat.completions.create(
    model="ft:gpt-4o-mini-2024-07-18:personal::AAh0b7Uy:ckpt-step-934",
    messages=[
        {"role": "system",
         "content": "You are Lao, a student of Life who has searched for understanding of the Body, Mind "
                    "And Soul - all his Life. "
                    "Has traveled the world and oceans, deeply immersed in cultures in both study"
                    "and practice, love, habits of the body, Mind and Soul."
                    "He returns home to spread his teachings with his fellow brothers, in "
                    "Truth Discerning awareness, wise but yet not speaking as if he is better than others."},
        {"role": "user", "content": prompt_2}
    ],
    temperature=0.7,  # Controls creativity; 0 is deterministic
    top_p=0.9,  # Controls diversity; higher means more varied completions
    max_tokens=500,  # Limits the length of the response
    frequency_penalty=0.0,  # Penalizes frequent words
    presence_penalty=0.6  # Encourages topic diversity
)

completion_content = completion.choices[0].message.content

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

print("Base Moodel: ")
comparing_to_base_model(prompt_2)
