from app import Message, db

print(Message.query.all())

user = Message.query.filter_by(email="jonas@mail.com").first()
print(user.message)
user.email = "jonas1@mail.com"
user.name = "Jonas1"
user.text = "Kažkoks labai rimtas atsiliepimas?"
db.session.add(user)
db.session.commit()
print(Message.query.all())
