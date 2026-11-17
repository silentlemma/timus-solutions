def main():
    teams = sorted(open(0, "rb", buffering=0).read().split()[1:])
    previous = printed = None
    for team in teams:
        if team == previous and team != printed:
            print(team.decode())
            printed = team
        previous = team


main()
