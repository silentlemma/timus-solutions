import re
import sys


def main():
    words = re.findall(r"[a-z]+", sys.stdin.read())
    trams, trolleys = words.count("tram"), words.count("trolleybus")
    if trams > trolleys:
        print("Tram driver")
    elif trolleys > trams:
        print("Trolleybus driver")
    else:
        print("Bus driver")


main()
