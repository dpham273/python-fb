class User:
    #User(string,string)
    def __init__(self,userName, userEmail):
        self.userName=userName
        self.userEmail=userEmail
        self.friends=[]
    def getUserName(self):
        return(self.userName)
    def getUserEmail(self):
        return(self.userEmail)
    def setUserName(self,newUserName):
        self.userName=newUserName
    def setUserEmail(self,newUserEmail):
        self.userEmail=newUserEmail
    def addFriend(self,user):
        self.friends.append(user)
        user.friends.append(self)
    def isFriend(self,user):
        if user in self.friends:
            return True
        else:
            return False
    def __str__(self):
        if self.friends == []:
            return (self.userName + "("+self.userEmail+") \n" + "Friends: None")
        else:
            friendList=[]
            for aFriend in self.friends:
                friendList.append(aFriend.userName)
            friends=", ".join(friendList)
            return(self.userName + "("+self.userEmail+") \n" + "Friends: " +friends)
            
                
