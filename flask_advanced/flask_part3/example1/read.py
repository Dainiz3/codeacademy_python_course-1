from app import Message

all_messages = Message.query.all()

message_1 = Message.query.get(1)
# print(message_1.message)

messages_antanas = Message.query.filter_by(name="Antanelis").first()

print(messages_antanas)
