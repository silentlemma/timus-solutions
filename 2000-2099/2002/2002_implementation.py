import sys


def process(commands):
    accounts = {}
    replies = []
    for command in commands:
        action, name = command[:2]
        account = accounts.get(name)
        if action == "register":
            if account is not None:
                reply = "fail: user already exists"
            else:
                accounts[name] = [command[2], False]
                reply = "success: new user added"
        elif action == "login":
            if account is None:
                reply = "fail: no such user"
            elif account[0] != command[2]:
                reply = "fail: incorrect password"
            elif account[1]:
                reply = "fail: already logged in"
            else:
                account[1] = True
                reply = "success: user logged in"
        else:
            if account is None:
                reply = "fail: no such user"
            elif not account[1]:
                reply = "fail: already logged out"
            else:
                account[1] = False
                reply = "success: user logged out"
        replies.append(reply)
    return replies


def main():
    input_file = sys.stdin.buffer
    count = int(input_file.readline())
    commands = [input_file.readline().decode("ascii").split() for _ in range(count)]
    sys.stdout.write("\n".join(process(commands)) + "\n")


if __name__ == "__main__":
    main()
