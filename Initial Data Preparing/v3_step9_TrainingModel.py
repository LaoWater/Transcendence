from openai import OpenAI
client = OpenAI()
input_file_path = 'Data/v3_step6_formatted_for_OpenAI_finetuning.jsonl'
training_file = 'file-Z25f10JJZCG6WVPv5VzkROLF'


client.fine_tuning.jobs.create(
  training_file=training_file,
  model="gpt-4o-mini"
)


