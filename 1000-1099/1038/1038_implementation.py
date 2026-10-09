import sys

SENTENCE_ENDS = ".?!"


def main():
    text = sys.stdin.read()
    errors = 0
    # a new sentence waits for its first letter; in_word: the previous character
    # was a letter
    new_sentence, in_word = True, False
    for c in text:
        if "a" <= c <= "z":
            errors += new_sentence
            new_sentence, in_word = False, True
        elif "A" <= c <= "Z":
            errors += in_word
            new_sentence, in_word = False, True
        else:
            in_word = False
            if c in SENTENCE_ENDS:
                new_sentence = True
    print(errors)


main()
