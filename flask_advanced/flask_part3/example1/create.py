from app import db, Message

db.create_all()


jonas = Message("Jonas", "jonas@mail.com", "Kažkoks labai rimtas atsiliepimas.")
antanas = Message("Antanas", "antanas@mail.lt", "Antano nuomonė labai svarbi.")
juozas = Message("Juozas", "juozukas@friends.lt", "Aš labai piktas, nes blogai.")
bronius = Message("Bronius", "bronka@yahoo.com", "Aš tai linksmas esu, man patinka.")
tomas = Message("Tomas", "tomka@yahoo.com", "Man patinka.")

db.session.add_all([jonas, antanas, juozas, bronius, tomas])
db.session.commit()

print(jonas.id)
print(antanas.id)
print(bronius.id)
print(juozas.id)
print(tomas.id)
