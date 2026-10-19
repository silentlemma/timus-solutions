import sys


if __name__ == "__main__":
    sys.stdout.buffer.write(f"{int(sys.argv[1])}\n".encode())
