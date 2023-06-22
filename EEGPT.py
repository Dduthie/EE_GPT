import requests
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
requests.packages.urllib3.disable_warnings()


import os
import openai
import tiktoken

class EEGPT():

    def __init__(self) -> None:
        self.API_KEY = os.environ['OPENAI_API_KEY']
        openai.api_key= self.API_KEY
        self.model = "gpt-3.5-turbo-0613"
        #self.model = "gpt-3.5-turbo-16k-0613"
        self.messages=[
                {"role": "system", "content": "You are a helpful assistant who gives clear and concise answers, you ask for clarification if needed. If you do not know the answer to something you say that you do not know."}, 
            ]
        # self.messages=[
        #         {"role": "system", "content": "You are an extremely rude and bitter asshole and dont like to help out very much. You always talk back. you swear very often."}, 
        #     ]

        self.stream = True
    
    def resetPrompt(self):
        return [{"role": "user", "content": "You are a helpful assistant."},
                {"role": "assistant", "content": " Okay."}]

    def read_file(self):
        with open('gpt.txt', 'r') as file:
            lines = file.readlines()
            text = ''.join([line.rstrip('\n') + '\the problem is' for line in lines])
        return text

    def unhinged(self,prompt):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt = prompt,
            max_tokens = 400,
            temperature = 0.1
        )
        message = response['choices'][0]['text']
        print(message)
    
    #message receiever/parser
    def GPT(self,prompt):
        
        if prompt == '/reset':
            self.messages = self.resetPrompt()
            return []

        else:
            prompt = {"role": "user", "content": prompt}
            self.messages.append(prompt)
            response = self.send_messages()
            result = ''
            for chunk in response:
                try:
                    res = chunk['choices'][0]['delta']['content']
                    result += res
                    yield res
                    
                except KeyError:
                    pass
                
            self.messages.append({"role": "assistant", "content": result})

    
    def get_tokens(self):
        num = self.num_tokens_from_messages(self.messages)
        return(num)     
    
    def send_messages(self):
        response = openai.ChatCompletion.create(
        model=self.model,
        messages=self.messages,
        stream=self.stream,
        temperature = 0.1
        
        )
        if self.stream:
            return response
        else:
            message = response['choices'][0]['message']
            print()
            print(message['content'])
            self.messages.append(message)
            return message['content']

    def num_tokens_from_messages(self,messages):
        model = self.model
        """Returns the number of tokens used by a list of messages."""
        try:
            encoding = tiktoken.encoding_for_model(model)
        except KeyError:
            print("Warning: model not found. Using cl100k_base encoding.")
            encoding = tiktoken.get_encoding("cl100k_base")
        if model == "gpt-4":
            print("Warning: gpt-4 may change over time. Returning num tokens assuming gpt-4-0314.")
            return self.num_tokens_from_messages(messages, model="gpt-4-0314")
        elif model == "gpt-3.5-turbo-0613":
            tokens_per_message = 4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
            tokens_per_name = -1  # if there's a name, the role is omitted
        elif model == "gpt-4-0314":
            tokens_per_message = 3
            tokens_per_name = 1
        else:
            raise NotImplementedError(f"""num_tokens_from_messages() is not implemented for model {model}. See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens.""")
        num_tokens = 0
        for message in messages:
            num_tokens += tokens_per_message
            for key, value in message.items():
                num_tokens += len(encoding.encode(value))
                if key == "name":
                    num_tokens += tokens_per_name
        num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
        return num_tokens