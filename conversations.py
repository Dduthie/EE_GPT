import pickle

class ConversationManager:
    
    def __init__(self) -> None:
        self.currentConversation = 0
        self.conversations = {}

    def addConversation(self):
        newConvo = Conversation()
          
    def changeConversation(self):
        pass
    
    def removeConversation(self):
        pass

    def saveConversation(self):
        pass

    def saveAllConversations(self):
        pass

class Conversation():
    def __init__(self) -> None:
        self.GPTmessages = []
        self.html = []
        self.state = 0
        