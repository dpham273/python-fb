class Comment:
    #Comment (string, string)
    def __init__(self, commentor, content):
        self.commentor=commentor
        self.content=content
    def getCommentor(self):
        return (self.commentor)
    def getContent(self):
        return (self.content)
    def setCommentor(self, newCommentor):
        self.commentor=newCommentor
    def setContent(self,newContent):
        self.content=newContent
    def __str__(self):
        return (self.commentor + ": " + self.content)
    
        
        
