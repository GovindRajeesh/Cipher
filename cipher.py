import sys

# Method to encode
def encode(msg,key):
    asci=""

    for i in msg:
        asci+=chr(int(ord(i))+int(key))

    return asci

# Method for decode
def decode(msg,key):
    asci=""

    for i in msg:
        asci+=chr(int(ord(i))-int(key))

    return asci

print("Welcome to cipher.")
print("This program allows you to send encode sentences and decode it.")
print("This is developed and owned by Govind Rajeesh.")

program=True

while program:
    # Asks decode or encode
    typ=input("E or D (Enter q to exit):").lower()

    # Exit the program when q is entered as input
    if typ=="q":
        print("Bye..")
        sys.exit()
        
    # Asks the message
    msg=input("Enter your message:")

    if typ=="e":
        # Asks the key
        key=input("Enter a key:")

        # Call encode method and print result
        print(encode(msg,key))

    elif typ=="d":
        # Asks the key
        key=input("Enter the key:")

        # Call decode method and print result
        print(decode(msg,key))

    
