def print_welcome_message(msg1, msg2):
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    print("-"*nstr*2)
    print("Hello",msg1)
    print(msg2)
    print("-"*nstr*2)

msg1=input("Input name: ")
print_welcome_message(msg1, "Welcome to Seoul.")