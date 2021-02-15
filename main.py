from tinydb import TinyDB

data_base=TinyDB("db.json")
data_base.truncate()

user1={"user_id":1,"username":"Jamshid"}
user2={"user_id":2,"username":"Diyor"}
user3={"user_id":3,"username":"Javohir"}
user4={"user_id":4,"username":"Ali"}


data_base.insert_multiple([user3,user1,user2,user4])