import pickle
from typing import List, Dict

class Conversation:
    def __init__(self, conversation_id: int):
        self.id: int = conversation_id
        self.GPTmessages: List[str] = []
        self.html: str = ""
        self.state: int = 0

    def addSystem(self, chat: str):
        self.GPTmessages.append({"role": "system", "content": chat})

    def addUser(self, chat: str):
        self.GPTmessages.append({"role": "user", "content": chat})

    def addGPT(self, chat: str):
        self.GPTmessages.append({"role": "assistant", "content": chat})

class ConversationManager:
    def __init__(self, conversations: Dict[int, Conversation] = None):
        self.currentConversation: int = 0
        self.conversations: Dict[int, Conversation] = conversations or {}

        self.promptManager = PromptManager()
        newConvo = Conversation(0)
        newConvo.addSystem(self.promptManager.getSelectedPrompt())
        self.conversations[0] = newConvo

    def exportConvo(self):
        convo = self.conversations[self.currentConversation]
        export = []
        for line in convo.GPTmessages:
            export.append(line['role']+": " +line['content']+'\n\n')
        return export
    
    def resetConvo(self):
        currentMessages = self.conversations[self.currentConversation].GPTmessages
        self.conversations[self.currentConversation].GPTmessages = currentMessages[:1]

    def getCurrentConversationID(self):
        return self.currentConversation

    def getCurrentConversation(self):
        return self.conversations[self.currentConversation].GPTmessages

    def getCurrentHTML(self):
        return self.conversations[self.currentConversation].html

    def addUserChat(self, chat: str):
        self.conversations[self.currentConversation].addUser(chat)

    def addGPTChat(self, chat: str):
        self.conversations[self.currentConversation].addGPT(chat)

    def addConversation(self, oldMessage: str):
        self.conversations[self.currentConversation].html = oldMessage
        newConvoId = self.__getNewConversationId()
        self.currentConversation = newConvoId
        newConvo = Conversation(newConvoId)
        self.conversations[newConvoId] = newConvo
        selectedPrompt = self.promptManager.getSelectedPrompt()
        newConvo.addSystem(selectedPrompt)

    def changeConversation(self, convoId: int,oldMessage):
        self.conversations[self.currentConversation].html = oldMessage
        self.currentConversation = convoId
        print(f"Changed conversation to {convoId}")

    def removeConversation(self):
        if len(self.conversations) == 1 or self.currentConversation == 0:
            self.resetConvo()
            return
        else:
            del self.conversations[self.currentConversation]
            self.__updateConversationsIds()
            self.currentConversation -= 1

    def saveConversation(self,filename:str,html):
        conversation = self.conversations[self.currentConversation]
        conversation.html = html
        try:
            with open(filename, "wb") as file:
                pickle.dump(conversation, file)
            print(f"Conversation saved.")
        except FileNotFoundError:
            print(f"Error: Conversation could not be saved.")


    def saveAllConversations(self):
        for convoId, conversation in self.conversations.items():
            try:
                with open(f"conversation_{convoId}.pickle", "wb") as file:
                    pickle.dump(conversation, file)
                print(f"Conversation {convoId} saved.")
            except FileNotFoundError:
                print(f"Error: Conversation {convoId} could not be saved.")

    def loadConversation(self,filename,oldHTML,loadMultiple=False):
        if loadMultiple: 
            for name in filename:
                try:
                    with open(name, "rb") as file:
                        conversation = pickle.load(file)
                        print("conversation loaded from file.")
                        self.__loadConversation(oldHTML,conversation)
                except FileNotFoundError:
                    print("No conversation loaded.")
        else:
            try:
                with open(filename, "rb") as file:
                    conversation = pickle.load(file)
                    print("conversation loaded from file.")
                    print(conversation.html)
                    self.__loadConversation(oldHTML,conversation)
                    
            except FileNotFoundError:
                print("No conversation loaded.")

    def addPrompt(self, prompt: str):
        self.promptManager.addPrompt(prompt)
        print("Prompt added.")

    def removePrompt(self, prompt: str):
        self.promptManager.removePrompt(prompt)
        print("Prompt removed.")

    def getAllPrompts(self):
        return self.promptManager.getAllPrompts()

    def selectPrompt(self, prompt: str):
        self.promptManager.selectPrompt(prompt)
        print("Prompt selected.")
        # Load the selected prompt into the current conversation
        currentConvo = self.conversations[self.currentConversation]
        currentConvo.GPTmessages = [prompt]

    def getSelectedPrompt(self):
        return self.promptManager.getSelectedPrompt()

    def getHTML(self):
        return self.conversations[self.currentConversation].html

    def __getNewConversationId(self):
        if not self.conversations:
            return 1
        return max(self.conversations.keys()) + 1

    def __updateConversationsIds(self):
        updatedConversations = {}
        newId = 0
        for convoId, conversation in self.conversations.items():
            updatedConversations[newId] = conversation
            newId += 1
        self.conversations = updatedConversations

    def __loadConversation(self,oldConvo,convo):
        self.conversations[self.currentConversation].html = oldConvo
        newConvoId = self.__getNewConversationId()
        self.currentConversation = newConvoId
        self.conversations[newConvoId] = convo


        
class PromptManager:
    def __init__(self):
        self.prompts: List[str] = []
        self.selectedPrompt: int = 0
        self.startUpPrompt()

    def startUpPrompt(self):
        try:
            with open('Pstart.pkl', "rb") as file:
                self.prompts.append(pickle.load(file))
                print("Prompts loaded from file.")
        except FileNotFoundError:
            print("Pstart.pkl not found. No prompts loaded.")

    def addPrompt(self, prompt: str):
        self.prompts.append(prompt)

    def removePrompt(self, prompt: str):
        if prompt in self.prompts:
            self.prompts.remove(prompt)

    def getAllPrompts(self):
        return self.prompts

    def selectPrompt(self, prompt: str):
        if prompt in self.prompts:
            self.selectedPrompt = prompt

    def getSelectedPrompt(self):
        return self.prompts[self.selectedPrompt]

    def loadPromptsFromFile(self, filename: str):
        try:
            with open(filename, "rb") as file:
                self.prompts = pickle.load(file)
                print("Prompts loaded from file.")
        except FileNotFoundError:
            print("File not found. No prompts loaded.")

convoManager = ConversationManager()