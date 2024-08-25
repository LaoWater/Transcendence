###############
## Version 1 ##
###############
Version 1 of Transcendence ended in complete hallucination of LLM after feeding standardly processed diary in .json
Also, at this point, there are not free to use big performing models.

###############
## Version 3 ##
###############
Version 2, started to look into LLMs, took llama 3.1 and broke it down up to reviewing weights, config, forward passes.
Installed locally through 3rd party ollama - reached training bottle neck.
Then downloaded official model files - RAW NN files - not compatible with torch, transformers frameworks.

Finally, used hugging face, but reached a new type of bottle new of the model taking 2+ minutes per response using CUDA
Time to move to version 3.

###############
## Version 3 ##
###############
In version 3 i want to first prepare the data set accordingly, no matter of what LLM we'll use.
Split whole text as per paragraphs - so that the ideas make sense.
Translate all to english.

Get it all of json form as:
"{"text": "Still, i pushed myself to actually do some of the things i was masturbating about She pissed in my mouth I was absolutely disgusted I came out with the revelation that for the pleasure to be real, the suffering must be real Me being absolutely crazy attracted by her energy and feminity and she - taking great pleasure in my suffering Love.. and it being denied in the most glorious ways The pattern for love i've written in my childhood The shadow"}
{"text": "In time, as i worked on myself and dating, i started attracting more high-quality women and in which arms i would feel a different kind of love The other type of love my mother showed me as a child, her being very pshisically close to me, nurtuing, loving But sexually, experiences were just as empty as the ones before This autumn, the shadow was so powerful that the fantasies could easily derail to being about me actually dying for \"her\" pleasure"}"

Next, think about dataset Architecture.

We'll try a few more

1. Role-Based Conversation Format 
## Dataset to be used: ConversationalDataset
*Develop or fine-tune a model for interactive, context-sensitive dialogues, where the model needs to respond based on the flow of a conversation.*

2. Prompt/Generated Text Format
## Dataset to be used: PromptResponseDataset
*train the model for generating specific types of content based on given prompts or instructions, without the need for extended interaction or dialogue management.*

3. Sentiment Analysis Dataset
## Dataset to be used: SentimentDataset
*train the model to understand and generate text with a particular emotional tone.*

-------------------------------

For all scenarios - diary entries must be translated & formatted in paragraphs.
Then fed into a LLM for

1. Generate content for role(user) and use diary for content (assistant) 
[
    {
        "role": "user",
        "content": "Explain the concept of physical depreciation in real estate."
    },
    {
        "role": "assistant",
        "content": "Physical depreciation refers to the gradual wear and tear on a property over time..."
    }
]

2. Generate According prompts to be used in Dataset Creation
[
    {
        "prompt": "Natural Truths",
        "generated_text": "Today I reflected on the importance of natural truths."
    }
]

