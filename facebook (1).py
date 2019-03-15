from Comment import *
from User import *
from Status import *

class Facebook:
    #Facebook(dict-of-string:user,list-of-status,string)
    def __init__(self):
        self.facebookUser={}
        self.facebookStatus=[]
        self.currentlyUsing=""
    def registerUser(self,name,email):
        user1=User(name,email)
        if name in self.facebookUser:
            print("This username has already been taken")
        else:
            self.facebookUser[name]=user1
    def login(self,name2):
        if self.currentlyUsing!="":
            print("Somebody has already logged into this account and that person needs to log out first")
        else:
            self.currentlyUsing=name2
    def logout(self):
        if self.currentlyUsing=="":
            print("Noone is currently logged in")
        else:
            self.currentlyUsing=""
    def addFriend(self,name):
        if self.currentlyUsing=="":
            print("Noone  is currently logged in")
        elif name not in self.facebookUser:
            print("Cannot find anyone with the given username")
        else:
            friend1=self.facebookUser[self.currentlyUsing]
            friend2=self.facebookUser[name]
            friend1.addFriend(friend2)
    def viewProfile(self):
        currentlyUsingUser=self.facebookUser[self.currentlyUsing]
        print (str(currentlyUsingUser))
    def postStatus(self,theStatus):
         if self.currentlyUsing=="":
            print("Noone is currently logged in")
         else:
            status1=Status(self.currentlyUsing,theStatus,[],[])
            self.facebookStatus.append(status1)
    def viewStatus(self):
        if self.currentlyUsing=="":
            print("Noone  is currently logged in ")
        else:
            viewStatusString=""
            for i in range (len(self.facebookStatus)):
                if self.facebookStatus[i].statusPoster==self.currentlyUsing or self.facebookUser[self.facebookStatus[i].statusPoster] in self.facebookUser[self.currentlyUsing].friends:
                    if len(self.facebookStatus)>1 and len(self.facebookUser[self.currentlyUsing].friends)>1:
                        viewStatusString=viewStatusString+"["+str(i)+"] "+str(self.facebookStatus[i])+"\n"
                    elif len(self.facebookStatus)==1 or len(self.facebookUser[self.currentlyUsing].friends)==1:
                        viewStatusString=viewStatusString+"["+str(i)+"] "+str(self.facebookStatus[i])
            print (viewStatusString)
    def likeStatus(self,IDnumber):
        statusToLike=self.facebookStatus[IDnumber]
        if self.currentlyUsing=="":
            print("Noone  is currently logged in ")
        elif self.facebookUser[statusToLike.statusPoster]!=self.facebookUser[self.currentlyUsing]and self.facebookUser[statusToLike.statusPoster] not in self.facebookUser[self.currentlyUsing].friends:
            print("You cannot like this status because it belongs to the user who is not your friend")
        else:
            statusToLike.statusLikers.append(self.currentlyUsing)
    def commentOnStatus(self,IDnumber,theComment):
        statusToComment=self.facebookStatus[IDnumber]
        if self.currentlyUsing=="":
            print("Noone  is currently logged in ")
        elif self.facebookUser[statusToComment.statusPoster]!=self.facebookUser[self.currentlyUsing]and self.facebookUser[statusToComment.statusPoster] not in self.facebookUser[self.currentlyUsing].friends:
            print("You cannot comment in this status because it belongs to the user who is not your friend")
        else:
            Comment1=Comment(self.currentlyUsing,theComment)
            statusToComment=self.facebookStatus[IDnumber]
            statusToComment.comments.append(Comment1)
        
    
        
    
