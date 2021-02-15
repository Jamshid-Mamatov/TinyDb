from tinydb import TinyDB

data_base=TinyDB("db.json")

data=data_base.all()
print(data)