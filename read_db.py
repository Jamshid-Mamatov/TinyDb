from tinydb import TinyDB,Query

data_base=TinyDB("db.json")
q=Query()
data=data_base.all()
user=data_base.search(q.user_id>2)

print(user)

