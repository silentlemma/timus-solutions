import os
from sys import stdout

source = open(0, "rb")
count = int(source.readline())
accounts = {}
for _ in range(count):
    command = source.readline().split()
    action, name = command[:2]
    account = accounts.get(name)
    if action == b"register":
        if account is not None:
            reply = "fail: user already exists"
        else:
            accounts[name] = [command[2], False]
            reply = "success: new user added"
    elif action == b"login":
        if account is None:
            reply = "fail: no such user"
        elif account[0] != command[2]:
            reply = "fail: incorrect password"
        elif account[1]:
            reply = "fail: already logged in"
        else:
            account[1] = True
            reply = "success: user logged in"
    elif account is None:
        reply = "fail: no such user"
    elif not account[1]:
        reply = "fail: already logged out"
    else:
        account[1] = False
        reply = "success: user logged out"
    print(reply)

# The answer is flushed before interpreter teardown is skipped.
stdout.flush()
os._exit(0)
