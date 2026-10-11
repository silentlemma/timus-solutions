def main():
    k = int(input())
    # from the BELL&RET cell upwards: "CALL i + 1" at cell i doubles the
    # bells made from the next cell, a call of the last cell adds one more,
    # so the binary digits of K give the cells
    ops = []
    for bit in format(k, "b")[1:]:
        ops.append("double")
        if bit == "1":
            ops.append("add")
    last = len(ops)
    lines = []
    for cell, op in enumerate(reversed(ops)):
        lines.append("CALL %d" % (cell + 1 if op == "double" else last))
    lines.append("BELL&RET")
    print("\n".join(lines))


main()
