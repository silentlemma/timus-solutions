from os import _exit, write


def respond(values):
    values = iter(values)
    count = int(next(values))
    accounts = {}
    responses = []
    for _ in range(count):
        action, name = next(values), next(values)
        account = accounts.get(name)
        if action == b"register":
            password = next(values)
            if account is not None:
                reply = b"fail: user already exists"
            else:
                accounts[name] = [password, False]
                reply = b"success: new user added"
        elif action == b"login":
            password = next(values)
            if account is None:
                reply = b"fail: no such user"
            elif account[0] != password:
                reply = b"fail: incorrect password"
            elif account[1]:
                reply = b"fail: already logged in"
            else:
                account[1] = True
                reply = b"success: user logged in"
        elif account is None:
            reply = b"fail: no such user"
        elif not account[1]:
            reply = b"fail: already logged out"
        else:
            account[1] = False
            reply = b"success: user logged out"
        responses.append(reply)
    return b"\n".join(responses) + b"\n"


def main():
    # At most 100 requests, each with two names of at most 30 ASCII bytes.
    # Token consumption follows the command arity, even on failed requests.
    values = open(0, "rb", buffering=0).read().split()
    write(1, respond(values))
    _exit(0)


main()
