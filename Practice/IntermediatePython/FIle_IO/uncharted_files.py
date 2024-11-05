sent_message = 'This message has been unsent.'

with open('sent_message.txt', 'w') as f:
    f.write(sent_message)
    
# Truncate the message
with open('sent_message.txt', 'a') as f:
    f.truncate(29)

# Read the message and use seek
# r+ is read and writing are allowed
with open('sent_message.txt', 'r+') as f:
    origianl_message = f.read()
    print(origianl_message)
    f.seek(0)