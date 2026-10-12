def main():
    n = int(input())
    # modulo n^2 + 1 the first number is -1 and the second is n, so the sum
    # of their squares is 1 + n^2, a multiple of n^2 + 1
    print(n * n, n * n + n + 1, n * n + 1)


main()
