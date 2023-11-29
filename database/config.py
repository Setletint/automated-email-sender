import pymongo

class Database:
    def __init__(self) -> None:
        self.conn = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db_email = self.conn["emails"]
        self.users = self.db_email["users"]

        
    def getAllEmails(self):
        return self.users.distinct('email')
        
    def insertNewUser(self,name,mail):
        exist = self.users.count_documents({'email':mail})
        if(exist > 0):
            return 'Already exist'
        else:
            user = {'user': name, 'email': mail}
            self.users.insert_one(user)

    def deleteUser(self,mail):
        userD = {'email': mail}
        exist = self.users.find({},userD)
        if(exist):
            self.users.delete_one(userD)
