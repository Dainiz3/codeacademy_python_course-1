from app import db, Message

asd = Message.query.get(1)
db.session.delete(asd)
db.session.commit()
print(Message.query.all())
