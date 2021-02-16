from tinydb import TinyDB,Query

data_base=TinyDB("db.json")
q=Query()

data_base.remove(q.user_id>2)
data=data_base.all()
print(data)
