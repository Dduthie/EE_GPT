import requests
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
requests.packages.urllib3.disable_warnings()


import os
import openai
import tiktoken



API_KEY = os.environ['OPENAI_API_KEY']

openai.api_key= API_KEY

model = "gpt-3.5-turbo"

def resetPrompt():
    return [{"role": "user", "content": "You are a helpful assistant."},
            {"role": "assistant", "content": "Okay."}]

messages=[
        {"role": "system", "content": "You are a helpful assistant."},
    ]

def read_file():
    with open('gpt.txt', 'r') as file:
        lines = file.readlines()
        text = ''.join([line.rstrip('\n') + '\the problem is' for line in lines])
    return text

def unhinged(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt = prompt,
        max_tokens = 400,
        temperature = 0.1
    )
    message = response['choices'][0]['text']
    print(message)

def send_messages():
        response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        
        )
        message = response['choices'][0]['message']
        print()
        print(message['content'])
        messages.append(message)

#{"role": "user", "content": "You are a helpful assistant."}
print('\n\n')
while True:

    prompt = input("> ")
    if prompt == 'end':
        break
    elif prompt == 'reset':
        messages = resetPrompt()
        
    elif prompt == 'swap':
        if model == 'gpt-4-0314':
            model = "gpt-3.5-turbo"
        elif model == "gpt-3.5-turbo":
            model = 'gpt-4-0314'
        print('switching to: ' + model)
        
    elif prompt == 'read': 
        prompt = {"role": "user", "content": read_file()}
        messages.append(prompt)
        send_messages()
    elif prompt == 'unhinged':
        prompt = input("> ")
        unhinged(prompt)
    else:
        prompt = {"role": "user", "content": prompt}
        messages.append(prompt)
        send_messages()
        
    print()




def num_tokens_from_messages(messages, model="gpt-3.5-turbo-0301"):
  """Returns the number of tokens used by a list of messages."""
  try:
      encoding = tiktoken.encoding_for_model(model)
  except KeyError:
      encoding = tiktoken.get_encoding("cl100k_base")
  if model == "gpt-3.5-turbo-0301":  # note: future models may deviate from this
      num_tokens = 0
      for message in messages:
          num_tokens += 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
          for key, value in message.items():
              num_tokens += len(encoding.encode(value))
              if key == "name":  # if there's a name, the role is omitted
                  num_tokens += -1  # role is always required and always 1 token
      num_tokens += 2  # every reply is primed with <im_start>assistant
      return num_tokens
  else:
      raise NotImplementedError(f"""num_tokens_from_messages() is not presently implemented for model {model}.
  See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens.""")