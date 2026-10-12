def main():
    limit = int(input())
    # going back from the last replacement: reach is the longest run that
    # the replacements chosen so far turn into a single space
    plan, reach = [], 1
    while reach < limit:
        step = (reach + 1) // 2 + 1  # the best length to replace here
        groups = reach + 2 - step  # most groups in a run that still fits
        reach = groups * step + step - 2
        plan.append(step)
    print(len(plan))
    for step in reversed(plan):
        print(step)


main()
