import string
import sys

SMALL = 2


def free_language(spoken):
    """english, or else the first name of one or two letters that no team
    speaks: at most 100 teams cannot take all 702 of them"""
    if "english" not in spoken:
        return "english"
    letters = string.ascii_lowercase
    names = list(letters) + [a + b for a in letters for b in letters]
    return next(name for name in names if name not in spoken)


def main():
    words = sys.stdin.read().split()
    n = int(words[0])
    langs = words[1 : 1 + n]
    if len(set(langs)) < n:
        # a third team would overhear two teams of one language
        print(0 if n == SMALL else "Impossible")
    elif n == 1:
        print(0)
    elif n == SMALL:
        print(1)
        print("%s-%s" % (langs[0], langs[1]))
    else:
        # a talk through another team's language is overheard, so every talk
        # goes through a language no team speaks
        hub = free_language(set(langs))
        print(n)
        print("\n".join("%s-%s" % (lang, hub) for lang in langs))


main()
