from tinydb import TinyDB

data_base=TinyDB("dataBase.json")
data_base.truncate()

user={}
for i in range(10):
    user['id']=int(input("id: "))
    user['first_name']=input("first name: ")
    user['last_name']=input("last name: ")
    user['birthday']=input("Birthday: ")
    user['email']=input("email: ")
    user['job']=input("job: ")
    user['phone']=input("phone: ")
    
    data_base.insert(user)

