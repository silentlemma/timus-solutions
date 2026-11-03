from sys import stdin, stdout

sentence = stdin.readline().lower()
clauses = []
for clause in sentence.split(","):
    # Known marker pairs directly delimit object, subject and verb phrases.
    phrases = [
        clause[clause.index(left) + 1 : clause.index(right)] for left, right in zip("{([", "})]")
    ]
    first_marker = min(clause.index(left) for left in "{([")
    prefix = clause[:first_marker].strip()
    clauses.append(" ".join(([prefix] if prefix else []) + phrases))
answer = ", ".join(clauses)
stdout.write(str(answer[0].upper() + answer[1:]))
