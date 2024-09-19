from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="ft:gpt-4o-mini-2024-07-18:personal::A8phTRw2",
  messages=[
    {"role": "system", "content": ""},
    {"role": "user", "content": "What foods bring you comfort during tough times?"}
  ]
)

print("Trained Model:")
print(completion.choices[0].message.content)


####################################
## Comparing to Normal Base Model ##
####################################

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": ""},
    {"role": "user", "content": "What foods bring you comfort during tough times?"}
  ]
)

print("\n\n\nBase Model:")
print(completion.choices[0].message.content)

