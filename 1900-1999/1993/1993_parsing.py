import sys

ROLE_COUNT = 3


def transform(sentence):
    opening = "{(["
    closing = "})]"
    result = []
    for clause in sentence.lower().split(","):
        phrases = [""] * ROLE_COUNT
        prefix = ""
        position = 0
        while position < len(clause):
            character = clause[position]
            if character in opening:
                role = opening.index(character)
                end = clause.index(closing[role], position + 1)
                phrases[role] = clause[position + 1 : end]
                position = end + 1
            elif "a" <= character <= "z":
                end = position + 1
                while end < len(clause) and "a" <= clause[end] <= "z":
                    end += 1
                prefix = clause[position:end]
                position = end
            else:
                position += 1
        result.append(" ".join(([prefix] if prefix else []) + phrases))
    answer = ", ".join(result)
    return answer[0].upper() + answer[1:]


def main():
    print(transform(sys.stdin.readline().strip()))


if __name__ == "__main__":
    main()
