from app import db, Message

all_messages = Message.query.all()

print(all_messages)

for message in all_messages:
    print(message.name)

message_1 = Message.query.get(1)
print(message_1)


message_antanas = Message.query.filter_by(name="Antanas")
print(type(message_antanas))
print(message_antanas.all())
