import math
import sys

ADMIN = "admin"
MAX_EXPONENT = 30


def perfect_power(value):
    """Write value as root ** exponent with the largest possible exponent."""
    for exponent in range(MAX_EXPONENT, 1, -1):
        guess = round(value ** (1 / exponent))
        for root in range(max(2, guess - 1), guess + 2):
            if root**exponent == value:
                return root, exponent
    return value, 1


def main():
    source = sys.stdin.buffer
    count, _, multiplier, divisor = map(int, source.readline().split())
    log_good = math.log(multiplier)
    log_fun = math.log(divisor)
    # A^g = B^f exactly when both are powers of one root with matching
    # exponents; a base of 1 contributes nothing.
    related = True
    scale_good, scale_fun = int(multiplier > 1), int(divisor > 1)
    if multiplier > 1 and divisor > 1:
        good_root, scale_good = perfect_power(multiplier)
        fun_root, scale_fun = perfect_power(divisor)
        related = good_root == fun_root
    players = {ADMIN: [0, 0, True]}
    total_good = 0
    total_fun = 0
    online = 1
    output = []

    for _ in range(count):
        line = source.readline().decode().rstrip("\r\n")
        _, _, body = line.partition(" ")
        author, command = body.split(": /", 1)
        kind = command[0]
        if kind == "j":
            player = players.setdefault(author, [0, 0, False])
            if player[2]:
                response = f"Failed: {author} is already on the server"
            else:
                player[0] -= total_good
                player[1] -= total_fun
                player[2] = True
                online += 1
                response = "Successful"
        elif kind == "q":
            player = players[author]
            player[0] += total_good
            player[1] += total_fun
            player[2] = False
            online -= 1
            response = "Successful"
        elif kind == "o":
            response = f"There are {online} players on the server"
        elif kind in ("s", "w"):
            _, _, message = command.partition(" ")
            good = message.count("g")
            fun = len(message) // 2 - good
            if kind == "s":
                # Online players share the totals; exclude the author's own message.
                total_good += good
                total_fun += fun
                player = players[author]
                player[0] -= good
                player[1] -= fun
                response = f"{author}: {message}"
            else:
                target = command[command.index("<") + 1 : command.index(">")]
                recipient = players.get(target)
                if recipient is not None and recipient[2]:
                    recipient[0] += good
                    recipient[1] += fun
                response = f"{author} (to {target}): {message}"
        else:
            if author != ADMIN:
                output.append("Failed: you have no such rights")
                continue
            targets = command[command.index("<") + 1 : -1].split(">-<")
            pair = len(targets) == 2
            first, second = targets if pair else (ADMIN, targets[0])
            left = players.get(first)
            right = players.get(second)
            if left is None or not left[2]:
                response = f"Failed: {first} is not on the server"
            elif right is None or not right[2]:
                response = f"Failed: {second} is not on the server"
            else:
                # Shared totals cancel before converting integer differences to floats.
                good = left[0] - right[0]
                fun = left[1] - right[1]
                if related:
                    equal = good * scale_good == fun * scale_fun
                else:
                    equal = good == 0 and fun == 0
                if equal:
                    response = "Their luck is equal" if pair else f"{second} is good"
                elif good * log_good - fun * log_fun > 0:
                    response = f"{second} is a loser"
                else:
                    response = f"{second} is a lucky guy"
        output.append(response)

    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()
