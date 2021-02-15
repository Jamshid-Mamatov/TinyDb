from tinydb import TinyDB

data_base=TinyDB("db.json")

user1={"user_id":1,"username":"Jamshid"}
user2={"user_id":2,"username":"Diyor"}
user3={"user_id":3,"username":"Javohir"}

data_base.insert(user1)
data_base.insert(user2)
data_base.insert(user3)