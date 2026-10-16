import sys


def main():
    data = list(map(int, sys.stdin.read().split()))
    n, thrown = data[0], data[1:1 + data[0]]
    sys.set_int_max_str_digits(0)
    # build the catch X digit by digit in base n. Adding s n^j to X keeps
    # the first j fishermen happy and adds s (n - 1)^j to what fisherman
    # j + 1 finds, which is s (-1)^j modulo n: that fixes s
    catch = found = 0
    power_n = power_m = 1
    for j, a in enumerate(thrown):
        s = (a - found) % n
        if j % 2:
            s = -s % n
        catch += s * power_n
        found += s * power_m
        # the fisherman throws a fishes away and leaves (n - 1)/n of the rest
        found = (found - a) // n * (n - 1)
        power_n *= n
        power_m *= n - 1
    # every catch of this residue modulo n^n works; at least one fish
    print(catch if catch else power_n)


main()
