###############################################################
## Input Diary is 5-7% in Romanian & Others ##
## This script assesses if text_Chunk is in any other than language and needs translation ##
## Then feeding the found out paragraphs chunks to LLM ##
## Finally, putting it all together into Translated_Data.jsonl - to be later used in PromptResponseDataset creation. ##
## Basically, it is seeking what text is not in english and feeding only the necessary identified non-english patterns
## To an LLM, greatly reducing cost of tokens ##
###############################################################
