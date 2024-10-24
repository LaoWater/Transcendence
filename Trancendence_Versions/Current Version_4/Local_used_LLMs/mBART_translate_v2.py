import torch
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

# Check CUDA availability
print("CUDA Version:", torch.version.cuda)
print("CUDA Available:", torch.cuda.is_available())

# Load the pre-trained mBART model and tokenizer for many-to-many machine translation
model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt").to('cuda' if torch.cuda.is_available() else 'cpu')
tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")

# Set the source language to Romanian and target language to English
tokenizer.src_lang = "ro_RO"  # Source language: Romanian

# Input text in Romanian
src_text = "Un guster sufla o ceapă la o margine de drum"  # Romanian sentence

# Tokenize the input and move to CUDA if available
encoded_input = tokenizer(src_text, return_tensors="pt").to('cuda' if torch.cuda.is_available() else 'cpu')

# Generate translation (force target language to English)
generated_output = model.generate(
    **encoded_input,
    forced_bos_token_id=tokenizer.lang_code_to_id["en_XX"],  # Target language: English
    max_length=50,  # Optional: limit max length of output
    num_beams=4,  # Optional: use beam search for better translation quality
    early_stopping=True  # Optional: stop early if the model is confident
)

# Decode the generated sequences to get the translated text
text_output = tokenizer.batch_decode(generated_output, skip_special_tokens=True)

# Print the translated output
print("Translated Text:", text_output[0])
