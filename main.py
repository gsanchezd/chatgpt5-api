import os
import sys
from openai import OpenAI

if len(sys.argv) < 3:
  print("Usage: python main.py <your input> <output_file>")
  sys.exit(1)

user_input = sys.argv[1]
output_file = sys.argv[2]

client = OpenAI()

response = client.responses.create(
  model="gpt-5",
  input=user_input,
  text={
    "verbosity": "high"
  }
)

# Write to markdown file
with open(output_file, 'w') as f:
    f.write(response.output[1].content[0].text)

print(f"Response saved to {output_file}")