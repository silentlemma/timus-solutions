def main():
    a, b, c, d = (int(x) for x in input().split())
    petya, driver = a, c
    # the driver never asks less than Petya offers, and the other way round
    if petya >= driver:
        print(petya)
        return
    while True:
        petya += b
        if petya >= driver:
            print(driver)
            return
        driver -= d
        if driver <= petya:
            print(petya)
            return


main()
