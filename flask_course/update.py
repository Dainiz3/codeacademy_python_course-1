from app import db, Message

antanas = Message.query.get(3)
antanas.email = "geras.zmogus@gmail.lt"
db.session.add(antanas)
db.session.commit()
print(Message.query.all())
