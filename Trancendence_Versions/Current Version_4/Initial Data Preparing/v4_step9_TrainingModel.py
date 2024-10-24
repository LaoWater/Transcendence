from openai import OpenAI
client = OpenAI()
input_file_path = 'Data/v4_step6_formatted_for_OpenAI_finetuning.jsonl'
training_file = 'file-73CPKdHZCiBTrblb9rWQxNZZ'


client.fine_tuning.jobs.create(
  training_file=training_file,
  model="gpt-4o-mini-2024-07-18"
)


