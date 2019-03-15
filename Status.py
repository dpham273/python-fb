from Comment import *
class Status:
    #Status(string,string,list-of-string,list-of-Comment-object)
    def __init__(self,statusPoster,statusMessage,statusLikers,comments):
        self.statusPoster=statusPoster
        self.statusMessage=statusMessage
        self.statusLikers=statusLikers
        self.comments=comments
    def getStatusPoster(self):
        return(self.statusPoster)
    def getStatusMessage(self):
        return(self.statusMessage)
    def getStatusLikers(self):
        return(self.statusLikers)
    def getComments(self):
        return(self.comments)
    def setStatusPoset(self,newStatusPoster):
        self.statusPoster=newStatusPoster
    def setStatusMessage(self,newStatusMessage):
        self.statusMessage=newStatusMessage
    def setStatusLikers(self,newStatusLikers):
        self.statusLikers=newStatusLikers
    def setComments(self,newComments):
        self.comments=newComments
    def addLike(self,newStatusLikers2):
        self.statusLikers.append(newStatusLikers2)
    def addComment(self,newComments):
        self.comments.append(newComments)
    def __str__(self):
        allComment=""
        for aComment in self.comments:
            allComment=allComment+ str(aComment) +"\n"
        if self.comments==[] and self.statusLikers!=[]:
            return(self.statusPoster+ " "+self.statusMessage+"\n"+ (", ".join(self.statusLikers))+ " like this.")
        elif self.comments==[] and self.statusLikers==[]:
            return(self.statusPoster+ " "+self.statusMessage)
        elif self.statusLikers==[]:
            return(self.statusPoster+ " "+self.statusMessage+"\n"+allComment)
        return(self.statusPoster+ " "+self.statusMessage+  "\n"+ (", ".join(self.statusLikers))+ " like this." +"\n"+allComment)
        
